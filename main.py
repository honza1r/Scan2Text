"""Version - BigUpdate.SmallUpdate.BugFixes"""
__version__ ="1.0.0"

"""Imports at the top"""
import fitz
import numpy as np
import easyocr

"""Code settings""" 


"""Classes""" 


"""Functions"""
def scanText(filepath):
    reader = easyocr.Reader(languages)
    if sourceFilepath.split('.')[-1].lower() == "pdf":
        print("im here")
        pages = fitz.open(filepath)
        print("pdf laoded")
        for page in pages:
            result = reader.readtext(np.array(page.get_pixmap(dpi=300).pil_image()))
            for bbox, text, confidence in result:
                if confidence > 0.5:
                    print(text)
    else:
        result = reader.readtext(sourceFilepath)
        with open(filepath, 'w', encoding='utf-8') as f:
            for bbox, text, confidence in result:
                if confidence > 0.5:
                    f.write(text+"\n")

"""Program variables"""
sourceFilepath = ""
languages = []

"""Code"""

