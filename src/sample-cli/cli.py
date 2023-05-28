
import click


@click.group()
def cli():
    """My simple command line tool."""

@click.command("fizzbuzz", short_help='exec fizz buzz program.')
@click.option("--input-number",
             required=False,
             type=int,
             default=None,
             help="target number to exec fizzbuzz.")
def fizz_buzz(input_number):

    if input_number == None:
        input_number = click.prompt('Please enter a valid integer', type=int)
    
    # clickのエラー出力を試すためここでは０は入力対象外とする
    if input_number == 0:
        err_msg = "0は入力対象外です。"
        raise click.BadParameter(err_msg)

    if input_number % 3 == 0 and input_number % 5 == 0:
        click.echo(click.style("FizzBuzz", fg="green", bg="yellow"))
        return

    if input_number % 3 == 0:
        click.echo(click.style("Fizz", fg="blue"))
        return
    
    if input_number % 5 == 0:
        click.echo(click.style("Buzz", fg="blue"))
        return
    
    click.echo("Not fizz and buzz.", err= True)



if __name__ == "__main__":
    cli.add_command(fizz_buzz)
    cli()
