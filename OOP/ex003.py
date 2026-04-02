# Biblioteca Rich

from rich import print
from rich.panel import Panel
from rich.table import Table
from rich import inspect
from rich.traceback import install

install()

# Exemple of print with Rich
print("Hello, [red]World![/red] :earth_americas:")
print("Hello, [#ff79c6]tech women![/#ff79c6] :heart:")

# Exemple of panel with Rich
box = Panel("[white]This is a exemple of panel[/white] :+1:", title="Message", style="bold magenta")
print(box)

# Exemple of table with Rich
table = Table(title="Tech Women")
table.add_column("Name", style="cyan", no_wrap=True)
table.add_column("Role", style="magenta")
table.add_row("Luci Rosa", "Mathematician")
table.add_row("Vini Henrique", "Computer Scientist")
print(table)

inspect(int)

# Exemple of error handling with Rich
def division(x, y):
    return x / y
print(division(10, 0))