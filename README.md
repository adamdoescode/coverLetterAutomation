
# CoverLetter automation

I want to write a simple script that will automate the process of writing cover letters.

I want to be able to write a cover letter once, and then have the script fill in the blanks for me.

So I have two ideas about how to do this:
1. use R and pagedown with variable names to fill this in
2. use Python to fill in the blanks and write to a word document or markdown file

I will try the python route first as I find the text manipulation is more effective there.

## python approach design

- a template.md file (`CV_template.md`) which acts as the template for the cover letter
- a python script (`CV_filler.py`) which will fill in the blanks
- a JSON file (`CV.json`) which will contain the data to fill in the blanks

The python script will read in the template and JSON and output a new file with the blanks filled in (`resume_filled.md`).

Once that is functional I will write a wrapper script that can convert the md file to a docx file and a pdf file.

## TODO

- [x] write CV_filler.py to fill in the blanks
- [x] add date to output file, and send it to a dedicated sub folder (add this to .gitignore!)
- [x] move input files to dedicated dir
- [ ] automate conversion to docx and pdf with pandoc


