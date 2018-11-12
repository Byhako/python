import click
from clients import commands as client_commands

@click.group()
@click.pass_context
def cli(cxt):
    cxt.obj = {}
    
cli.add_command(client_commands.all)
