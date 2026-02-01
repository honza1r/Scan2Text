"""Imports at the top"""
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import ttkbootstrap as tb  # For modern themes
import main as be
import sys
import os

def buttonFuncOpenFile():
    # Open a file dialog to select a file
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    filepath = filedialog.askopenfilename(
        title="Vyberte zdrojový soubor", # HERE GO INSTRUCTION FOR THE USER AS TO WHICH FILE THEY'RE SUPPOSED TO SELECT
        filetypes=[("PNG", "*.png"),("JPEG", "*.jpeg"),("PDF", "*.pdf")] # HERE GO ALLOWED FILETYPES THAT CAN BE SELECTED
    )
    
    if not filepath:
        insertToMessageBox("Žádný soubor nebyl vybrán")
        return None

    be.printText(filepath)
    # Attempt to process the filepath
    # try:
    #     """HERE GOES CODE FOR DOING SOMETHING WITH THE FILEPATH"""
    #     be.printText(filepath)
    # except Exception as e:
    #     insertToMessageBox(f"Chyba při nahrávání souboru: {e}")
    

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

"""Drop-down Menus"""
dropDownExample = ttk.Combobox(root, width=21, state='enabled')
dropDownExample['values'] = ["Option 1", "Option 2", "Option 3"]
dropDownExample.bind("<<ComboboxSelected>>", dropDownChange) # Function that gets called whenever theres a new selection made
dropDownExample.place(x=x+1, y=y+40)

"""Checkboxes"""
checkboxExample = tk.IntVar(value=1)  
checkboxExample = ttk.Checkbutton(root, text="Example Checkbox", variable=checkboxExample) 
checkboxExample.place(x=x+485, y=y)

"""Message Box"""
messageBox = tk.Text(root, height=8, width=72, wrap="none", state=tk.NORMAL, takefocus=False, font = ("Arial", 12, "bold")) #Whenever text need be changed the window first needs be enabled and disabled again (to prevent user interaction)
messageBox.place(x=x, y=y+80)
messageBox.config(state=tk.DISABLED) #message box needs to be disabled to prevent user input!!!
insertToMessageBox("Vyberte scan na přepsání\n") # PLACE INITIAL INSTRUCTION FOR THE USER
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