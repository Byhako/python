# Crear entorno

conda create --name pandas_tuto

También puedes especificar la versión de python a utilizar

conda create --name pandas_tuto python=x.x

# Activar entorno

conda activate pandas_tuto

# Desactivar entorno

conda deactivate

# Ver info del entorno virtual

conda info

# Ver todos los ambientes virtuales

conda info --envs

# Instalar paquetes usando conda

conda install pandas

# Actualizar una especifica libreria

conda update pandas

# Actualizar todas las librerías ambiente virtual

conda update --all

# Eliminar ambiente virtual

conda remove --name pandas_tuto --all

# Requerimientos

conda install --file requirements.txt.