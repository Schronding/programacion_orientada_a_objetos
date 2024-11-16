import threading
import time

def espera_inconclusa():
    time.sleep(5)
    print("termino la espera de 5 segundos")
    return True

#ejecutado = espera_inconclusa()

def espera_paciente(string):
    executed = string.join()
    if executed == 'True' or executed == True:
        print("La espera valio la pena")

hilo_independiente = threading.Thread(target = espera_inconclusa)
hilo_dependiente = threading.Thread(target = espera_paciente, args = (   str(hilo_independiente.is_alive()))   )

hilo_independiente.start()
hilo_dependiente.start()

hilo_independiente.join(timeout = 6)
hilo_dependiente.join(timeout = 3)

print(f" el hilo dependiente esta corriendo? {hilo_dependiente.is_alive()}")
print(f" el hilo independiente esta corriendo? {hilo_independiente.is_alive()}")
