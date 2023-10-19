#Como crear un paquete distribuible
# -> setuptools (paquete que ya esta creado en python )
from setuptools import setup

setup(
    name= "Paquete Distribuible" ,
    version= "1.0", 
    description= "Este paquete es de prueba de como crear un paquete distribuible",
    author= "Martin Navarro",
    author_email= "martinnavarro1503@gmail.com",
    packages=["paquete"] #todas las carpetas que va a contener el paquete   
)

#EN LA TERMINAL
# -> sdist le dice a python que quiero crear un paquete distribuible
# python .\setup.py sdist
# -> Crea 2 carpetas (dist y nombre_archivo.egg-info).
# -> De la carpeta dist el archivo (Paquete Distribuible-1.0.tar.gz) lo puedo compartir con los clientes, 
# -> para que lo puedan instalar en sus equipos, con los siguientes comandos.
# cd dist
# dir
# pip install '.\Paquete Distribuible-1.0.tar.gz'
# pip list (para ver si esta instalado)
# pip uninstall '.\Paquete Distribuible-1.0.tar.gz' (para desinstalarlo)