
import click

from .fizzbuzz import fizz_buzz
from .sample_commands import input_your_params,edit_your_config_file


@click.group()
def cli():
    """My simple command line tool."""

def main():
    cli.add_command(fizz_buzz)
    cli.add_command(input_your_params)
    cli.add_command(edit_your_config_file)
    cli()

if __name__ == "__main__":
    main()
