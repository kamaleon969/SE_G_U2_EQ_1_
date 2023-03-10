import serial as s

arduino=s.Serial("COM4",baudrate=9600,timeout=1)

while True:
    """
    Cadena=arduino.readline() --> Imprime como... b'419/r/n'
    Cadena=Cadena.decode() --> Imprime como... 419 con salto de linea
    Cadena=Cadena.replace("\n","").replace("\r","") --> Imprime normal como debe de ser.
    Entonces...
    """
    Cadena=arduino.readline().decode().replace("\n","").replace("\r","")
    print(Cadena)
