
from InquirerPy import prompt
from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
import data_val as dv

console = Console()

def collect_project_info():
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

    console.print(Panel("[bold yellow]README.md File Generator[/bold yellow]", expand=False))
    
    title = dv.rich_prompt("What is the title of your project?", color="cyan", validator=dv.validate_not_empty)

    # title = Prompt.ask("[cyan]What is the title of your project?[/cyan]")
    description = dv.rich_prompt("Provide a brief description", color="yellow")
    installation = dv.rich_prompt("Installation instructions", color="cyan")
    
    usage = dv.rich_prompt("How will your project be used", color="yellow")
    author = dv.rich_prompt("Who is the author of this project", color="cyan")
    email = dv.rich_prompt("What is your email address", color="yellow", validator=dv.validate_email)

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

######
    console.print("\n[bold underline green]✅ Summary Preview[/bold underline green]") #############
######    
    console.print(f"[bold]Title:[/bold] {title}")
    console.print(f"[bold]Description:[/bold] {description}")
    console.print(f"[bold]Installation:[/bold] {installation}")
    console.print(f"[bold]Usage:[/bold] {usage}")
    console.print(f"[bold]License:[/bold] {license_name} - {license_desc}")
    console.print(f"[bold]Author:[/bold] {author}")
    console.print(f"[bold]Contact:[/bold] {email}")

    # Output tp README.md file
    readme_content = f"""# {title}

    ## Description
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

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    console.print("\n✅ [bold green]README.md has been created successfully![/bold green]")

    
if __name__ == "__main__":
    collect_project_info()


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
