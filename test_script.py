
#import CV_filler

import json
import CV_filler
import os

TEST_JSON_DATA = "testFiles/CV.json"
TEST_PRIVATE_JSON_DATA = "testFiles/privateInput.json"
TEST_TEMPLATE = "testFiles/CV_template.md"
TEST_OUTPUT_DIR = "testOutput/"

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
        privateJsonData=TEST_PRIVATE_JSON_DATA,
        cvTemplate=TEST_TEMPLATE,
        outputDir=TEST_OUTPUT_DIR
    )
    assert cv.jsonData == TEST_JSON_DATA
    assert cv.cvTemplate == TEST_TEMPLATE
    assert cv.outputDir == TEST_OUTPUT_DIR

def test_getJsonData():
    '''
    Test the getJsonData method
    '''
    cv = CV_filler.CV_filler(
        jsonData=TEST_JSON_DATA, 
        privateJsonData=TEST_PRIVATE_JSON_DATA,
        cvTemplate=TEST_TEMPLATE,
        outputDir=TEST_OUTPUT_DIR
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
        privateJsonData=TEST_PRIVATE_JSON_DATA,
        cvTemplate=TEST_TEMPLATE,
        outputDir=TEST_OUTPUT_DIR
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
        privateJsonData=TEST_PRIVATE_JSON_DATA,
        cvTemplate=TEST_TEMPLATE,
        outputDir=TEST_OUTPUT_DIR
    )
    cv.main()
    assert os.path.exists(cv.outputFileName + ".md")

def test_textPresentBeforeReplacement():
    '''
    Ensure cv text is replaced with data from json file
    '''
    cv = CV_filler.CV_filler(
        jsonData=TEST_JSON_DATA, 
        privateJsonData=TEST_PRIVATE_JSON_DATA,
        cvTemplate=TEST_TEMPLATE,
        outputDir=TEST_OUTPUT_DIR
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
        privateJsonData=TEST_PRIVATE_JSON_DATA,
        cvTemplate=TEST_TEMPLATE,
        outputDir=TEST_OUTPUT_DIR
    )
    #need to get CV template
    cv.getCVTemplate()
    assert cv.cvText
    for key in cv.getJsonData().keys():
        assert key not in cv.fillCV()

def test_privateJson_tags_in_template():
    '''
    Test the private json data is output into the template
    '''
    cv = CV_filler.CV_filler(
        jsonData=TEST_JSON_DATA, 
        privateJsonData=TEST_PRIVATE_JSON_DATA,
        cvTemplate=TEST_TEMPLATE,
        outputDir=TEST_OUTPUT_DIR
    )
    cv.getCVTemplate()
    assert cv.cvText
    #get info from test private json file
    with open(TEST_PRIVATE_JSON_DATA) as f:
        privateData = json.load(f)['privateDetails']
    for key in privateData.keys():
        assert key in cv.cvText

def test_privateJson_tags_replaced_in_output():
    '''
    Test the private json data is output into the template
    '''
    cv = CV_filler.CV_filler(
        jsonData=TEST_JSON_DATA, 
        privateJsonData=TEST_PRIVATE_JSON_DATA,
        cvTemplate=TEST_TEMPLATE,
        outputDir=TEST_OUTPUT_DIR
    )
    cv.getCVTemplate()
    assert cv.cvText
    cv.privateFillCV()
    #get info from test private json file
    with open(TEST_PRIVATE_JSON_DATA) as f:
        privateData = json.load(f)['privateDetails']
    for key in privateData.keys():
        assert privateData[key] in cv.cvText

# if main, for deb
if __name__ == "__main__":
    test_parseArgs()
    test_args()
    test_getJsonData()
    test_getCVTemplate()
    test_writeCV()
    test_textPresentBeforeReplacement()
    test_textReplaced()
    test_privateJson_tags_in_template()
    test_privateJson_tags_replaced_in_output()
    print("All tests passed")
