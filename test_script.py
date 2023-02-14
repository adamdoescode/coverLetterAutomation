
#import CV_filler

import CV_filler

#test parseArgs()
def test_parseArgs():
    '''
    Test the default values for argparse arguments
    '''
    args = CV_filler.parseArgs()
    assert args.jsonInput == "input/CV.json"
    assert args.templateInput == "input/CV_template.md"
    
