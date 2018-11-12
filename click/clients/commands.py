import click

@click.group()
def clients():
    """Manages of clients lifecycle"""
    pass


@clients.command()
@click.pass_context
def create(cxt, name, company, email, position):
    """creates a new client"""
    pass


@clients.command()
@click.pass_context
def list(cxt):
    """List old clients"""
    pass


@clients.command()
@click.pass_context
def update(cxt, client_uid):
    """updates to client"""
    pass


@clients.command()
@click.pass_context
def delete(cxt, client_uid):
    """delete to client"""
    pass
    
all = clients
