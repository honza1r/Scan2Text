"""Version - BigUpdate.SmallUpdate.BugFixes"""
__version__ ="1.0.0"

"""Imports at the top"""
import easyocr

"""Code settings""" 


"""Classes""" 


"""Functions"""
def printText(filepath):
    reader = easyocr.Reader(['en', 'hu'])
    result = reader.readtext(filepath)
    for bbox, text, confidence in result:
        if confidence > 0.5:
            print(text)

"""Program variables"""


"""Code"""

