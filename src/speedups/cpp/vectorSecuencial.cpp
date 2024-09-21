#include <iostream>
#include <vector>
#include <random>
#include <chrono>  // Para medir el tiempo

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Uso: " << argv[0] << " <num_datos>" << std::endl;
        return 1;
    }

    // Obtener el número de datos desde los argumentos
    long long int num_datos = std::stoll(argv[1]);

    if (num_datos <= 0) {
        std::cerr << "El número de datos debe ser mayor a 0." << std::endl;
        return 1;
    }

    // Generador de números aleatorios
    std::random_device rd;  // Fuente de entropía
    std::mt19937 gen(rd()); // Generador Mersenne Twister
    std::uniform_int_distribution<> distrib(1, 100); // Distribución uniforme entre 1 y 100

    // Inicializamos los vectores con valores aleatorios
    std::vector<int> vec1(num_datos);
    std::vector<int> vec2(num_datos);

    // Llenamos los vectores con valores aleatorios
    for (long long int i = 0; i < num_datos; ++i) {
        vec1[i] = distrib(gen);
        vec2[i] = distrib(gen);
    }

    // Medir el tiempo de ejecución
    auto inicio_tiempo = std::chrono::high_resolution_clock::now();

    // Cálculo secuencial
    long long resultado_secuencial = 0; // Cambiamos a long long para evitar desbordamiento
    for (long long int i = 0; i < num_datos; ++i) {
        resultado_secuencial += static_cast<long long>(vec1[i]) * vec2[i];
    }

    // Medir el tiempo de finalización
    auto fin_tiempo = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duracion = fin_tiempo - inicio_tiempo;

    // Imprimir los resultados
    std::cout << "Resultado secuencial: " << resultado_secuencial << std::endl;
    std::cout << "Tiempo de ejecucion: " << duracion.count() << " segundos" << std::endl;

    return 0;
}
