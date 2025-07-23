from InquirerPy import prompt
from rich.console import Console
from rich.panel import Panel
import tkinter as tk
from tkinter import filedialog
import os
import questionary 
from easygui import diropenbox # Import the directory open box function. # Or from tkinter import filedialog

# Modules
import data_val as dv

console = Console()

def select_folder_easygui():

    root = tk.Tk()
    root.withdraw() # Hide the main window

    try:
        folder_path = diropenbox(
            title="Select a Folder",
            default=os.getcwd()
        )
    finally:
        # This is critical: ensure the Tkinter root window is destroyed
        # whether the user selects a path or cancels.
        root.destroy()
    
    return folder_path
    
    # folder_path = diropenbox(
    #     title="Select a Folder",
    #     default=os.getcwd() # Set initial directory
    # )
    # # easygui returns None if the user cancels
    # return folder_path

def collect_project_info():

    console.print(Panel("[bold yellow]README.md File Generator[/bold yellow]", expand=False))

    response = questionary.confirm(
        "Continue?", 
        default=None, 
        auto_enter=True
    ).ask()

    if not response:  
        console.print("[yellow]README.md  File Generator cancelled.[/yellow]")
        return

    title = dv.rich_prompt("What is the title of your project?", color="cyan", validator=dv.validate_not_empty)

    description = dv.rich_prompt("Provide a brief description", color="yellow")
    installation = dv.rich_prompt("Installation instructions", color="cyan")
    
    usage = dv.rich_prompt("How will your project be used", color="yellow")
    author = dv.rich_prompt("Who is the author of this project", color="cyan")
    email = dv.rich_prompt("What is your email address", color="yellow", validator=dv.validate_email)

    #  using a Dictionary for the license list
    licenses = {
        "MIT License": "Permissive, allows modification and distribution with attribution.",
        "Apache License 2.0": "Similar to MIT but includes patent protection.",
        "GNU General Public License (GPL v3)": "Strong copyleft, modifications must remain open-source.",
        "GNU Lesser General Public License (LGPL v3)": "Weak copyleft, allows use in proprietary software.",
        "Mozilla Public License 2.0 (MPL 2.0)": "Hybrid license, modified files must stay open-source.",
        "Creative Commons Licenses": "For non-code assets like documentation (e.g., CC0, CC BY).",
        "Unlicense": "Public domain dedication, no restrictions."
    }
    
    license_choices = [] 
    
    for name, desc in licenses.items():
        license_choices.append({
                "name": f"{name} - {desc}",  
                "value": name # this will store just the name as the actual value when selected            
            })


    license_answer = prompt([
        {
            "type": "list",
            "name": "license",
            "message": "Choose a license for your project:",
            "choices": license_choices
        }
    ])

    # answers = prompt(project_info)
    license_name = license_answer["license"]
    license_desc = licenses[license_name]

    #select_folder()
    
    # Use the easygui version
    # file_path = select_folder_easygui() 

    # if file_path is None:
    #     console.print("[yellow]Folder selection cancelled. README.md will not be created.[/yellow]")
    #     return 
    
    # file_path = os.path.join(file_path, "README.md")

    # Output tp README.md file
    readme_content = f"""# {title}

    ## Descriptiony

    {description}

    ## Installation

    {installation}

    ## Usage
    {usage}

    ## License
    **{license_name}**

    {license_desc}

    ## Author
    {author}

    ## Contact
    For questions, contact [email]({email}).
    """
    file_path = "README.md"
    with open( file_path , "w", encoding="utf-8") as f:
        f.write(readme_content)

    console.print("\n✅ [bold green]README.md has been created successfully![/bold green]")

######d
    console.print("\n[bold underline green]✅ Summary Preview[/bold underline green]") #############
######    
    console.print(f"[bold]Title:[/bold] {title}")
    console.print(f"[bold]Description:[/bold] {description}")
    console.print(f"[bold]Installation:[/bold] {installation}")
    console.print(f"[bold]Usage:[/bold] {usage}")
    console.print(f"[bold]License:[/bold] {license_name} - {license_desc}")
    console.print(f"[bold]Author:[/bold] {author}")
    console.print(f"[bold]Contact:[/bold] {email}")
    
if __name__ == "__main__":
    collect_project_info()

# def select_folder():

#     root = tk.Tk() # Create a Tkinter root window
#     root.withdraw() # hide it as we only need the file dialog

#     folder_path = filedialog.askdirectory(
#         title="Select a Folder",
#         initialdir=os.getcwd()  # Set the initial directory
#     )
#     return folder_path

    # project_info = [
    #     {"type": "input", "name": "title", "message": "What is the title of your project?"},
    #     {"type": "input", "name": "description", "message": "Provide a brief description of your project:"},
    #     {"type": "input", "name": "installation", "message": "Insallation instructions:"},
    #     {"type": "input", "name": "usage", "message": "How will your project be used?"},
    #     {
    #         "type": "list",
    #         "name": "license",
    #         "message": "What type of license does your project use?",
    #         "choices": license_choices # list(licenses.keys())
    #     },
    #     {"type": "input", "name": "author", "message": "Who is the author of this project?"},
    #     {"type": "input", "name": "contact_info", "message": "What is your email address?"}
    # ]    

        # title = inquirer.text(
    #     message="Enter project title:",
    #     validate=EmptyInputValidator()
    # ).execute()

        # license_answer = dv.rich_prompt([
    #     {
    #         "type": "list",
    #         "name": "license",
    #         "message": "Choose a license for your project:",
    #         "choices": license_choices
    #     }
    # ])
    # Hide the root window
    # root = tk.Tk()
    # root.withdraw()

    # folder_path = filedialog.askdirectory(title="Select Folder to Create README.md")

    # if folder_path:  # If user selects a folder
    #     readme_path = os.path.join(folder_path, "README.md")
    #     with open(readme_path, "w") as f:
    #         f.write("# Project Title\n\nA short description of your project.")
    #     print(f"README.md created at: {readme_path}")
    # else:
    #     print("No folder selected.")