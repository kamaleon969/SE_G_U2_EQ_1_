from pynput.keyboard import Controller


controlador=Controller()

controlador.press("G")
controlador.press("A")
controlador.press("T")
controlador.press("O")

controlador.release("G")
controlador.release("A")
controlador.release("T")
controlador.release("O")