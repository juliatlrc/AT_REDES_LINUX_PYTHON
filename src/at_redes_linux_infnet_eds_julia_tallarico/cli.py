"""Console script for at_redes_linux_infnet_eds_julia_tallarico."""
import at_redes_linux_infnet_eds_julia_tallarico

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for at_redes_linux_infnet_eds_julia_tallarico."""
    console.print("Replace this message by putting your code into "
               "at_redes_linux_infnet_eds_julia_tallarico.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
