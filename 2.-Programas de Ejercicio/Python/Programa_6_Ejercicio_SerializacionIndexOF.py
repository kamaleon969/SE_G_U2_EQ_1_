import sys
import serial as conecta

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "Programa_6_Ejercicio_Serializacion4pasos.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_accion.clicked.connect(self.accion)
        self.arduino = None
        #TextoA123A456A

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.control)

        self.btn_control_led.setText("ENVIAR")  # ENVIAR CADENA ACTUADORES
        self.btn_control_led.clicked.connect(self.control_led)
        # self.btn_control_led.setEnabled(False)

    # Área de los Slots
    def accion(self):
        try:
            txt_btn = self.btn_accion.text()
            if txt_btn == "CONECTAR":  ##arduino == None
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
            else:  # RECONECTAR
                self.txt_estado.setText("RECONECTADO")
                self.btn_accion.setText("DESCONECTAR")
                self.arduino.open()
                self.segundoPlano.start(10)
        except Exception as error:
            print(error)
        # self.arduino.isOpen()

    def control_led(self):
        if not self.arduino == None:
            if self.arduino.isOpen():

                actuador1 = 1
                actuador2 = 30
                actuador3 = 254

                # Paso 1
                actuador1 = self.validaLongitud(actuador1)
                actuador2 = self.validaLongitud(actuador2)
                actuador3 = self.validaLongitud(actuador3)

                cadenaSerializada = "E" + actuador1 + "R" + actuador2 + "R" + actuador3 + "C"
                #E001R056R255C
                self.arduino.write(cadenaSerializada.encode())
                print(cadenaSerializada)
                if cadenaSerializada[0] == 'E' or cadenaSerializada[0] == 'C':
                    cadenaSerializada = cadenaSerializada.replace('E', ' ')
                    cadenaSerializada = cadenaSerializada.replace('C', ' ')
                val1, val2, val3 = cadenaSerializada.split("R")

                val1 = int(val1)
                val2 = int(val2)
                val3 = int(val3)

                print('valores: ',val1, '',val2, '',val3)

                resultado = ':'+str(val1)+','+str(val2)+','+str(val3)

                self.arduino.write(resultado.encode())
                #E001R056R255C:1,56,255
                print(resultado)

    def validaLongitud(self, valActuador):
        # CONSIDERANDO QUE SON ACTUADORES ANALOGICOS, EL VALOR MAS GRANDE ES 255
        cadenaModificada = "0" * (3 - len(str(valActuador))) + str(valActuador)
        return cadenaModificada

    def control(self):
        if not self.arduino == None:
            if self.arduino.isOpen():
                if self.arduino.inWaiting():
                    # leer
                    variable = self.arduino.readline().decode()
                    variable = variable.replace("\r", "")
                    variable = variable.replace("\n", "")

                    if not variable == "":
                        self.lw_datos.addItem(variable)
                        self.lw_datos.setCurrentRow(self.lw_datos.count() - 1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
