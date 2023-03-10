import sys
import serial as conecta
from pynput.keyboard import Controller
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "Programa_9_Ejercicio_LetraConPulsador_V3.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.txt_puerto.setText("")

        self.btn_accion.clicked.connect(self.accion)
        self.arduino = None

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.control)
        self.controlador = Controller()


    def accion(self):
        try:
            if not self.txt_puerto.text() == "":
                txt_btn = self.btn_accion.text()
                if txt_btn == "CONECTAR": ##arduino == None
                    self.txt_estado.setText("CONECTADO")
                    self.btn_accion.setText("DESCONECTAR")
                    #puerto = self.txt_puerto.text()
                    puerto = "COM" + self.txt_puerto.text()
                    self.arduino = conecta.Serial(puerto, baudrate=9600, timeout=1)
                    self.segundoPlano.start(10)
                elif txt_btn == "DESCONECTAR":
                    self.txt_estado.setText("DESCONECTADO")
                    self.btn_accion.setText("RECONECTAR")
                    self.segundoPlano.stop()
                    self.arduino.close()
                else: #RECONECTAR
                    self.txt_estado.setText("RECONECTADO")
                    self.btn_accion.setText("DESCONECTAR")
                    self.arduino.open()
                    self.segundoPlano.start(10)
        except Exception as error:
            print(error)

    def control(self):
        if not self.arduino == None:
            if self.arduino.isOpen():
                if self.arduino.inWaiting():

                    Cadena = self.arduino.readline().decode()
                    Cadena = Cadena.replace("\r","")
                    Cadena = Cadena.replace("\n","")

                    if not Cadena == "":
                        self.lw_datos.addItem(Cadena)
                        self.lw_datos.setCurrentRow(self.lw_datos.count()-1)

                    Cadena=Cadena.replace(" ","")
                    if Cadena[0]=="1":
                        self.controlador.press("A")
                    elif Cadena[1]=="1":
                        self.controlador.press("B")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())