import matplotlib.pyplot as plt

# Función para graficar el speedup
def graficar_speedup(hilos, speedups):
    plt.plot(hilos, speedups, marker='o')
    plt.xticks(hilos)
    plt.yticks(speedups)
    plt.xlabel('Número de hilos')
    plt.ylabel('Speedup (valores reales)')
    plt.title('Speedup vs Número de hilos')
    plt.grid(True)
    plt.show()
