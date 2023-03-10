import sys
import serial as conecta

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "Programa_11_Clase_HastaXX_VariosSensores.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_accion.clicked.connect(self.accion)
        self.arduino = None

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.control)

        self.btn_control_led.setText("ENVIAR") #ENVIAR CADENA ACTUADORES
        self.btn_control_led.clicked.connect(self.control_led)
        #self.btn_control_led.setEnabled(False)

    # Área de los Slots
    def control_led(self):
        if not self.arduino == None:
            if self.arduino.isOpen():
                #ENVIO DE CADENA SERIALIZADA....

                #1.- LEER LOS VALORES DE LOS SENSORES .. (PEND)
                #2.- PROCESAR LOS VALORES PARA OBTENER UNA RESPUESTA (PEND)

                #3.- ENVIAR RESULTADO DE CONTROL DE ACTUADORES A ARDUINO ...

                actuador1  = 1
                actuador2 = 56
                actuador3 = 300

                #Paso 1
                actuador1 = self.validaLongitud(actuador1)
                actuador2 = self.validaLongitud(actuador2)
                actuador3 = self.validaLongitud(actuador3)

                ##  E + ACTUADOR1 + R + ACTUADOR 2 + R + ACTUADOR 3 + C

                cadenaSerializada = "E" + actuador1 + "R" + actuador2 + "R"  \
                    + actuador3 + "C"

                print(cadenaSerializada)

                self.arduino.write(cadenaSerializada.encode())


    def validaLongitud(self, valActuador):
        #CONSIDERANDO QUE SON ACTUADORES ANALOGICOS, EL VALOR MAS GRANDE ES 255
        cadenaModificada = "0" * (3 - len(str(valActuador))) + str(valActuador)
        return cadenaModificada


    def accion(self):
        try:
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
                self.arduino.open()
                self.segundoPlano.start(10)
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
                    #print(variable)
                    if not variable == "":
                        self.lw_datos.addItem(variable)
                        self.lw_datos.setCurrentRow(self.lw_datos.count()-1)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

