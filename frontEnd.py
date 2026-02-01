"""Imports at the top"""
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import ttkbootstrap as tb  # For modern themes
import main as be
import sys
import os
from pathlib import Path

def buttonFuncOpenFile():
    # Open a file dialog to select a file
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    filepath = filedialog.askopenfilename(
        title="Vyberte zdrojový soubor", # HERE GO INSTRUCTION FOR THE USER AS TO WHICH FILE THEY'RE SUPPOSED TO SELECT
        filetypes=[("PDF", "*.pdf"),("PNG", "*.png"),("JPEG", "*.jpeg")] # HERE GO ALLOWED FILETYPES THAT CAN BE SELECTED
    )
    
    if not filepath:
        insertToMessageBox("Žádný soubor nebyl vybrán")
        return None

    insertToMessageBox("Zdrojový Soubor: " + filepath)
    be.sourceFilepath = filepath
    
def buttonFuncCreateText():
    # Open a file dialog to select a file
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    folderpath = filedialog.askdirectory(
        title="Vyberte cílovou složku"  # "Select the target folder"
    )
    
    if not folderpath:
        insertToMessageBox("Žádná složka nebyla vybrána")
        return None
    
    folderpath += "/" + Path(be.sourceFilepath).stem + ".txt"
    
    be.languages = []
    if checkboxEnglish_var.get() == 1:
        be.languages.append('en')
    if checkboxCzech_var.get() == 1:
        be.languages.append('cs')
    if checkboxHungarian_var.get() == 1:
        be.languages.append('hu')
    if checkboxItalian_var.get() == 1:
        be.languages.append('it')
    if checkboxUkranian_var.get() == 1:
        be.languages.append('uk')
    if checkboxRussian_var.get() == 1:
        be.languages.append('ru')
    print(be.languages)
    be.scanText(folderpath)
    
    insertToMessageBox("Text uložený do: " + folderpath)

def dropDownChange(event):
    selection = dropDownExample.get()
    

def insertToMessageBox(text):
    messageBox.config(state=tk.NORMAL) #message box needs to be disabled to prevent user input!!!
    messageBox.insert(tk.END,text+"\n") 
    messageBox.config(state=tk.DISABLED) #message box needs to be disabled to prevent user input!!!

def closeApp():
    insertToMessageBox("Ukončuji aplikaci")
    root.quit()     # Stops the mainloop
    sys.exit()      # Fully exits the script

def resourcePath(relative_path):
    """Get absolute path to resource, neccessary when turning into .exe with PyInstaller"""
    try:
        base_path = sys._MEIPASS  # Folder created by PyInstaller
    except AttributeError:
        base_path = os.path.abspath(".")  # Normal dev run

    return os.path.join(base_path, relative_path)

"""Start tkinter application window"""
root = tb.Window(themename="cosmo")  
root.minsize(700,300) # CHANGE ACCORDING TO YOUR DESIRED APP SIZE
root.geometry("700x300") # CHANGE ACCORDING TO YOUR DESIRED APP SIZE
root.title("Scan2Text"+" "+be.__version__) # CHANGE STRING TO DESIRED APP NAME
# root.iconbitmap(resourcePath("Resources/soma_icon.ico"))
root.state('normal')  # start in maximized window
root.update_idletasks()  # ensure window is maximized before I get its information
window_x = root.winfo_width()  # get window size information
window_y = root.winfo_height()  # get window size information
x = window_x * 0.01 # these will function as reference for all UIX objects
y = window_y * 0.05

"""Buttons"""
buttonOpenFile = ttk.Button(root, text="Vybrat Scan", command=buttonFuncOpenFile, takefocus=True, width=22)
buttonOpenFile.place(x=x, y=y)
buttonOpenFile.config(state="enabled") 

buttonScanToText = ttk.Button(root, text="Vytvořit Přepis", command=buttonFuncCreateText, takefocus=True, width=22)
buttonScanToText.place(x=x, y=y+40)
buttonScanToText.config(state="enabled") 

"""Checkboxes"""
checkboxEnglish_var = tk.IntVar(value=0)  
checkboxEnglish = ttk.Checkbutton(root, text="Angličtina", variable=checkboxEnglish_var) 
checkboxEnglish.place(x=x+175, y=y)

checkboxCzech_var = tk.IntVar(value=0)  
checkboxCzech = ttk.Checkbutton(root, text="Čeština", variable=checkboxCzech_var) 
checkboxCzech.place(x=x+175, y=y+19)

checkboxHungarian_var = tk.IntVar(value=0)  
checkboxHungarian = ttk.Checkbutton(root, text="Maďarština", variable=checkboxHungarian_var) 
checkboxHungarian.place(x=x+175, y=y+38)

checkboxItalian_var = tk.IntVar(value=0)  
checkboxItalian = ttk.Checkbutton(root, text="Italština", variable=checkboxItalian_var) 
checkboxItalian.place(x=x+175, y=y+57)

checkboxUkranian_var = tk.IntVar(value=0)  
checkboxUkranian = ttk.Checkbutton(root, text="Ukrajinština", variable=checkboxUkranian_var) 
checkboxUkranian.place(x=x+260, y=y)

checkboxRussian_var = tk.IntVar(value=0)  
checkboxRussian = ttk.Checkbutton(root, text="Ruština", variable=checkboxRussian_var) 
checkboxRussian.place(x=x+260, y=y+19)

"""Message Box"""
messageBox = tk.Text(root, height=8, width=72, wrap="none", state=tk.NORMAL, takefocus=False, font = ("Arial", 12, "bold")) #Whenever text need be changed the window first needs be enabled and disabled again (to prevent user interaction)
messageBox.place(x=x, y=y+80)
messageBox.config(state=tk.DISABLED) #message box needs to be disabled to prevent user input!!!
insertToMessageBox("Vyberte scan na přepsání") # PLACE INITIAL INSTRUCTION FOR THE USER
# Add scrollbars to the Text widget
scrollbarY = ttk.Scrollbar(root, command=messageBox.yview)
scrollbarY.place(x=x + 659, y=y+80, height = 177) 
scrollbarX = ttk.Scrollbar(root, command=messageBox.xview, orient="horizontal")
scrollbarX.place(x=x, y=y+246, width = 659) 
messageBox.configure(yscrollcommand=scrollbarY.set)
messageBox.configure(xscrollcommand=scrollbarX.set)


# Bind the window close event (clicking the "X")
root.protocol("WM_DELETE_WINDOW", closeApp)
# Start Application
root.mainloop()