import serial as s

arduino = None

arduino = s.Serial("COM3", baudrate=9600, timeout=1)

lista = []
totlecturas = 9
i = 0
med = 0

while i < totlecturas:
    cadena = arduino.readline()
    cadena = cadena.decode()
    cadena = cadena.replace("\n", "")
    cadena = cadena.replace("\r", "")
    if cadena != "":
        cadena = int(cadena)
        print(cadena)
        lista.append(cadena)
        i += 1

for j in range(totlecturas):
    if (totlecturas % 2 == 0):
        med = ((lista[int(totlecturas / 2)] + lista[int(totlecturas / 2 - 1)]) / 2)
    else:
        med = (lista[int(totlecturas / 2)])

print("mediana: ", med)
