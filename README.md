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


## TODO
- Implementar una vista para actualizar estudiantes
- Implementar una vista para borrar estudiantes
- Mejorar el CSS
