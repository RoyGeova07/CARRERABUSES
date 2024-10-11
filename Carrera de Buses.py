import time
import os # aqui se necesita el os para que permita interactuar con el sistema operativo (aqui para limpiar la pantalla mientras los buses avanzan)
from random import randint # aqui el randiant genera numeros aleatorios, que se usa para determinar cual bus avanza 
import pygame
from pygame import mixer # mixer para el uso del audio

# aqui se iniciliza el audio 
mixer.init()

# Funcion para reproducir el audio al inicio
def play_audio():
    mixer.music.load('C:/Users/royum/Downloads/Escritorio/python007/carreraBusesAudio.mp3') #aqui cargamos el audio 
    mixer.music.play(-1) # con esto reproduce el audio indefinidamente con el -1, por lo que la musica continuara hasta que sea detenida manualmente


# Funcion para detener el audio al finalizar la carrera
def stop_audio():
    mixer.music.stop()

# Funcion para dibujar los buses
def buses(n1, n2):
    print(115 * "-") # el print(115 * "-") se encarga de imprimir 115 guiones, esta linea se usa para separar los 2 buses
    print((n1 * " ") + "________________" + ((100 - n1) * " ") + "|")
    print((n1 * " ") + "|__|__|__|__|__|__" + ((97 - n1) * " ") + "|")
    print((n1 * " ") + "|     COTUC       |" + ((96 - n1) * " ") + "|")
    print((n1 * " ") + "|----@--------@---|" + ((96 - n1) * " ") + "|")
    print(115 * "-")
    print((n2 * " ") + "________________" + ((100 - n2) * " ") + "|")
    print((n2 * " ") + "|__|__|__|__|__|__" + ((97 - n2) * " ") + "|")
    print((n2 * " ") + "|    CONTRAIBAL   |" + ((96 - n2) * " ") + "|")
    print((n2 * " ") + "|----@--------@---|" + ((96 - n2) * " ") + "|")
    print(115 * "-")

# aqui Funcion para limpiar la pantalla
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Variables iniciales
a = 0
b = 0

print("CARRERA DE BUSES!!!!!")
print("COTUC VS CONTRAIBAL")
time.sleep(3)
clear_screen()

# aqui inicia el audio cuando comienza la carrera
play_audio()

# Carrera de buses
while a < 97 and b < 97:
    c = randint(1, 2)
    if c == 1:
        a += 1
    else:
        b += 1

    clear_screen()
    buses(a, b)
    time.sleep(0.05)

# aqui detiene el audio al finalizar la carrera
stop_audio()

# con esto se Verifica quien gano
if a == 97:
    gano = "COTUC"
elif b == 97:
    gano = "CONTRAIBAL"

print(f"¡GANO {gano}!")
