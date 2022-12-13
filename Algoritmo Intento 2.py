import threading
import time

SC = 0
banderas = [False, False]
num_veces = 10 # si se utiliza 8 o más, no ocurre el proceso 2, si es menor, si ocurre debido a la exclusión mutua.

def Pi():
    global SC, banderas
    while True:
        while (banderas[1]):
                continue
        banderas[0] = True

        # uso de la sección crítica
        for i in range(num_veces):
            SC += 1
            print("Thread 0: SC =", SC)
            time.sleep(0.1)

        # condición de salida
        banderas[0] = False     

        break       

def Pj():
    global SC, banderas
    while True:
        while (banderas[0]):
            continue
        banderas[1] = True

        # uso de la sección crítica
        if SC <= 8:
            SC += 10
            print("Thread 1: SC =", SC)
            time.sleep(0.1)

        # condición de salida
        banderas[1] = False
        break

t0 = threading.Thread(target=Pi)
t1 = threading.Thread(target=Pj)

t0.start()
t1.start()