from flask import Blueprint

from project.exceptions import DataStorageError

error_handler = Blueprint("error_handler", __name__)


@error_handler.app_errorhandler(DataStorageError)
def error_data_storage(error):
    return f"Не удается получить данные: {error.get_explanation()} {error}", 500


@error_handler.app_errorhandler(404)
def bar(error):
    return "Не нашлось", 404


@error_handler.app_errorhandler(418)
def bar(error):
    return "418 I'm a teapot", 418

