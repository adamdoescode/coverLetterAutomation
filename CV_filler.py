# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    CV_filler.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Adam Graham <13943324+adamdoescode@user    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/25 09:31:07 by adam              #+#    #+#              #
#    Updated: 2023/01/25 16:32:45 by Adam Graham      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
A simple script to fill the CV with the data from the json file
'''

import json
import sys
import os

#we can hardcode the path to the json file, assumes has a specific name and is in the same directory
class CV_filler:
    def __init__(self):
        self.jsonData = "CV.json"
        self.cvTemplate = "CV_template.md"
    
    def getJsonData(self):
        with open(f'input/{self.jsonData}', "r") as jsonFile:
            data = json.load(jsonFile)
        return data['details']

    def getCVTemplate(self):
        with open(f'input/{self.cvTemplate}', "r") as cvFile:
            data = cvFile.read()
        return data
    
    def getDate(self):
        '''date is easier to get from python'''
        import datetime
        return datetime.datetime.now().strftime("%Y-%m-%d")
    
    def fillCV(self):
        data = self.getJsonData()
        cv = self.getCVTemplate()
        for key in data.keys():
            cv = cv.replace(key, data[key])
        #do the date separately
        cv = cv.replace("{date}", self.getDate())
        return cv

    def writeCV(self, cv):
        #get company name from json and replace spaces with _
        company_name = self.getJsonData()['{company name}'].replace(' ', '_')
        self.outputFileName = f"output/{self.getDate()}_{company_name}_CV_filled"
        with open(f"{self.outputFileName}.md", "w") as cvFile:
            cvFile.write(cv)
    
    def main(self):
        cv = self.fillCV()
        self.writeCV(cv)



if __name__ == "__main__":
    CVmaker = CV_filler()
    CVmaker.main() #fill the CV, CV maker now has a file name to use
    #use pandoc to convert md to docx
    os.system(f"pandoc {CVmaker.outputFileName}.md -o {CVmaker.outputFileName}.docx")
