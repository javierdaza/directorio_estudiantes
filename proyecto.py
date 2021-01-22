from flask import Flask
from decouple import config

from models.estudiante import Estudiante, database_proxy
from views.home import home
from views.detail import perfil
from views.crear import crear
from views.guardar import guardar
from views.cargar import cargar

app = Flask(__name__)
app.secret_key = config('SECRET_KEY')
app.register_blueprint(home)
app.register_blueprint(perfil)
app.register_blueprint(crear)
app.register_blueprint(guardar)
app.register_blueprint(cargar)


def main():
    database_proxy.create_tables([Estudiante], safe=True)
    app.run(debug=True, host='0.0.0.0', port=8000)


if __name__ == '__main__':
    main()
