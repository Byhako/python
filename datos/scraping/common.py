import yaml

__config = None

def config():
    global __config
    if not __config:
        with open('config.yaml', mode='r') as f:
            __config = yaml.load(f)
            
    return __config

"""
si no hay configuración, se carga el archivo, si ya esta cargado,
no lo vuelve a hacer.
"""