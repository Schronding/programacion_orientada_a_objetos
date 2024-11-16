### **Ejercicio 2: Simulación de Cajeros Automáticos (50 puntos)**

# Diseña un programa que simule el funcionamiento de cajeros automáticos utilizando programación orientada a objetos y multihilos.

# - Crea una clase `CuentaBancaria` con:
#  - Un atributo `saldo` inicializable en el constructor.
#  - Métodos `depositar(cantidad)` y `retirar(cantidad)` que modifiquen el saldo.
# - Implementa la clase `CajeroAutomatico`, que hereda de `threading.Thread` y recibe una instancia de `CuentaBancaria`.
#  - Cada cajero realizará una serie de operaciones (depósitos y retiros) aleatorias sobre la cuenta.
# - Utiliza mecanismos de sincronización para asegurar que las operaciones sobre el saldo sean seguras y evitar condiciones de carrera.
# - En el programa principal:
#  - Crea una instancia de `CuentaBancaria` con un saldo inicial.
#  - Crea y ejecuta 3 hilos de `CajeroAutomatico` que operen sobre la misma cuenta.
#  - Espera a que todos los hilos terminen y luego imprime el saldo final de la cuenta.

# **Puntos a considerar:**

# - Usa la clase `Lock` de `threading` para sincronizar el acceso al saldo.
# - Genera operaciones aleatorias utilizando el módulo `random`.

import threading
import random

class cuentaBancaria():
    def __init__(self, saldo):
        self.saldo = saldo
        self._lock = threading.Lock()

    def depositar(self, cantidad):
        with self._lock:
            self.saldo += cantidad

    def retirar(self, cantidad):
        with self._lock:
            self.saldo -= cantidad

class cajeroAutomatico():
    def __init__(self, cuenta):
        self.cuenta = cuenta


cuenta_estudihambre = cuentaBancaria(1000)
hilos = []

for index in range(6):
    if index % 2 == 0:
        hilos.append(threading.Thread(cuenta_estudihambre.depositar(random.randint(50, 500))))
    else:
        hilos.append(threading.Thread(cuenta_estudihambre.retirar(random.randint(50, 500))))

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()

print(cuenta_estudihambre.saldo)