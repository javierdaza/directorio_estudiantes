from flask import render_template, Blueprint

from utils import agregar_lista_estudiantes

cargar = Blueprint('cargar', __name__)


@cargar.route('/cargar')
def cargar_estudiantes():
    mensaje = agregar_lista_estudiantes()
    return render_template('carga.html', datos=mensaje)