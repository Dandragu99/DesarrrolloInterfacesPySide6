import self
from PySide6.QtCore import Property, Signal, QTime, QTimer, Slot
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QPushButton, QApplication, QGraphicsDropShadowEffect


class CustomButton(QPushButton):
        ## Definimos una señal personalizada que emitirá cuando el texto cambie
    texto_cambiado = Signal(str)
    def __init__(self, text = "Texto Inicial"):
        super().__init__(text)  # Llamamos al constructor de QPushButton con texto inicial
        self._text = text # Inicializamos el atributo _text con el texto proporcionado
        self.set_color_bases_on_text() # Llamar a la función
        self.set_text_size(12) #Establezco el tamaño del boton a 12 px
        self.add_shadow_effect()
        self.texto_cambiado.connect(self.on_text_changed)
    @Property(str)  # Defino una propiedad text que devuelve el valor de texto
    def text(self):
        return self._text

    @text.setter
    def text(self,value): # Si el texto es distinto al anterior
        if self._text_!= value:
            self._text = value # Actualizo la variable interna
            self.setText(value) # Cambio el texto del boton
            self.texto_cambiado.emit(value) # Emito la señal del textoCombinado para notificar el cambio


    def set_color_bases_on_text(self):
        # Defino un diccionario que a un valor del texto lo mapea a un  color
        color_map = {
        "Rojo": "red",
        "Verde": "green",
        "Azul": "blue"
        }
        color = color_map.get(self._text, "gray") # Si no encuentra el texto usamos el color gris por defecto
        self.setStyleSheet(f"background-color:{color};") # Establecemos el color de fondo del boton


    def set_text_size(self,size):
        self.setStyleSheet(f"font-size:{size} px") #Estyablecemos el tamañño usando CSS

    def add_shadow_effect(self):
        # Crear un efecto de sombrea
        shadow = QGraphicsDropShadowEffect()
        # Establece el radio de difución
        shadow.setBlurRadius(10)
        # Establecemos el color de la sombra
        shadow.setColor(QColor(0,0,0,160))
        # Desplazamiento de la sombra
        shadow.setOffset(3.3)
        # Aplico el efecto de la sombra al boton
        self.setGraphicsEffect(shadow)

    def animate_color_change(self, target_color):
        # Inicializamos el color actual con el color objetivo
        self.current_color = QColor(self.palette().button().color())
        self.target_color = QColor(target_color)

    #Cambio el color de manera gradual
        self.timer = QTimer()
        self.timer.timeout.connect(self.step_color_change) #Conectamos el temporizador al cambio de color
        self.timer.start(50) # Este temporizador se ajusta cada 50 ms

    def step_color_change(self):
        step = 10 # CAmbio del color
        current_rgb = self.current_color.getRgb()[:3]
        target_rgb = self.target_color.getRgb()[:3]
        # Calcular el nuevo RGB intermedio
        new_rgb = [
            min(255, max(0, current_rgb[i] + target_rgb[i] - current_rgb[i]) // step)
            for i in range(3)
        ]
        self.current_color.setRgb(*new_rgb)
        self.setStyleSheet(f"background-color: {self.current_color.name()};") # Aplicar el nuevo color
        if self.current_color == self.target_color:
            self.timer.stop()

    def set_text_size(self, size):
        self.setStyleSheet(f"font-size:{size} px")

    @Slot(str) # TextoCambiado ha sido emitidio pues se ejecuta



    def on_text_changed(self, new_text):
        self.new_text_size(16)
        print(f"El texto del boton se cambio")
        self.set_text_size(16)

if __name__ == "__main__":
    app = QApplication([]) # Aplicacion de QT
    button = CustomButton("Rojo")
    button.show()
    button.setText("Verde")
    button.animate_color_change("green") # Iniciamos la aniamcion de cambio de color hacia el azul
    app.exec()

