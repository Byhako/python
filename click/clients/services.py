import csv
import os
import click
from clients.models import ClientModel

class ClientService:
    def __init__(self, table_name):
        self.table_name = table_name


    def createClient(self, client):
        with open(self.table_name, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=ClientModel.schema())
            writer.writerow(client.to_dict())


    def list_clients(self):
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=ClientModel.schema())
            return list(reader)


    def update_client(self, updated_client):
        # obtenemos lista de clientes
        clients = self.list_clients()
        updated_clients = []

        for client in clients:
            # agregamos cliente actualizado
            if client['uid'] == updated_client.uid:
                updated_clients.append(updated_client.to_dict())
            else:
                # los demas clientes se agregan iguales
                updated_clients.append(client)
        
        # guardamos en disco
        self._save_to_disk(updated_clients)


    def delete_client(self, client_uid):
        clients_list = self.list_clients()
        clients = [client for client in clients_list if client['uid'] != client_uid]
        self._save_to_disk(clients)

        if len(clients_list) != len(clients):
            click.echo('Cliente deleted')
        else:
            click.echo('Client not found')


    def _save_to_disk(self, clients):
        # creamos tabla temporal
        tmp_table = self.table_name + '.tmp'
        with open(tmp_table, mode='w') as f:
            writer = csv.DictWriter(f, fieldnames=ClientModel.schema())
            writer.writerows(clients)

        # borramos tabla original
        os.remove(self.table_name)
        # renombramos nueva tabla
        os.rename(tmp_table, self.table_name)
