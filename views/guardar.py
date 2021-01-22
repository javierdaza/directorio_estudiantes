from peewee import IntegrityError
from flask import (render_template, redirect, Blueprint,
                   url_for, request, flash)

from models.estudiante import Estudiante

guardar = Blueprint('guardar', __name__)


@guardar.route('/guardar', methods=['POST'])
def guardar_estudiante():
    if request.method == 'POST':
        try:
            nombre_usuario= request.form.get(
                'nombre_usuario'
            ).strip().replace(' ','').lower()
            estudiante = Estudiante.create(
                nombre_usuario=nombre_usuario,
                puntaje=1,
                numero_telefono=request.form.get('numero_telefono'),
                email=request.form.get('email'),
                foto=request.form.get('foto'),
                motivacion=request.form.get('motivacion')
            )
        except IntegrityError as err:
            print(":::::: Error en el backend: ", err)
            flash('Error: Este usuario ya esta en uso.')
        else:
            flash('Estudiante creado satisfactoriamente.')
            return redirect(
                url_for('perfil.detail', nombre_usuario=estudiante.nombre_usuario)
            )

    return redirect(url_for('home.home_page'))