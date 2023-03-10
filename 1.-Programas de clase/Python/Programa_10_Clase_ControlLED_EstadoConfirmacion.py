import sys
import serial as conecta

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "Programa_10_Clase_ControlLED_EstadoConfirmacion.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_accion.clicked.connect(self.accion)
        self.arduino = None

        self.btn_Led.clicked.connect(self.controlLed)
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.control)

    def controlLed(self):
        if not self.arduino == None:
            if self.arduino.isOpen():
                textoBoton=self.btn_Led.text()
                if(textoBoton == "PRENDER"):
                    self.arduino.write("1".encode())
                    self.btn_Led.setText("APAGAR")
                else:
                    self.arduino.write("0".encode())
                    self.btn_Led.setText("PRENDER")

    # Área de los Slots
    def accion(self):
        try:
            if not self.txt_puerto.text() == "":
                txt_btn = self.btn_accion.text()
                if txt_btn == "CONECTAR": ##arduino == None
                    self.txt_estado.setText("CONECTADO")
                    self.btn_accion.setText("DESCONECTAR")
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
                    self.segundoPlano.start(10)
                    self.arduino.open()
        except Exception as error:
            print(error)
        #self.arduino.isOpen()

    def control(self):
        if not self.arduino == None:
            if self.arduino.isOpen():
                if self.arduino.inWaiting():
                    #leer
                    variable = self.arduino.readline().decode()
                    variable = variable.replace("\r","")
                    variable = variable.replace("\n","")
                    if not variable == "":
                        self.lw_datos.addItem(variable)
                        self.lw_datos.setCurrentRow(self.lw_datos.count() - 1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())