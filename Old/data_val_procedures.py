# As it's a learning exercise have kept these in a normal module (i.e. not a class)
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt


console = Console()

def rich_prompt(message, color="cyan", validator=None): # uses error handler to 
    while True:
        try:
            prompt_text = Text(message, style=color)
            value = Prompt.ask(prompt_text)
            if validator:
                return validator(value)
            return value
        except ValueError as e: # catch only ValueError type errors
            console.print(f"[red]❌ {e}[/red]")

def validate_not_empty(value):
    if not value.strip():
        raise ValueError("Input cannot be empty1.") # raise = Throw
    return value

def validate_email(value):
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

