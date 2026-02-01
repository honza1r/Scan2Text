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
    with open(filepath, 'w', encoding='utf-8') as f:
        if sourceFilepath.split('.')[-1].lower() == "pdf":
            pages = fitz.open(sourceFilepath)
            progress = 0
            for page in pages:
                img = np.array(page.get_pixmap(dpi=300, colorspace=fitz.csGRAY).pil_image())
                result = reader.readtext(img)
                for bbox, text, confidence in result:
                    if confidence > 0.5:
                        f.write(text+"\n")
                progress += 1
                print(progress/len(pages))
        else:
            result = reader.readtext(sourceFilepath)
            for bbox, text, confidence in result:
                if confidence > 0.5:
                    f.write(text+"\n")

"""Program variables"""
sourceFilepath = ""
languages = []

"""Code"""

