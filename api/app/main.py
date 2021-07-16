import os.path
import pkgutil

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

# Encargados de importar automaticamente los controllers para asignar los routers
# no borrar el import * desde el controller
from app.controller import *
from app import controller
from app.constants.main_constants import MainConstants


def import_routers(app):
    path_package = os.path.dirname(controller.__file__)
    files = [name for _, name, _ in pkgutil.iter_modules([path_package])]
    for file in files:
        instance = getattr(controller, file)
        if hasattr(instance, 'router'):
            app.include_router(instance.router)


def add_app_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"]
    )


class Main:

    def __init__(self):
        pass

    def start_app(self):
        version = os.getenv("version", "1.0.0")
        app = FastAPI(title=MainConstants.MAIN['title'],
                      description=MainConstants.MAIN['description'],
                      version=version,
                      )
        add_app_cors(app)
        import_routers(app)
        return app


app = Main().start_app()
