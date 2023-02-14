
#import CV_filler

import CV_filler
import os

#test parseArgs()
def test_parseArgs():
    '''
    Test the default values for argparse arguments
    '''
    args = CV_filler.parseArgs()
    assert args.jsonInput == "input/CV.json"
    assert args.templateInput == "input/CV_template.md"

def test_args():
    '''
    Use input from testFiles to test the values for argparse arguments
    '''
    cv = CV_filler.CV_filler(
        jsonData="testFiles/CV.json", 
        cvTemplate="testFiles/CV_template.md",
        outputDir="testOutput/"
    )
    assert cv.jsonData == "testFiles/CV.json"
    assert cv.cvTemplate == "testFiles/CV_template.md"
    assert cv.outputDir == "testOutput/"

def test_getJsonData():
    '''
    Test the getJsonData method
    '''
    cv = CV_filler.CV_filler(
        jsonData="testFiles/CV.json", 
        cvTemplate="testFiles/CV_template.md",
        outputDir="testOutput/"
    )
    assert cv.getJsonData() == {
        "{company address}": "company address",
        "{company name}": "Business Team",
        "{position}": "Data analyst",
        "{location}":"Nedlands, WA"
    }

def test_getCVTemplate():
    '''
    Test the getCVTemplate method
    '''
    cv = CV_filler.CV_filler(
        jsonData="testFiles/CV.json", 
        cvTemplate="testFiles/CV_template.md",
        outputDir="testOutput/"
    )
    assert "{company name}" in cv.getCVTemplate()

def test_writeCV():
    '''
    Test the writeCV method
    '''
    cv = CV_filler.CV_filler(
        jsonData="testFiles/CV.json", 
        cvTemplate="testFiles/CV_template.md",
        outputDir="testOutput/"
    )
    cv.writeCV(cv.fillCV())
    assert os.path.exists(cv.outputFileName + ".md")
