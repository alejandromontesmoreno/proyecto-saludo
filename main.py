from PyQt5 import QtWidgets, uic
import sys

class VentanaSaludo(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("view/dialog_saludo.ui", self)

        # Conectar botón
        self.btnSaludar.clicked.connect(self.saludar)

    def saludar(self):
        nombre = self.txtNombre.text()
        if nombre:
            self.lblSaludo.setText(f"¡Hola, {nombre}!")
        else:
            self.lblSaludo.setText("Por favor, ingresa tu nombre.")

if __name__ == "__main__":
    print('Ejecutando main...')
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaSaludo()
    ventana.show()
    sys.exit(app.exec_())
