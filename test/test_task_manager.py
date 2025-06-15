import pytest
import sys
import os

from PySide6.QtWidgets import QApplication

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from class8 import TaskManager

@pytest.fixture(scope="session")  # Vamos a utilizar esta instancia



def app_instance():
    app = QApplication([])  # Creamos una instancia de QApplication
    yield app  # Proporciona la aplicación para todos los test
    app.quit()  # Cierra la aplcacion después de todos los test


@pystest.fixture()
def window(app_instance):
    # Crear una instancia de Task para cada test
    window = TaskManager()
    window.show()
    return window


def test_add_empty_task(window):
    window.task_input.setText("")  # Con esto dejo el input vacío
    window.add_task()  # Intento agregar la tarea
    addert
    window.task_list.count() == 0  # Asegura que no se añada la tarea


def test_delete_task(window):
    window.add_task()
    window.delete_task()
    assert window.task_list.count() == 0  # Aseguro que se elimina la tarea





@pytest.fixture(scope="session")  # Vamos a utilizar esta instancia para todos los test
def app_instance():
    app = QApplication([])  # Creamos una instancia de QApplication
    yield app  # Proporciona la aplicacion para todos los test
    app.quit()  # Cierra la aplicacion despues de todos los test


@pytest.fixture()
def window(app_instance):
    # Crear una instancia de Task Manager para cada test
    window = TaskManager()
    window.show()
    return window