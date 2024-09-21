import os
import subprocess
import platform

# Ruta al directorio donde están los archivos C++
CPP_DIR = os.path.join(os.path.dirname(__file__), 'cpp')

# Función para compilar los programas C++
def compilar_programas():
    # Detectar el sistema operativo
    current_os = platform.system()

    try:
        # Comando de compilación para Windows
        if current_os == "Windows":
            print("Compilando en Windows...")
            # Compilar program1.cpp (sin pthread)
            subprocess.run(['g++', '-o', os.path.join(CPP_DIR, 'vectorParalelo'), os.path.join(CPP_DIR, 'vectorParalelo.cpp')], check=True)


        # Comando de compilación para Linux (con pthread)
        elif current_os == "Linux":
            print("Compilando en Linux con pthread...")
            # Compilar program1.cpp (con pthread para multihilos)
            subprocess.run(['g++', '-pthread', '-o', os.path.join(CPP_DIR, 'vectorParalelo'), os.path.join(CPP_DIR, 'vectorParalelo.cpp')], check=True)

        else:
            print(f"OS '{current_os}' no soportado para compilación automática.")
            return

        subprocess.run(['g++', '-o', os.path.join(CPP_DIR, 'vectorSecuencial'), os.path.join(CPP_DIR, 'vectorSecuencial.cpp')], check=True)

        print("Programas compilados exitosamente.")

    except subprocess.CalledProcessError as e:
        print(f"Error al compilar los programas: {e}")
        raise


# Función para ejecutar el programa secuencial
def ejecutar_programa_secuencial(num_datos):
    tiempos = []
    for _ in range(10):
        result = subprocess.run([os.path.join(CPP_DIR, 'vectorSecuencial'), str(num_datos)], capture_output=True, text=True)
        time = float(result.stdout.splitlines()[-1].split()[-2])
        tiempos.append(time)
    return sum(tiempos) / len(tiempos)

# Función para ejecutar el programa paralelo
def ejecutar_programa_paralelo(num_hilos, num_datos):
    tiempos = []
    for _ in range(10):
        result = subprocess.run([os.path.join(CPP_DIR, 'vectorParalelo'), str(num_hilos), str(num_datos)], capture_output=True, text=True)
        time = float(result.stdout.splitlines()[-1].split()[-2])
        tiempos.append(time)
    return sum(tiempos) / len(tiempos)

# Función para calcular el speedup
def calcular_speedup(tiempo_secuencial, tiempo_paralelo):
    return tiempo_secuencial / tiempo_paralelo
