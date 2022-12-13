import threading
import time

SC = 0
num_veces = 10

def P0():
    global SC, banderas
    while True:
        # uso de la sección crítica
        for i in range(num_veces):
            SC += 1
            print("Thread 0: SC =", SC)
            time.sleep(0.1)
        break       

def P1():
    global SC, banderas
    while True:
        # uso de la sección crítica
        if SC <= 8:
            SC += 10
            print("Thread 1: SC =", SC)
            time.sleep(0.1)
        break
            

t0 = threading.Thread(target=P0)
t1 = threading.Thread(target=P1)
t0.start()
t1.start()