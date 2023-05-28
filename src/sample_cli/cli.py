
import click

from .fizzbuzz import fizz_buzz


@click.group()
def cli():
    """My simple command line tool."""

def main():
    cli.add_command(fizz_buzz)
    cli()

if __name__ == "__main__":
    main()
