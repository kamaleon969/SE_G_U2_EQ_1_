import sys
import serial as conecta
from pynput.keyboard import Controller
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "Programa_4_Practica_JuegoDelGato.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.txt_puerto.setText("")

        self.btn_accion.clicked.connect(self.accion)
        self.btn_Jugar.clicked.connect(self.jugar)
        self.arduino = None
        self.c=0

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
                        self.controlador.press("X")
                        self.controlador.release("X")
                    elif Cadena[1]=="1":
                        self.controlador.press("O")
                        self.controlador.release("O")

                    if self.txt_V00.text()!="" and self.txt_V00.text()==self.txt_V01.text() and self.txt_V01.text()==self.txt_V02.text():
                        self.txt_Ganador.setText("G A N A S T E ! ! ! :  "+self.txt_V00.text())
                        self.c=1
                    if self.txt_V10.text()!="" and self.txt_V10.text()==self.txt_V11.text() and self.txt_V11.text()==self.txt_V12.text():
                        self.txt_Ganador.setText("G A N A S T E ! ! ! :  "+self.txt_V10.text())
                        self.c = 1
                    if self.txt_V20.text()!="" and self.txt_V20.text()==self.txt_V21.text() and self.txt_V21.text()==self.txt_V22.text():
                        self.txt_Ganador.setText("G A N A S T E ! ! ! :  "+self.txt_V20.text())
                        self.c = 1

                    if self.txt_V00.text()!="" and self.txt_V00.text()==self.txt_V10.text() and self.txt_V10.text()==self.txt_V20.text():
                        self.txt_Ganador.setText("G A N A S T E ! ! ! :  "+self.txt_V00.text())
                        self.c = 1
                    if self.txt_V01.text()!="" and self.txt_V01.text()==self.txt_V11.text() and self.txt_V11.text()==self.txt_V21.text():
                        self.txt_Ganador.setText("G A N A S T E ! ! ! :  "+self.txt_V01.text())
                        self.c = 1
                    if self.txt_V02.text()!="" and self.txt_V02.text()==self.txt_V12.text() and self.txt_V12.text()==self.txt_V22.text():
                        self.txt_Ganador.setText("G A N A S T E ! ! ! :  "+self.txt_V02.text())
                        self.c = 1

                    if self.txt_V00.text()!="" and self.txt_V00.text()==self.txt_V11.text() and self.txt_V11.text()==self.txt_V22.text():
                        self.txt_Ganador.setText("G A N A S T E ! ! ! :  "+self.txt_V00.text())
                        self.c = 1
                    if self.txt_V02.text()!="" and self.txt_V02.text()==self.txt_V11.text() and self.txt_V11.text()==self.txt_V20.text():
                        self.txt_Ganador.setText("G A N A S T E ! ! ! :  "+self.txt_V02.text())
                        self.c = 1

                    if(self.c==1):
                        self.txt_V00.setEnabled(False);self.txt_V01.setEnabled(False)
                        self.txt_V02.setEnabled(False);self.txt_V10.setEnabled(False)
                        self.txt_V11.setEnabled(False);self.txt_V12.setEnabled(False)
                        self.txt_V20.setEnabled(False);self.txt_V21.setEnabled(False)
                        self.txt_V22.setEnabled(False)

    def jugar(self):
        self.c=0
        self.txt_V00.setText("");self.txt_V01.setText("");self.txt_V02.setText("")
        self.txt_V10.setText("");self.txt_V11.setText("");self.txt_V12.setText("")
        self.txt_V20.setText("");self.txt_V21.setText("");self.txt_V22.setText("")

        self.txt_V00.setEnabled(True);self.txt_V01.setEnabled(True)
        self.txt_V02.setEnabled(True);self.txt_V10.setEnabled(True)
        self.txt_V11.setEnabled(True);self.txt_V12.setEnabled(True)
        self.txt_V20.setEnabled(True);self.txt_V21.setEnabled(True)
        self.txt_V22.setEnabled(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())