### **Ejercicio 1: Contador Concurrente (50 puntos)**

# Crea una clase `ContadorConcurrente` que herede de `threading.Thread`. Esta clase debe tener un atributo compartido llamado `contador`, ...
# ... inicializado en cero y común a todas las instancias de la clase. Cada hilo debe incrementar el contador en 1, un total de 1000 veces.

# - Implementa los mecanismos necesarios para evitar condiciones de carrera y asegurar que el valor final del contador sea correcto.
# - Crea y ejecuta 5 hilos de `ContadorConcurrente` de forma concurrente.
# - Al finalizar la ejecución de todos los hilos, imprime el valor final de `contador`, el cual debería ser 5000.

# **Puntos a considerar:**

# - Utiliza locks o semáforos para sincronizar el acceso al contador.
# - Asegúrate de que el atributo `contador` sea compartido entre todas las instancias.

import threading

contadorGlobal = 0

class contadorConcurrente:
    def __init__(self):
        self._lock = threading.Lock()

    def increment(self):
        global contadorGlobal
        for _ in range(1000):
            with self._lock:
                contadorGlobal += 1
            

contador1 = contadorConcurrente()
contador2 = contadorConcurrente()
contador3 = contadorConcurrente()
contador4 = contadorConcurrente()
contador5 = contadorConcurrente()

hilo1 = threading.Thread(target = contador1.increment)
hilo2 = threading.Thread(target = contador2.increment)
hilo3 = threading.Thread(target = contador3.increment)
hilo4 = threading.Thread(target = contador4.increment)
hilo5 = threading.Thread(target = contador5.increment)

hilos = [hilo1, hilo2, hilo3, hilo4, hilo5]

for hilo in hilos: 
    hilo.start()

for hilo in hilos: 
    hilo.join()

print(contadorGlobal)
