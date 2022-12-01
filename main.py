from rich.console import Console
from rich.table import Table
from CreatePolicy import CreatePolicy
from seekRule import seekRule
from show import ShowRules
from delPolicy import delPolicy
while 1==1:
    console = Console()

    console.print("""
                ,-._
              _.-'  '--.
            .'      _  -`\_
            / .----.`_.'----'
            ;/     `
    dfw   /_;

        ._      ._      ._
    _.-._)`\_.-._)`\_.-._)`\_.-._
    """, style="blue")
    table = Table(title="Dolphin Firewall")

    table.add_column("Key", justify="right", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")

    table.add_row("1", "Create Policy")
    table.add_row("2", "Delete Policy")
    table.add_row("3", "Show Rules")
    table.add_row("4", "EXIT", style="red")

    console.print(table)

    respond=input()
    if respond == '1':
        CreatePolicy()
    elif respond == '2':
        delPolicy()
    elif respond == '3':
        ShowRules()
    elif respond == '4':
        console.print('\nEXIT\n', style="red")
        break
    else:
        print('wrong number')

