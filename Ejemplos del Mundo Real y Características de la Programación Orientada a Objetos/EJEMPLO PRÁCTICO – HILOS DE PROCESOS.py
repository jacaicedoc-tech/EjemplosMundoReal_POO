import threading
import time

def tarea(nombre, tiempo):
    print(f"Hilo {nombre} iniciado")
    for i in range(3):
        print(f"Hilo {nombre} ejecutando paso {i + 1}")
        time.sleep(tiempo)
    print(f"Hilo {nombre} finalizado")

# Creación de los hilos
hilo1 = threading.Thread(target=tarea, args=("A", 1))
hilo2 = threading.Thread(target=tarea, args=("B", 2))
hilo3 = threading.Thread(target=tarea, args=("C", 1.5))

# Inicio de los hilos
hilo1.start()
hilo2.start()
hilo3.start()

# Esperar a que los hilos finalicen
hilo1.join()
hilo2.join()
hilo3.join()

print("Todos los hilos han terminado su ejecución")