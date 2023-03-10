import random
import sys
import serial as conecta
from pynput.keyboard import Controller
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "Ahorcado.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

palabras = ['SERIAL', 'PYTHON', 'ARDUINO', 'SISTEMA', 'EMBEBIDO', 'COMPUTADORA', 'SENSOR', 'DIGITAL', 'ANALOGO',
            'DOMOTICA']
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_accion.clicked.connect(self.accion)
        self.btn_ini.clicked.connect(self.inicio)
        self.arduino = None
        self.palabra = ''
        self.respuesta = ''
        self.cont = 0
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.control)
        self.controlador = Controller()

    # Área de los Slots
    def accion(self):
        try:
            if not self.txt_puerto.text() == "":
                txt_btn = self.btn_accion.text()
                if txt_btn == "CONECTAR":  ##arduino == None
                    self.txt_estado.setText("CONECTADO")
                    self.btn_accion.setText("DESCONECTAR")
                    puerto = "COM" + self.txt_puerto.text()
                    self.arduino = conecta.Serial(puerto, baudrate=9600, timeout=1)
                    self.segundoPlano.start(100)
                elif txt_btn == "DESCONECTAR":
                    self.txt_estado.setText("DESCONECTADO")
                    self.btn_accion.setText("RECONECTAR")
                    self.segundoPlano.stop()
                    # self.arduino.close()
                else:  # RECONECTAR
                    self.txt_estado.setText("RECONECTADO")
                    self.btn_accion.setText("DESCONECTAR")
                    self.segundoPlano.start(100)
                    # self.arduino.open()
        except Exception as error:
            print(error)
        # self.arduino.isOpen()

    def control(self):
        if not self.arduino == None:
            if self.arduino.isOpen():

                self.lbl_letra.setText(letras[self.cont])
                Cadena = self.arduino.readline().decode()
                Cadena = Cadena.replace("\r", "")
                Cadena = Cadena.replace("\n", "")

                if not Cadena == "":
                    self.lw_datos.addItem(Cadena)
                    self.lw_datos.setCurrentRow(self.lw_datos.count() - 1)

                Cadena = Cadena.replace(" ", "")
                if Cadena[0] == "1":
                    self.cont -= 1
                    self.lbl_letra.setText(letras[self.cont])
                    if self.cont < 0:
                        self.cont = 25
                elif Cadena[1] == "1":
                    self.cont += 1
                    self.lbl_letra.setText(letras[self.cont])
                    if self.cont > 25:
                        self.cont = 0
                # elif Cadena[2] == "1":
                # for i in range(len(self.palabra)):
                # if self.palabra[i] == letras[self.cont]:

    def inicio(self):
        try:
            txt_btn2 = self.btn_ini.text()
            if txt_btn2 == "Iniciar":
                self.btn_ini.setText("Reiniciar")
                self.cont = 0
                self.palabra = random.choice(palabras)
                print(self.palabra)
                self.respuesta = '_' * len(self.palabra)
                print(self.respuesta)
            elif txt_btn2 == "Reiniciar":
                self.palabra = random.choice(palabras)
                print(self.palabra)
                self.respuesta = '_' * len(self.palabra)
                print(self.respuesta)
        except Exception as error:
            print(error)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
