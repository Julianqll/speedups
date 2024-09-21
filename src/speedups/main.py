from tkinter import messagebox
from speedups.cpp_utils import compilar_programas, ejecutar_programa_secuencial, ejecutar_programa_paralelo, calcular_speedup
from speedups.graphs import graficar_speedup
from speedups.tkinter_utils import crear_interfaz

# Función que se ejecuta cuando se presiona el botón en la interfaz gráfica
def ejecutar(entry_datos, entry_hilos_inicial, entry_hilos_final, entry_intervalo):
    try:
        num_datos = int(entry_datos.get())
        hilos_inicial = int(entry_hilos_inicial.get())
        hilos_final = int(entry_hilos_final.get())
        intervalo = int(entry_intervalo.get()) if entry_intervalo.get() else 2

        if hilos_inicial <= 0 or hilos_final <= 0 or num_datos <= 0 or hilos_inicial > hilos_final:
            raise ValueError

        # 1. Ejecutar el programa secuencial 10 veces y obtener el tiempo promedio
        tiempo_secuencial_promedio = ejecutar_programa_secuencial(num_datos)

        # 2. Ejecutar el programa paralelo con diferentes números de hilos
        hilos = list(range(hilos_inicial, hilos_final + 1, intervalo))
        speedups = []

        for num_hilos in hilos:
            tiempo_paralelo_promedio = ejecutar_programa_paralelo(num_hilos, num_datos)
            speedup = calcular_speedup(tiempo_secuencial_promedio, tiempo_paralelo_promedio)
            speedups.append(speedup)
            print(f"Hilos: {num_hilos}, Speedup: {speedup}")

        # 3. Graficar los resultados
        graficar_speedup(hilos, speedups)

    except ValueError:
        messagebox.showerror("Error de entrada", "Por favor, ingrese valores válidos.")

# Función principal
def main():
    # Compilar los programas C++
    compilar_programas()

    # Crear la interfaz gráfica
    crear_interfaz(ejecutar)

if __name__ == "__main__":
    main()
