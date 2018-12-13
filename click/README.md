# Aplicación básica usando "click"

+ Creamos entorno virtual.

```
:~$ conda create -n nombredeentorno
:~$ source activate nombredeentorno
:~$ source deactivate
:~$ conda info —envs
:~$ conda remove —name nombredeentorno —all
```

### Para instalar la aplicación:

Estos comandos corren el archivo setup.py

```
pip install --editable .
```

Corremos la aplicación.

```
pv clients --help
pv clients create
```

## Decoradores principales de click.

@click.group
  agrupar comandos
@click.command
  definimos todos los comandos de nuestra aplicacion
@click.argument
  parametros necesarios
@click.option
  parametros opcionales
