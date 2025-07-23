import tkinter as tk
from tkinter import filedialog
import os

def select_folder():

    root = tk.Tk() # Create a Tkinter root window
    root.withdraw() #  hide it as we only need the file dialog

    folder_path = filedialog.askdirectory(
        title="Select a Folder",
        initialdir=os.getcwd()  #  Set the initial directory
    )
    return folder_path

if __name__ == "__main__":
    select_folder()