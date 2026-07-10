# Flask Task Manager

Aplicacion web para gestionar tareas personales, desarrollada con Flask y Tailwind CSS 3.

## Captura de la aplicacion

<!-- Agrega tu captura aqui -->
![App Screenshot](docs/screenshot.png)

## Funcionalidades

- Registro e inicio de sesion de usuarios
- Crear, editar y eliminar notas
- Cada usuario solo ve sus propias notas
- Validacion de formularios con WTForms
- Diseno responsive con Tailwind CSS 3
- Animaciones en la interfaz

## Stack tecnologico

- **Backend:** Flask 3, Flask-SQLAlchemy, Flask-WTF
- **Frontend:** Tailwind CSS 3 (CDN), Jinja2
- **Base de datos:** SQLite
- **Gestion de dependencias:** Poetry
- **Produccion:** Gunicorn, Docker

## Requisitos

- Python 3.12 o superior
- [Poetry](https://python-poetry.org/docs/#installation)
- Docker (opcional, para despliegue)

## Instalacion

1. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/flask-task-manager.git
cd flask-task-manager
```

2. Instalar dependencias:

```bash
poetry install
```

3. Arrancar el servidor de desarrollo:

```bash
poetry run flask run
```

La app estara disponible en `http://127.0.0.1:5000`

## Docker

1. Construir la imagen:

```bash
docker build -t task-flask .
```

2. Ejecutar el contenedor:

```bash
docker run -d -rm -p 8000:8000 --name task-app task-flask
```

La app estara disponible en `http://localhost:8000`

## Estructura del proyecto

```
flask-task-manager/
├── app/
│   ├── __init__.py        # Factory create_app()
│   ├── config.py          # Configuracion
│   ├── forms.py           # Formularios WTForms
│   ├── models.py          # Modelos SQLAlchemy
│   ├── notes/
│   │   ├── __init__.py
│   │   └── routes.py      # Rutas de notas
│   ├── users/
│   │   ├── __init__.py
│   │   └── routes.py      # Rutas de usuarios
│   ├── templates/         # Templates Jinja2
│   └── static/            # Archivos estaticos
├── wsgi.py                # Entry point para produccion
├── dockerfile
├── pyproject.toml
└── poetry.lock
```

## Licencia

MIT
