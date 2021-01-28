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


## Despliegue en PythonAnywhere (PyAw)
Me basaré en la guía [oficial de despliegue de Flask en PyAw](https://help.pythonanywhere.com/pages/Flask/) para esta receta:

1. Registrate en PyAw y crea un proyecto web
2. Sigue el paso a paso para crear una app de Flask usando python3
3. Las pestañas mas comúnes en su plataforma serán Consoles y Web
```
En Web encontrarás la mayoría de información de tu aplicación web
En Consoles tendrás acceso a las consolas de Bash y MySQL. En la versión gratuita solo puedes tener 2 consolas abiertas al tiempo.
```
4. Cónectate en la consola de PyAw y ve a la dirección de tu proyecto. Seguramente será algo como /home/<NOMBRE_USUARIO>/mysite (esta información aparece en la pestaña Web)
5. Reemplaza el archivo app.py por tu proyecto. Sugiero aquí hacer un git clone de tu repositorio.
6. Crea un ambiente virtual y actívalo.
7. Instala tus paquetes de python adentro del ambiente virtual. Copia la ruta de tu virtualenv porque la necesitarás en el siguiente paso. Debe ser una ruta como:
```
/home/<NOMBRE_USUARIO>/mysite/venv
```
8. En la pestaña Web, ve a virtualenv y agrega la ruta del paso 7.

9. En Web aparece la ruta a tu archivo wsgi.py. Cambia la siguiente línea para que tenga sentido con tu proyecto:
```
from proyecto import app as application  # noqa
```
10. Nuevamente en la consola de tu proyecto, asegurate que se cree la base de datos sqlite. Puedes correr `python proyecto.py` y una vez generada, detenerla.
11. Ve a web Recarga tu proyecto. El botón verde que dice reload.

Recuerda que en PyAw no sirve usar `app.run()` de Flask. El servidor web se encargará de correr tu proyecto. Por ello se usa el pequeño hack especificado en la guía:
```
if __name__ == '__main__':
    if 'liveconsole' not in gethostname():
        app.run()
```
## TODO
- Implementar una vista para actualizar estudiantes
- Implementar una vista para borrar estudiantes
- Mejorar el CSS
- En una rama apare mostrar el mismo proceso con SQLAlchemy
- Usar la base de datos MySQL de PyAw
