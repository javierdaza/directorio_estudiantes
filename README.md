----------------------
# Directorio Estudiantes
----------------------
Este es un proyecto sencillo que muestra el uso Flask y el ORM llamado PeeWee.  La idea del proyecto es poder crear y listar estudiantes del [curso de Python básico nivel 4](https://javierdaza.co/cursos/laboratorio-aplicaciones-python/).


Variables de entorno en **.env**
```
SECRET_KEY=muchoscaracteresaleatorios
DATABASE_URL=app.db
PRODUCTION=False
```


## Instalación local

- Crear archivo .env
- Configura la variable `PRODUCTION` dependiendo del ambiente
- git clone
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- python proyecto.py


## Despliegue en Heroku

1. Crear cuenta en Heroku y dale un nombre
2. Descargar el [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) (Command Line Interface)
3. Crear la app en Heroku (dashboard)
4. Conectarte a github y seleccionar el repositorio (dashboard)
5. Añadir el add-on de Heroku-postgress en categoria hobby-dev Free
6. En settings, configurar variables de entorno `SECRET_KEY` y `PRODUCTION`
7. Abrir la consola y correr:
```
heroku login
heroku run bash --app <NOMBRE_DE_TU_APP_DE_HEROKU>
```
8. Correr python proyecto.py y luego de que funcione, detenerlo
9. En la consola local correr:
```
heroku pg:info --app <NOMBRE_DE_TU_APP_DE_HEROKU>
```
El comando debería mostrarte cuantas tablas (1) y el número de filas (5)
10. Usa psql para conectarte a la BD y hacer un query a las tablas
```
heroku pg:psql --app <NOMBRE_DE_TU_APP_DE_HEROKU>
```
11. Conectate a la URL de tu app. Debería ser:
```
https:://<NOMBRE_DE_TU_APP_DE_HEROKU>.herokuapp.com
```
12. Puedes ver los logs desde el dashboard en more > view logs o correr:
```
heroku logs --tail --app <NOMBRE_DE_TU_APP_DE_HEROKU>
```


## TODO
- Implementar una vista para actualizar estudiantes
- Implementar una vista para borrar estudiantes
- Mejorar el CSS
