from flask import render_template, Blueprint

from models.estudiante import Estudiante

perfil = Blueprint('perfil', __name__)


@perfil.route('/perfil/<nombre_usuario>/')
def detail(nombre_usuario):
    estudiante = Estudiante.get(
        nombre_usuario=nombre_usuario
    )
    return render_template('detail.html', persona=estudiante)
