# Projecto final para informatorio 2020
En esten projecto vamos a crear una pagina wweb para un sistema de adopcion de mascotas.

## Configuracion 
Para el projecto utilizaremos el framework Django 3.1.6, con la siguiente estructura: 
* Repositorio
  * infoFinal
  * Template
  * Apps
  * Static
  * Media
  * manage.py
  * my.cnf
  
Dentro del repositorio cada participante tiene que tener un archivo my.cnf con su conexion a la base de datos y tener las librerias de requerimeintos que se espicifican.

## Database
La database que usamos es mysql y el archivo de configuracion tiene que tener este formato. 
```
[client]
database = #nombre de la database
user = #nombre de usuario
password = #contrasenia 
default-character-set = utf8
```
## Email
Para configurar el email tiene que cambiar en el archivo settings los datos con el email de prueba que quieran.