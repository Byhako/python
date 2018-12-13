import click
from clients.services import ClientService
from clients.models import ClientModel

@click.group()
def clients():
    """Manages of clients lifecycle"""
    pass


@clients.command()
@click.option('-n', '--name', type=str, prompt=True, help='The client name.')
@click.option('-c', '--company', type=str, prompt=True, help='The client company.')
@click.option('-e', '--email', type=str, prompt=True, help='The client email.')
@click.option('-p', '--position', type=str, prompt=True, help='The client position.')
@click.pass_context
def create(cxt, name, company, email, position):
    """Creates a new client"""
    client = ClientModel(name, company, email, position)

    client_service = ClientService(cxt.obj['client_table'])
    client_service.createClient(client)


@clients.command()
@click.pass_context
def list_clients(cxt):
    """List old clients"""
    client_service = ClientService(cxt.obj['client_table'])
    client_list = client_service.list_clients()

    if client_list:
        click.echo('\n  NAME  |  COMPANY  |  EMAIL  | POSITION  |  ID')
        click.echo('*'*100)

        for client in client_list:
            click.echo('  {name} | {company} | {email} | {position}  |  {uid}'.format(
                name=client['name'],
                company=client['company'],
                email=client['email'],
                position=client['position'],
                uid=client['uid'] ))


@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def update(cxt, client_uid):
    """Updates to client"""
    client_service = ClientService(cxt.obj['client_table'])
    client_list = client_service.list_clients()
    client = [client for client in  client_list if client['uid'] == client_uid]

    if client:
        client = _update_client_flow(ClientModel(**client[0]))
        client_service.update_client(client)

        click.echo('Client updated.')
    else:
        click.echo('Client not found.')


def _update_client_flow(client):
    click.echo('Leave empty if you dont want to modify the value.')

    client.name = click.prompt('New name: ', type=str, default='client.name')
    client.company = click.prompt('New company: ', type=str, default='client.company')
    client.email = click.prompt('New email: ', type=str, default='client.email')
    client.position = click.prompt('New position: ', type=str, default='client.position')

    return client


@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def delete(ctx, client_uid):
    """Deletes a client"""
    client_service = ClientService(ctx.obj['client_table'])

    if click.confirm('Are you sure you want to delete the client with uid: {}'.format(client_uid)):
        client_service.delete_client(client_uid)
    
all = clients
