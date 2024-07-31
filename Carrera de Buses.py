import time
import os
from random import randint

def buses(n1, n2):
    print(115 * "-")
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

def clear_screen():
    # Comando para limpiar la pantalla en Windows 
    os.system('cls' if os.name == 'nt' else 'clear')

a = 0
b = 0
print("CARRERA DE BUSES!!!!!")
print("COTUC VS CONTRAIBAL")
time.sleep(3)
clear_screen()

while a < 97 and b < 97:
    c = randint(1, 2)
    if c == 1:
        a += 1
    else:
        b += 1

    clear_screen()
    buses(a, b)
    time.sleep(0.05)

if a == 97:
    gano = "COTUC"
elif b == 97:
    gano = "CONTRAIBAL"

print(f"¡GANO {gano}!")
