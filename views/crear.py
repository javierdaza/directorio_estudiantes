from flask import render_template, Blueprint

from models.estudiante import Estudiante

crear = Blueprint('crear', __name__)


@crear.route('/crear')
def crear_page():
    return render_template('crear.html')
