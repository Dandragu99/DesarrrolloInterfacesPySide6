import sqlite3
import sys
from base64 import b64encode

import bcrypt
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QLineEdit, QPushButton, QWidget, \
    QMessageBox, QTableWidget, QTableWidgetItem, QAbstractItemView, QCheckBox


def crear_base_datos():
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL UNIQUE,
        contrasena TEXT NOT NULL,
        ed_admin INTEGER NOT NULL DEFAULT 0
    )
    ''')

    conexion.commit()
    conexion.close()


class LoginForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio de sesión")
        self.setGeometry(100, 100, 300, 250)

        # LAYOUT PRINCIPAL EN VERTICAL
        main_layout = QVBoxLayout()
        title = QLabel("Inicio de sesion")
        main_layout.addWidget(title)

        # Entrada de texto área para el usuario
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Nombre usuario")
        main_layout.addWidget(self.username_input)

        # ENTRADA DE TEXTO PARA LA CONTRASEÑA

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Contraseña")
        self.password_input.setEchoMode(QLineEdit.Password)
        main_layout.addWidget(self.password_input)

        # Boton de inicio de sesion
        login_button = QPushButton("Iniciar sesion")
        login_button.clicked.connect(self.iniciar_sesion)
        main_layout.addWidget(login_button)

        # Boton para pasar al la ventan de registro
        register_button = QPushButton("Registrar")
        register_button.clicked.connect(self.volver_a_registro)
        main_layout.addWidget(register_button)

        # ESTABLECER EL LAYOUT PRINCIPAL
        central_wiget = QWidget()
        central_wiget.setLayout(main_layout)
        self.setCentralWidget(central_wiget)

    def volver_a_registro(self):
        self.login = RegisterForm()
        self.login.show()
        self.close()

    def iniciar_sesion(self):
        usuario = self.username_input.text()
        contrasena = self.password_input.text()

        if not usuario or not contrasena:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios")

        conexion = sqlite3.connect("usuarios.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT contrasena, ed_admin FROM usuarios WHERE usuario = ?", (usuario, ))
        resultado = cursor.fetchone()
        conexion.close()

        if resultado and bcrypt.checkpw(contrasena.encode(), resultado[0]):
            self.bienvenida = WelcomeForm(usuario, resultado[1])
            self.bienvenida.show()
            self.close()
        else:
            QMessageBox.critical(self, "Error", "Usuario o Contraseña incorrecta")
            self.password_input.clear()
            self.username_input.clear()


class RegisterForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro")
        self.setGeometry(100, 100, 400, 400)

        # LAYOUT PRINCIPAL EN VERTICAL
        main_layout = QVBoxLayout()
        title = QLabel("Registro")
        main_layout.addWidget(title)

        # Entrada de texto área para el usuario
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Nombre usuario")
        main_layout.addWidget(self.username_input)

        # ENTRADA DE TEXTO PARA LA CONTRASEÑA

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Contraseña")
        self.password_input.setEchoMode(QLineEdit.Password)
        main_layout.addWidget(self.password_input)

        # CHECKBOX PARA MARCAR SI ES ADMINISTRADOR

        self.admin_checkbox = QCheckBox("¿Es administrador?")
        main_layout.addWidget(self.admin_checkbox)

        # Boton para registro de usuario
        register_button = QPushButton("Registrar")
        register_button.clicked.connect(self.registrar_usuario)
        main_layout.addWidget(register_button)

        # Boton para pasar al la ventan de registro
        back_button = QPushButton("Iniciar sesion")
        back_button.clicked.connect(self.volver_al_login)
        main_layout.addWidget(back_button)

        # ESTABLECER EL LAYOUT PRINCIPAL
        central_wiget = QWidget()
        central_wiget.setLayout(main_layout)
        self.setCentralWidget(central_wiget)

    def volver_al_login(self):
        self.login = RegisterForm()
        self.login.show()
        self.close()

    def registrar_usuario(self):
        usuario = self.username_input.text()
        contrasena = self.password_input.text()

        if not usuario or not contrasena:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios")
        else:
            # ENCRIPTAR CONTRASEÑA
            contrasena_encriptada = bcrypt.hashpw(contrasena.encode(), bcrypt.gensalt())
            try:
                conexion = sqlite3.connect("usuarios.db")
                cursor = conexion.cursor
                cursor.execute("INSERT INTO usuarios(usuario, contrasena) VALUES (?,?)",
                               (usuario, contrasena_encriptada))
                conexion.commit()
                conexion.close()
                QMessageBox.information(self, "Exito", "El usuario ha sido registrado")
                self.volver_al_login()
            except sqlite3.IntegrityError:
                QMessageBox.critical(self, "Error", "El usuario ya existe")


class WelcomeForm(QMainWindow):
    def __init__(self, usuario):
        super().__init__()
        self.setWindowTitle("Bienvenida")
        self.setGeometry(100, 100, 600, 400)

        self.usuario = usuario

        # LAYOUT PRINCIPAL
        main_layout = QVBoxLayout()

        # ETIQUETA PRINCIPAL
        self.welcome_label = QLabel(f"¡Bienvenido,{usuario}!")
        main_layout.addWidget(self.welcome_label)

        # PINTAR LA TABLA

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Usuario", "Contraseña encriptada"])
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        main_layout.addWidget(self.table)
        self.cargar_usuario()

        # BOTON PARA ELIMINAR UNA CUENTA

        delete_button = QPushButton("Borrar cuenta seleccionada")
        delete_button.clicked.connect(self.borrar_cuenta)
        main_layout.addWidget(delete_button)

        # ESTABLECER EL LAYOUT PRINCIPAL COMO EL CENTRAL

        central_widget = QWidget
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def cargar_usuario(self):
        conexion = sqlite3.connect("usuarios.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT usuario, contrasena FROM usuario")
        usuarios = cursor.fetchall()
        conexion.close()
        self.table.setRowCount(len(usuarios))

        for row, (usuario, contrasena) in enumerate(usuarios):
            self.table.setItem(row, 0, QTableWidgetItem(usuario))
            contrasena_legible = b64encode(contrasena).decode("utf-8")
            self.table.setItem(row, 1, QTableWidgetItem(contrasena_legible))

    def borrar_cuenta(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Selecciona una cuenta para borrarla")
        else:
            usuario = self.table.items(selected_row, 0).text()
            respuesta = QMessageBox.question(
                self,
                "Confirmacion",
                f"¿Esta seguro que quiere borrar la cuenta de '{usuario}'",
                QMessageBox.Yes | QMessageBox.No
            )

            if respuesta == QMessageBox.Yes:
                conexion = sqlite3.connect("usuarios.db")
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM usuarios WHERE usuario = ?", (usuario,))
                conexion.commit()
                conexion.close()

                QMessageBox.information(self, "Exito", "Cuenta eliminada con éxito")
                self.cargar_usuario()



    def salir(self):
        """Cierra la sesión y regresa al incio de sesión."""
        self.login = LoginForm()
        self.login.show()
        self.close()

if __name__ == "__main__":
    # Crear la base de datos si no existe
    crear_base_datos()

    # Iniciar la aplicación
    app = QApplication(sys.argv)
    ventana = LoginForm()
    ventana.show()
    sys.exit(app.exec())
