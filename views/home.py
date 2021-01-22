from flask import render_template, Blueprint

from models.estudiante import Estudiante

home = Blueprint('home', __name__)


@home.route('/')
def home_page():
    estudiantes = Estudiante.select().order_by(
        Estudiante.puntaje.desc()
    )
    return render_template('index.html', datos=estudiantes)
