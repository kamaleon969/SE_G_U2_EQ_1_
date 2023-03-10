import serial as s
Lecturas=5
i=0
Lista=[]

arduino=s.Serial("COM4",baudrate=9600,timeout=1)

while i<Lecturas:
    """
    Cadena=arduino.readline() --> Imprime como... b'419/r/n'
    Cadena=Cadena.decode() --> Imprime como... 419 con salto de linea
    Cadena=Cadena.replace("\n","").replace("\r","") --> Imprime normal como debe de ser.
    Entonces...
    """
    Cadena=arduino.readline().decode().replace("\n","").replace("\r","")
    if(Cadena!=""):
        Lista.append(Cadena)
        i+=1

Lista=list(map(int,Lista))
print(Lista)