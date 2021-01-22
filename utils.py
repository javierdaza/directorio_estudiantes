from peewee import IntegrityError

from models.estudiante import Estudiante, db


lista_estudiantes = [
    {
        'nombre_usuario': 'juanibañez',
        'puntaje': 14717,
        'numero_telefono': '35555555',
        'email': 'jibanez@example.com',
        'foto': 'https://avatars2.githubusercontent.com/u/61925347?s=460&u=bfe92ef1424d77d84b230910bc9699bcdb0ddaf1&v=4',
        'motivacion': 'Fortalecer mis habilidades de python. Practicar para las entrevistas de trabajo.'
    },
    {
        'nombre_usuario': 'sergiomolinares',
        'puntaje': 11912,
        'numero_telefono': '3015678932',
        'email': 'sergiom@example.com',
        'foto': 'https://avatars1.githubusercontent.com/u/39917505?s=460&u=cf9747baf386ab0215a78dd242c51ac64bdc8513&v=4',
        'motivacion': 'Fortalecer mis habilidades en programacion para hacer mejores scripts.'
    },
    {
        'nombre_usuario': 'miguequintero',
        'puntaje': 7363,
        'numero_telefono': '3003246711',
        'email': 'mqintero@example.com',
        'foto': 'https://avatars0.githubusercontent.com/u/50154791?s=460&v=4',
        'motivacion': 'Cambiar de carrera. Entrar a una empreasa como cientifico de datos.'
    },
    {
        'nombre_usuario': 'aliexerm',
        'puntaje': 4079,
        'numero_telefono': '3114569037',
        'email': 'aliexer@example.com',
        'foto': 'https://avatars1.githubusercontent.com/u/33433883?s=460&u=fe36215fb263f93d3b487b6e99061f0a8479249b&v=4',
        'motivacion': 'Conseguir empleo como desarrollador de aplicaciones web con python.'
    },
    {
        'nombre_usuario': 'carlosh',
        'puntaje': 4888,
        'numero_telefono': '310567345',
        'email': 'carlosh@example.com',
        'foto': 'https://avatars3.githubusercontent.com/u/74746285?s=460&v=4',
        'motivacion': 'Quiero ser siempre el mejor, mejor que naadie mas.'
    },
]


def agregar_lista_estudiantes():
    mensaje = ''

    for estudiante in lista_estudiantes:
        try:
            Estudiante.create(
                nombre_usuario=estudiante['nombre_usuario'],
                puntaje=estudiante['puntaje'],
                numero_telefono=estudiante['numero_telefono'],
                email=estudiante['email'],
                foto=estudiante['foto'],
                motivacion=estudiante['motivacion']
            )
            mensaje = 'Los estudiantes fueron guardados exitosamente'
        except IntegrityError:
            # El estudiante ya existe
            mensaje = 'El listado de estudiantes ya fue guardado anteriormente'

    return mensaje
