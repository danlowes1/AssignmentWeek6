import os
from easygui import diropenbox # Import the directory open box function

def select_folder_easygui():
    """
    Opens a simple folder selection dialog using easygui.
    Returns the selected folder path as a string, or None if cancelled.
    """
    folder_path = diropenbox(
        title="Select a Folder",
        default=os.getcwd() # Set initial directory
    )
    # easygui returns None if the user cancels
    return folder_path

# Then in your collect_project_info():
if __name__ == "__main__":



    # Use the easygui version
    file_path = select_folder_easygui() 

    # if file_path is None:
    #     console.print("[yellow]Folder selection cancelled. README.md will not be created.[/yellow]")
    #     return 

    # ... rest of your code using file_path ...