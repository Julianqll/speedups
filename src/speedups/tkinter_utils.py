import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal y las entradas de texto
def crear_interfaz(ejecutar_callback):
    ventana = tk.Tk()
    ventana.title("Calculadora de Speedup")
    ventana.geometry("400x300")

    # Crear un frame para centrar el contenido
    frame = tk.Frame(ventana)
    frame.pack(expand=True)

    # Etiquetas y entradas de texto para los inputs
    tk.Label(frame, text="Cantidad de datos:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    entry_datos = tk.Entry(frame)
    entry_datos.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(frame, text="Número de hilos inicial:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    entry_hilos_inicial = tk.Entry(frame)
    entry_hilos_inicial.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(frame, text="Número de hilos final:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    entry_hilos_final = tk.Entry(frame)
    entry_hilos_final.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(frame, text="Intervalo (opcional, 2 por defecto):").grid(row=3, column=0, padx=10, pady=10, sticky="e")
    entry_intervalo = tk.Entry(frame)
    entry_intervalo.grid(row=3, column=1, padx=10, pady=10)

    # Botón para ejecutar el cálculo
    boton_ejecutar = tk.Button(frame, text="Calcular Speedup", command=lambda: ejecutar_callback(entry_datos, entry_hilos_inicial, entry_hilos_final, entry_intervalo))
    boton_ejecutar.grid(row=4, columnspan=2, padx=10, pady=20)

    # Asegurar que el contenido esté centrado
    ventana.grid_columnconfigure(0, weight=1)
    ventana.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)

    ventana.mainloop()
