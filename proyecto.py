from socket import gethostname

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


@app.before_request
def _db_connect():
    database_proxy.connect()


@app.teardown_request
def _db_close(exc):
    if not database_proxy.is_closed():
        database_proxy.close()


if __name__ == '__main__':
    database_proxy.connect()
    database_proxy.create_tables([Estudiante], safe=True)
    if 'liveconsole' not in gethostname():
        app.run(debug=True)
