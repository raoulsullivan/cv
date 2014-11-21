"""Converts markdown to html and pdf"""
import markdown
import argparse
import pdfkit

if __name__ == "__main__":
    """Import arguments, run the thing"""
    parser = argparse.ArgumentParser(description='Convert .md to .html')
    parser.add_argument('input',type=str,help='Input .md file')
    parser.add_argument('output',type=str,help='Output .html file - will also do a pdf file of same name')
    arguments = vars(parser.parse_args())
    markdown.markdownFromFile(input=arguments['input'],output=arguments['output'])
    pdffile = arguments['output'].split('.')[0] + ".pdf"
    pdfkit.from_file(arguments['output'],pdffile)
