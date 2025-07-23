from InquirerPy import prompt
from rich.console import Console
from rich.panel import Panel
import questionary
import os
from datetime import datetime

# Modules
# import data_val as dv
from data_val import DataValidator

# console = Console() move to the constructor

class ReadmeGenerator:
    def __init__(self):
        self.console = Console()
        self.dv = DataValidator() #  Create an instance of DataValidator
        self.licenses = {
            "MIT License": "Permissive, allows modification and distribution with attribution.",
            "Apache License 2.0": "Similar to MIT but includes patent protection.",
            "GNU General Public License (GPL v3)": "Strong copyleft, modifications must remain open-source.",
            "GNU Lesser General Public License (LGPL v3)": "Weak copyleft, allows use in proprietary software.",
            "Mozilla Public License 2.0 (MPL 2.0)": "Hybrid license, modified files must stay open-source.",
            "Creative Commons Licenses": "For non-code assets like documentation (e.g., CC0, CC BY).",
            "Unlicense": "Public domain dedication, no restrictions."
        }

    def create_license_choices(self):
        return [
            {"name": f"{name} - {desc}", "value": name}
            for name, desc in self.licenses.items()
        ]
    
    def confirm_continue(self):
        return questionary.confirm(
            "Continue?", 
            default=None, 
            auto_enter=True
        ).ask()
         
    def write_readme_file(self, file_path, title, description, installation, usage, license_name, license_desc, author, email):

        # Create the README content
        new_readme_content = f"""# {title}
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
        Contact email: {email}.
        """


        existing_content = ""
        file_existed = False
        content_was_present = False

        if os.path.exists(file_path): # check if file already exists
            file_existed = True
            with open(file_path, "r", encoding="utf-8") as f:
                existing_content = f.read()
            
            if existing_content.strip(): # Check if file contains text
                content_was_present = True
                self.console.print(f"[yellow]'{file_path}' already exists and contains content.[/yellow]")
            else:
                self.console.print(f"[yellow]'{file_path}' exists but is empty.[/yellow]")
        else:
            self.console.print(f"[green]Creating new file: '{file_path}'.[/green]")

        final_content = new_readme_content + ("\n\n" + existing_content if content_was_present else "")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(final_content)

        if file_existed and content_was_present:
            self.console.print(f"\n✅ [bold green]'{file_path}' has been updated. The existing text was kept, and new details were prepended to the top.[/bold green]")
        else:
            self.console.print(f"\n✅ [bold green]'{file_path}' has been created successfully![/bold green]")

    def collect_project_info(self):

        self.console.print(Panel("[bold yellow]README.md File Generator[/bold yellow]", expand=False))

        if not self.confirm_continue():
            self.console.print("[yellow]README.md File Generator cancelled.[/yellow]")
            return None

        title = self.dv.rich_prompt("What is the title of your project?", color="cyan", validator=DataValidator.validate_not_empty)
        description = self.dv.rich_prompt("Provide a brief description", color="yellow")
        installation = self.dv.rich_prompt("Installation instructions", color="cyan")
        usage = self.dv.rich_prompt("How will your project be used", color="yellow")
        author = self.dv.rich_prompt("Who is the author of this project", color="cyan")
        email = self.dv.rich_prompt("What is your email address", color="yellow", validator=DataValidator.validate_email)

        # OLD: title = dv.rich_prompt("What is the title of your project?", color="cyan", validator=dv.validate_not_empty)

        license_answer = prompt([
            {
                "type": "list",
                "name": "license",
                "message": "Choose a license for your project:",
                "choices": self.create_license_choices()
            }
        ])
        
        license_name = license_answer["license"]
        license_desc = self.licenses[license_name]

        now = datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M")

        file_path = f"README_{timestamp}.md"
        
        self.write_readme_file(file_path, title, description, installation, usage, license_name, license_desc, author, email)

def main():
    generator = ReadmeGenerator()
    generator.collect_project_info()

if __name__ == "__main__":
    main()
