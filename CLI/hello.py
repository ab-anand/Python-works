import click

@click.command()
@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
@click.option('--name', '-n', multiple=True, default='', help='Who are you?')
@click.password_option()
def cli(verbose,name, password):
    """This is an example script to learn Click."""
    if verbose:
        click.echo("We are in the verbose mode.")
    click.echo("Hello World")
    for n in name:
        click.echo('Bye {0}'.format(n))
    click.echo('We received {0} as password.'.format(password))

