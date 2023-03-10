import random
import sys
import serial as conecta
from PyQt5.QtGui import QPixmap
from pynput.keyboard import Controller
from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "Ahorcado.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

palabras = ['SERIAL', 'PYTHON', 'ARDUINO', 'SISTEMA', 'EMBEBIDO', 'COMPUTADORA', 'SENSOR', 'DIGITAL', 'ANALOGO',
            'DOMOTICA']
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']
img = ['FotosAhorcao/1.jpg', 'FotosAhorcao/2.jpg', 'FotosAhorcao/3.jpg', 'FotosAhorcao/4.jpg', 'FotosAhorcao/5.jpg', 'FotosAhorcao/6.jpg', 'FotosAhorcao/7.jpg']


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_accion.clicked.connect(self.accion)
        self.btn_ini.clicked.connect(self.inicio)
        self.arduino = None
        self.palabra = []
        self.respuesta = []
        self.usadas = []
        self.cont = 0
        self.errores = 0
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
                if self.arduino.inWaiting():
                    # leer
                    Cadena = self.arduino.readline().decode()
                    Cadena = Cadena.replace("\r", "")
                    Cadena = Cadena.replace("\n", "")
                    Cadena = Cadena.replace(" ", "")
                    print(Cadena)
                    aux = 0
                    # print(variable)

                    if Cadena[0] == "1":
                        self.cont -= 1
                        if self.cont < 0:
                            self.cont = 25
                        if not letras[self.cont] in self.usadas:
                            self.lbl_letra.setText(letras[self.cont])
                        else:
                            self.cont -= 1
                            self.lbl_letra.setText(letras[self.cont])
                        print(self.cont)
                    elif Cadena[1] == "1":
                        self.cont += 1
                        if self.cont > 25:
                            self.cont = 0
                        if not letras[self.cont] in self.usadas:
                            self.lbl_letra.setText(letras[self.cont])
                        else:
                            self.cont += 1
                            self.lbl_letra.setText(letras[self.cont])
                        print(self.cont)
                    elif Cadena[2] == "1":
                        if letras[self.cont] in self.palabra:
                            for i in range(len(self.palabra)):
                                if self.palabra[i] == letras[self.cont]:
                                    self.respuesta[i] = letras[self.cont]
                            print(self.respuesta)
                            self.usadas.append(letras[self.cont])
                            print(self.usadas)
                            resp = ''.join(self.respuesta)
                            self.lbl_resp.setText(resp)
                        else:
                            self.errores = self.errores + 1
                            self.usadas.append(letras[self.cont])
                            print('Errores=' + str(self.errores))
                            self.lbl_img.setPixmap(QtGui.QPixmap(img[self.errores]))
                    if self.respuesta == self.palabra:
                        self.lbl_resp.setText("Ganaste :D")
                    elif self.errores == 6:
                        self.lbl_resp.setText("Perdiste :c")

    def inicio(self):
        try:
            txt_btn2 = self.btn_ini.text()
            if txt_btn2 == "Iniciar":
                self.btn_ini.setText("Reiniciar")
                self.cont = 0
                self.errores = 0
                inspa = random.choice(palabras)
                for i in inspa:
                    self.palabra.append(i)
                print(self.palabra)
                for i in range(len(inspa)):
                    self.respuesta.append('_')
                resp = ''.join(self.respuesta)
                self.lbl_resp.setText(resp)
                print(self.respuesta)
            elif txt_btn2 == "Reiniciar":
                self.cont = 0
                self.errores = 0
                self.palabra.clear()
                self.respuesta.clear()
                self.usadas.clear()
                self.lbl_img.setPixmap(QtGui.QPixmap(img[self.errores]))
                inspa = random.choice(palabras)
                for i in inspa:
                    self.palabra.append(i)
                print(self.palabra)
                for i in range(len(inspa)):
                    self.respuesta.append('_')
                resp = ''.join(self.respuesta)
                self.lbl_resp.setText(resp)
                print(self.respuesta)
        except Exception as error:
            print(error)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
