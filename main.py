
# las importaciones al principio
import time
import random


# AQUI AGREGAMOS LA CLASE COLOR CON COLORES COMO PROPIEDAD
class color:
    ROSA = "\033[95m"
    CYAN = "\033[96m"
    CYANOSCURO = "\033[36m"
    AZUL = "\033[94m"
    VERDE = "\033[92m"
    AMARILLO = "\033[93m"
    ROJO = "\033[91m"
    NEGRITA = "\033[1m"
    LINEA = "\033[4m"
    FIN = "\033[0m"


# ESTABLECEMOS PREMIO POR DEFECTO
class config:
    PREMIO = "Una entrada al CINE"
    MAX_INTENTOS = 2
    INTENTOGANADOR = 1
    SCRM=0
    SCRU=0
    JUEGO_NUM=0


# mis funciones
def muestraMisLineas():
    print(color.ROSA, "-----------------------", color.FIN)


def muestraMiProgresbar(cuanto):
    for i in range(1, cuanto + 1):
        time.sleep(0.1)
        ancho = "[{}{}] - {}\r".format(
            (i * " * "),
            ((cuanto - i) * " - "),
            (("{:0.2f}".format(((i) * (100 / cuanto))) + "%")),
        )
        print(color.ROSA, ancho, end="")
    print(color.FIN)


def salirDelJuego():
    print(color.ROJO, "Intentos superados", color.FIN)
    exit()


def muestraLaAyuda():
    print(color.AMARILLO)
    print("Este un juego para obtener una decisión rapida entre dos personas.")
    print("En esta trivia jugaras con la máquina.")
    print(
        "Debes elegir una de las tres opciones dada(piedra, papel o tijera).",
        color.FIN)
    desarrollaElJuego()


def muestraElMenu():
    print(color.NEGRITA, "\n", "MENU DEL JUEGO:")
    muestraMisLineas()
    print("a: Mostrar ayuda")
    print("c: Configurar premio")
    print("i: Configurar # Intento Ganador")
    print("j: Jugar ahora")
    print("s: Salir del juego")
  
    return input("Ingresa una opción:")


def configuraElPremio():
    print("\n", color.AMARILLO)
    print(
        "Tu premio esta configurado a: (" + config.PREMIO +
        "). Para cambiar selecciona un nuevo premio", color.AMARILLO)
    premios = { "c": "Un cafecito", "p": "Una pizza", "m": "Una entrada al cine" }

    print("c: Un cafecito")
    print("p: Una pizza")
    print("m: Una entrada al cine", color.FIN)
    opPremio = input("Ingresa una opcion:")
    intento = 0
    ops1 = ["c", "p", "m"]
    while (opPremio not in ops1 and intento <= config.MAX_INTENTOS):
        intento = intento + 1
        opPremio = input("Opcion incorrecta, Ingresa c, p o m:")
    if opPremio not in ops1:
        salirDelJuego()

    config.PREMIO = premios[opPremio]
    print(color.VERDE, "Correctamente cambiado", color.FIN)
    desarrollaElJuego()


def configIntentoGanador():
    print("\n", color.AMARILLO)
    print(
        "Numero Intentos Por Defecto es a: (" + str(config.INTENTOGANADOR) +
        "). Para cambiar selecciona un nuevo Numero Intento Ganador", color.AMARILLO)

    intentoGan = { "1":1, "2":2, "3":3 }
    print("1: Un Intento")
    print("2: Dos Intentos")
    print("3: Tres Intentos", color.FIN)

    opIntentoGanador = input("Ingresa una opcion:")
    opsI = ["1","2","3"]
    l=0

    while (opIntentoGanador not in opsI and l <= config.MAX_INTENTOS):
        l = l + 1
        opIntentoGanador = input("Opcion incorrecta, Ingresa 1, 2 o 3:")
    if opIntentoGanador not in opsI:
        salirDelJuego()

    config.INTENTOGANADOR = intentoGan[opIntentoGanador]
    print(color.VERDE, "Correctamente cambiado", color.FIN, "\n")
    GooGame()

def mostrarScore(SM,SU):
    config.SCRM=config.SCRM+SM
    config.SCRU=config.SCRU+SU

    if config.JUEGO_NUM <= config.INTENTOGANADOR :
        if config.SCRM > config.SCRU : print("Perdiste !", "\n")
        if config.SCRU > config.SCRM : print("Ganaste !", "\n")
        if config.SCRU == config.SCRM : print("Empate !", "\n")

    if config.JUEGO_NUM == config.INTENTOGANADOR:
        if config.SCRM > config.SCRU :
            print(color.AZUL, "Partida Final: Sigue Intentando!, Perdiste. "+ str(config.SCRM) + " a " + str(config.SCRU), "\n")
            desarrollaElJuego()
        if config.SCRU > config.SCRM :
            print(color.AZUL, "Partida Final: Ganaste!, "+ str(config.SCRU) + " a " + str(config.SCRM), ",Te debo ", config.PREMIO, "\n")
            desarrollaElJuego()
        if config.SCRU == config.SCRM :
            print(color.AZUL, "Partida Final: Sigue Intentando!, Empate. "+ str(config.SCRM) + " a " + str(config.SCRU), "\n")        
            desarrollaElJuego()

def GooGame():
    for x in range(config.INTENTOGANADOR):
        jugarAhora()


def jugarAhora():
    config.JUEGO_NUM=config.JUEGO_NUM + 1
    print("Juego #: " + str(config.JUEGO_NUM))
    opciones = ["piedra", "papel", "tijera"]
    # le muestro las opciones al user
    print(color.AZUL, "Inicia el juego! Elije una opcion:")
    print("1: piedra.")
    print("2: papel.")
    print("3: tijera.")
    opcionUsuario = input("Ingresa aquí:")
    if opcionUsuario in ["1", "2", "3"]:
        opcionM = random.randint(1, 3)
        opcionU = int(opcionUsuario)
        SCOREM=0
        SCOREU=0
        print("--------")
        print("Elijiste         : ", opciones[opcionU - 1], color.VERDE)
        print("La máquina eligió: ", opciones[opcionM - 1], color.FIN)
        if opcionM == 1:
            if opcionU == 1: mostrarScore(0,0)
            elif opcionU == 2: mostrarScore(0,1)
            else: mostrarScore(1,0)

        elif opcionM == 2:
            if opcionU == 1: mostrarScore(1,0)
            elif opcionU == 2: mostrarScore(0,0)
            else: mostrarScore(0,1)

        else:
            if opcionU == 1: mostrarScore(0,1)
            elif opcionU == 2: mostrarScore(1,0)
            else: mostrarScore(0,0)
    else:
        print(color.ROJO, "Ingresar De Nuevo !", color.FIN)
        desarrollaElJuego()


def desarrollaElJuego():
    
    config.JUEGO_NUM=0
    config.SCRM=0
    config.SCRU=0
    # MENU DEL JUEGO
    OP_PRINCIPAL = muestraElMenu()
    ops = ["a", "c","i","j", "s"]
    # VALIDAMOS
    chance_op = 0
    while (OP_PRINCIPAL not in ops and chance_op <= config.MAX_INTENTOS):
        chance_op = chance_op + 1
        OP_PRINCIPAL = input("Opcion incorrecta, ingresa nuevamente:")

    if OP_PRINCIPAL not in ops:
        salirDelJuego()

    if OP_PRINCIPAL == "a": muestraLaAyuda()
    elif OP_PRINCIPAL == "c": configuraElPremio()
    elif OP_PRINCIPAL == "i": configIntentoGanador()
    elif OP_PRINCIPAL == "j": GooGame()
    else: salirDelJuego()


# INICIO DEL PROGRAMA
# Aqui mostramos en la pantalla el texto de bienvenida
print(color.NEGRITA, "Hola! Bienvenido a mi trivia")
# llamamos nuestra funcion aqui
muestraMisLineas()
# Obtenemos el nombre aqui
name = input("¿Me podrías decir como quieres que te llame?\nIngresa Aqui:")

lin = 0
while name == "" and lin <= config.MAX_INTENTOS:
    lin = lin + 1
    name = input("Tu nombre es obligatorio:")
# Damos bienvenida

if name == "":
    salirDelJuego()
else:
    print(
        color.VERDE,
        "Bienvenido " + name + ", Ahora vamos a jugar piedra papel o tijeras",
        color.FIN,
    )

# carga el juego!!!
muestraMiProgresbar(5)

desarrollaElJuego()
