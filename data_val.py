from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt


class DataValidator:
    def __init__(self):
        self.console = Console()

    def rich_prompt(self, message: str, color: str = "cyan", validator=None):

        while True:
            try:
                prompt_text = Text(message, style=color)
                value = Prompt.ask(prompt_text)
                if validator:
                    return validator(value)
                return value
            except ValueError as e: # catch only ValueError type errors
                self.console.print(f"[red]❌ {e}[/red]")

    @staticmethod  #  States that this is a static method i.e. belongs to the class but does not receive the instance (self) or the class (cls) as its first argument
    def validate_not_empty(value: str) -> str: 
        if not value.strip():
            raise ValueError("Input cannot be empty1.") # raise = Throw
        return value
    
    @staticmethod 
    def validate_email(value: str) -> str:
        value = value.strip()
        if "@" not in value or "." not in value.split("@")[-1]:
            raise ValueError("Please enter a valid email address.")
        return value




# Alternative email validation using the 're' (Regular Expressions) library
# import re
# def validate_email(value):
#     pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
#     if not re.match(pattern, value):
#         raise ValueError("Please enter a valid email address.")
#     return value

