#include <iostream>
#include <thread>
#include <vector>
#include <mutex>
#include <random>
#include <chrono>  // Para medir el tiempo

// Mutex para sincronización
std::mutex mtx;
long long int resultado_paralelo = 0;

// Función para calcular una parte del producto escalar
void calcular_producto(const std::vector<int>& vec1, const std::vector<int>& vec2, long long int inicio, long long int fin) {
    long long int suma_parcial = 0;
    for (long long int i = inicio; i < fin; ++i) {
        suma_parcial += vec1[i] * vec2[i];
    }
    // Sección crítica
    std::lock_guard<std::mutex> lock(mtx);
    resultado_paralelo += suma_parcial;
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Uso: " << argv[0] << " <num_hilos> <num_datos>" << std::endl;
        return 1;
    }

    // Obtener el número de hilos desde los argumentos
    int num_hilos = std::stoi(argv[1]);

    // Obtener el número de datos desde los argumentos
    long long int num_datos = std::stoll(argv[2]);

    if (num_datos <= 0) {
        std::cerr << "El número de datos debe ser mayor a 0." << std::endl;
        return 1;
    }

    // Generador de números aleatorios
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> distrib(1, 100); // Distribución uniforme entre 1 y 100

    // Inicializamos los vectores con valores aleatorios
    std::vector<int> vec1(num_datos);
    std::vector<int> vec2(num_datos);

    for (long long int i = 0; i < num_datos; ++i) {
        vec1[i] = distrib(gen);
        vec2[i] = distrib(gen);
    }

    // Definir el rango que manejará cada hilo
    long long int rango = num_datos / num_hilos;

    // Medir el tiempo de ejecución
    auto inicio_tiempo = std::chrono::high_resolution_clock::now();

    // Arreglo de hilos
    std::vector<std::thread> hilos;

    // Crear y lanzar los hilos
    for (int i = 0; i < num_hilos; ++i) {
        long long int inicio = i * rango;
        long long int fin = (i == num_hilos - 1) ? num_datos : (i + 1) * rango;
        hilos.emplace_back(calcular_producto, std::ref(vec1), std::ref(vec2), inicio, fin);
    }

    // Esperar a que todos los hilos terminen
    for (auto& hilo : hilos) {
        hilo.join();
    }

    // Medir el tiempo de finalización
    auto fin_tiempo = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duracion = fin_tiempo - inicio_tiempo;

    // Imprimir los resultados
    std::cout << "Resultado paralelo: " << resultado_paralelo << std::endl;
    std::cout << "Tiempo de ejecucion: " << duracion.count() << " segundos" << std::endl;

    return 0;
}
