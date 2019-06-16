# CRUD Usuarios

## Características

- Autenticación
- Vistas protegidas
- Lista, Crea, Actualiza y Borra Usuarios
- Cada usuario creado puede autenticarse
- Los usuarios solo pueden modificar sus propios perfiles
- Administradores pueden pueden crear, modificar y eliminar todos los perfiles
- Paginación cada 5 elementos

## Puesta en marcha

```shell
$ git clone https://github.com/wilfredinni/CRUD_users.git

$ cd CRUD_users
$ python -m virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt

$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

Login con las credenciales del super usuario.