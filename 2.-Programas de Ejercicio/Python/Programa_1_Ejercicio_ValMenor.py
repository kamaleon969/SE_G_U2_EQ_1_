import serial as s
arduino = None

arduino = s.Serial("COM4", baudrate=9600, timeout=1)

lista = []
totlecturas = 30
i = 0
valor=999999

while i < totlecturas:
    cadena = arduino.readline()
    cadena = cadena.decode()
    cadena = cadena.replace("\n","")
    cadena = cadena.replace("\r", "")
    if cadena!="":
        lista.append(cadena)
        i+=1

lista = list(map(int, lista))
print(lista)

for i in range(totlecturas):
    if(lista[i]<valor):
        valor=lista[i]

print("\nValor menor: ",valor)