import threading
import time

lock = threading.Lock()
CONTADOR_COMPARTIDO = 0

def incrementarContador():
    global CONTADOR_COMPARTIDO
    with lock:
        valorTemporal = CONTADOR_COMPARTIDO
        time.sleep(0.001)
        CONTADOR_COMPARTIDO = valorTemporal + 1

hilos = []

for _ in range(100):
    hilo = threading.Thread(target = incrementarContador)
    hilo.start()
    hilos.append(hilo)

for hilo in hilos:
    hilo.join()

print(f"Valor final del contador compartido: {CONTADOR_COMPARTIDO}")