import sys
import serial as conecta

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "Programa_9_Practica_AumentoLW_and_Csv.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_accion.clicked.connect(self.accion)
        self.btn_Visualizar.clicked.connect(self.Vis)
        self.arduino = None

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.control)
        archivo = open("Programa_1_Practica_AumentoLW_and_Csv.csv", "w")
        archivo.write("")
        archivo.flush()
        archivo.close()

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
                    variable = self.arduino.readline().decode().replace("\r", "").replace("\n", "")
                    self.segundoPlano.start(100)
                elif txt_btn == "DESCONECTAR":
                    self.txt_estado.setText("DESCONECTADO")
                    self.btn_accion.setText("RECONECTAR")
                    self.btn_Visualizar.setText("NO VISUALIZAR")
                    self.segundoPlano.stop()
                    self.arduino.close()
                else: #RECONECTAR
                    self.txt_estado.setText("RECONECTADO")
                    self.btn_accion.setText("DESCONECTAR")
                    variable = self.arduino.readline().decode().replace("\r", "").replace("\n", "")
                    self.segundoPlano.start(100)
                    self.arduino.open()
        except Exception as error:
            print(error)

    def Vis(self):
        try:
            if not self.txt_puerto.text() == "":
                txt_ver = self.btn_Visualizar.text()
                if txt_ver == "VISUALIZAR":
                    self.btn_Visualizar.setText("NO VISUALIZAR")
                elif txt_ver == "NO VISUALIZAR":
                    self.btn_Visualizar.setText("VISUALIZAR")
        except Exception as error:
            print(error)


    def control(self):
        if not self.arduino == None:
            if self.arduino.isOpen():
                txt_ver = self.btn_Visualizar.text()
                if txt_ver == "NO VISUALIZAR":
                    #leer
                    variable = self.arduino.readline().decode()
                    variable = variable.replace("\r","")
                    variable = variable.replace("\n","")

                    self.lw_datos.addItem(variable)
                    self.lw_datos.setCurrentRow(self.lw_datos.count() - 1)

                    archivo = open("Programa_1_Practica_AumentoLW_and_Csv.csv", "a")
                    archivo.write("LW  : " + str(variable) + "\n")
                    archivo.flush()
                    archivo.close()
                else:
                    variable = self.arduino.readline().decode()
                    variable = variable.replace("\r", "")
                    variable = variable.replace("\n", "")
                    archivo = open("Programa_1_Practica_AumentoLW_and_Csv.csv", "a")
                    archivo.write("CSV : "+str(variable)+"\n")
                    archivo.flush()
                    archivo.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())