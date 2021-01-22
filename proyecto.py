from flask import Flask

from models.estudiante import Estudiante, db
from views.home import home
from views.detail import perfil
from views.crear import crear
from views.guardar import guardar
from views.cargar import cargar

app = Flask(__name__)
app.secret_key = '12345'
app.register_blueprint(home)
app.register_blueprint(perfil)
app.register_blueprint(crear)
app.register_blueprint(guardar)
app.register_blueprint(cargar)


def main():
    db.create_tables([Estudiante], safe=True)
    app.run(debug=True, host='0.0.0.0', port=8000)


if __name__ == '__main__':
    main()
