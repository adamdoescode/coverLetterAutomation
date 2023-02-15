# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    CV_filler.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Adam Graham <13943324+adamdoescode@user    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/25 09:31:07 by adam              #+#    #+#              #
#    Updated: 2023/02/15 08:22:59 by Adam Graham      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
A simple script to fill the CV with the data from the json file
'''

import json
import argparse
import os


def parseArgs():
    parser = argparse.ArgumentParser(
        description='Fill CV with data from json file')
    parser.add_argument(
        '-i', '--input', help='path to json file', 
        dest='jsonInput', default='input/CV.json')
    parser.add_argument(
        '-p', '--privateInput', help='path to json file', 
        dest='privateJsonInput', default='privateInput/privateInput.json')
    parser.add_argument(
        '-o', '--output', help='output directory, defaults to output/', 
        dest='outputDir', default='output/')
    parser.add_argument(
        '-t', '--template', help='path to CV template', 
        dest='templateInput', default='input/CV_template.md')
    return parser.parse_args()

# we can hardcode the path to the json file, assumes has a specific name
# and is in the same directory


class CV_filler:
    def __init__(
        self,
        jsonData="CV.json",
        privateJsonData="privateInput/privateInput.json",
        cvTemplate="CV_template.md",
        outputDir="output/"
    ):
        self.jsonData = jsonData
        self.cvTemplate = cvTemplate
        self.outputDir = outputDir
        self.privateJsonData = privateJsonData

    def getJsonData(self):
        with open(f'{self.jsonData}', "r") as jsonFile:
            data = json.load(jsonFile)
        return data['details']

    def getCVTemplate(self):
        with open(f'{self.cvTemplate}', "r") as cvFile:
            data = cvFile.read()
        self.cvText = data

    def getDate(self):
        '''date is easier to get from python'''
        import datetime
        return datetime.datetime.now().strftime("%Y-%m-%d")

    def fillCV(self):
        data = self.getJsonData()
        self.getCVTemplate()  # get the template text
        # creates the cvText attribute with string data in it
        for key in data.keys():
            self.cvText = self.cvText.replace(key, data[key])
        # do the date separately
        self.cvText = self.cvText.replace("{date}", self.getDate())
        return self.cvText

    def privateFillCV(self):
        '''
        Pull in private details from a separate json file held outside the git repo
        '''
        with open(f'{self.privateJsonData}', "r") as privateJsonFile:
            privateData = json.load(privateJsonFile)["privateDetails"]
        for key in privateData.keys():
            self.cvText = self.cvText.replace(key, privateData[key])
        return self.cvText

    def writeCV(self):
        # get company name from json and replace spaces with _
        company_name = self.getJsonData()['{company name}'].replace(' ', '_')
        self.outputFileName = f"{self.outputDir}/{self.getDate()}_{company_name}_CV_filled"
        with open(f"{self.outputFileName}.md", "w") as cvFile:
            cvFile.write(self.cvText)

    def main(self):
        self.fillCV()
        self.privateFillCV()
        self.writeCV()


if __name__ == "__main__":
    args = parseArgs()
    CVmaker = CV_filler(jsonData=args.jsonInput, cvTemplate=args.templateInput)
    CVmaker.main()  # fill the CV, CV maker now has a file name to use
    # use pandoc to convert md to docx
    os.system(
        f"pandoc {CVmaker.outputFileName}.md -o {CVmaker.outputFileName}.docx")
