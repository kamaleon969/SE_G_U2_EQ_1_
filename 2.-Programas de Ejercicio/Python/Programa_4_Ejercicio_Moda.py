import serial as s
arduino = None

arduino = s.Serial("COM3", baudrate=9600, timeout=1)

lista = []
totlecturas = 10
i = 0
cont=0
may=0

while i < totlecturas:
    cadena = arduino.readline()
    cadena = cadena.decode()
    cadena = cadena.replace("\n","")
    cadena = cadena.replace("\r", "")
    if cadena != "":
        cadena=int(cadena)
        lista.append(cadena)
        i += 1

lista.sort()

for j in range(totlecturas-1):
    if lista[j]==lista[j+1]:
        cont+=1
    else:
        if cont>may:
            mod=lista[j]
            may=cont
        cont=1

print(lista)
print(mod)
print(may)
