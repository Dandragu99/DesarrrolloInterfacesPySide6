

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QApplication, QMessageBox




class TaskManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de tareas")
        self.setGeometry(100, 100, 400, 300)
        self.layout = QVBoxLayout()
        self.task_input = QLineEdit()
        self.task_input.setPlaceHolderText("Escribe una tarea")
        self.layout.addWidget(self.task_input)
        self.add_button = QPushButton("Agregar tarea")
        self.add_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_button)
        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)
        self.delete_button = QPushButton("Eliminar tarea")
        self.delete_button.clicked.connect(self.delete_task)
        self.layout.addWidget(self.delete_button)
        self.setLayout(self.layout)

    def add_task(self):
        task = self.task_input.text().strip()
        if task:
            self.task_list.addItem(task)
            self.task_imput.clear()
        else:
            QMessageBox.warning(self, "Error", "La tarea no puede estar vacía")

    def delete_task(self):
        selected_item = self.task_list.currentRow()

        if selected_item >= 0:
            self.task_list.takeItem(selected_item)

        else:
            QMessageBox.warning(self, "Error", "Seleccioname una tarea para eliminar")

if __name__=="__main__":
    app = QApplication([])
    window = TaskManager()
    window.show()
    app.exec()




