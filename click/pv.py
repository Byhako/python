import click
from clients import commands as client_commands

CLIENTS_TABLE = '.clients.csv'

@click.group()
@click.pass_context
def cli(cxt):
    cxt.obj = {}
    cxt.obj['client_table'] = CLIENTS_TABLE


cli.add_command(client_commands.all)
