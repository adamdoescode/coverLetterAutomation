
#import CV_filler

import json
import CV_filler
import os

TEST_JSON_DATA = "testFiles/CV.json"
TEST_TEMPLATE = "testFiles/CV_template.md"

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
        jsonData=TEST_JSON_DATA, 
        cvTemplate=TEST_TEMPLATE,
        outputDir="testOutput/"
    )
    assert cv.jsonData == TEST_JSON_DATA
    assert cv.cvTemplate == TEST_TEMPLATE
    assert cv.outputDir == "testOutput/"

def test_getJsonData():
    '''
    Test the getJsonData method
    '''
    cv = CV_filler.CV_filler(
        jsonData=TEST_JSON_DATA, 
        cvTemplate=TEST_TEMPLATE,
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
        jsonData=TEST_JSON_DATA, 
        cvTemplate=TEST_TEMPLATE,
        outputDir="testOutput/"
    )
    cv.getCVTemplate()
    assert cv.cvText
    assert len(cv.cvText) > 0

def test_writeCV():
    '''
    Test the writeCV method
    '''
    cv = CV_filler.CV_filler(
        jsonData=TEST_JSON_DATA, 
        cvTemplate=TEST_TEMPLATE,
        outputDir="testOutput/"
    )
    cv.writeCV(cv.fillCV())
    assert os.path.exists(cv.outputFileName + ".md")

def test_textPresentBeforeReplacement():
    '''
    Ensure cv text is replaced with data from json file
    '''
    cv = CV_filler.CV_filler(
        jsonData=TEST_JSON_DATA, 
        cvTemplate=TEST_TEMPLATE,
        outputDir="testOutput/"
    )
    #need to get CV template
    cv.getCVTemplate()
    assert cv.cvText
    for key in cv.getJsonData().keys():
        assert key in cv.cvText

def test_textReplaced():
    '''
    Ensure cv text is replaced with data from json file
    '''
    cv = CV_filler.CV_filler(
        jsonData=TEST_JSON_DATA, 
        cvTemplate=TEST_TEMPLATE,
        outputDir="testOutput/"
    )
    #need to get CV template
    cv.getCVTemplate()
    assert cv.cvText
    for key in cv.getJsonData().keys():
        assert key not in cv.fillCV()

