# Calculadora de Speedup

Este proyecto permite calcular el **speedup** de dos programas en C++ que se ejecutan de manera secuencial y paralela. Además, incluye una interfaz gráfica con **Tkinter** para ingresar los parámetros, ejecutar los programas y graficar los resultados utilizando **Matplotlib**.

## Requisitos Previos

Asegúrate de tener instalados los siguientes requisitos:

- **Python 3.11** o superior
- **Poetry** para la gestión de dependencias
- Un compilador de C++ (como `g++`)

## Instalación de Poetry

Si no tienes **Poetry** instalado, puedes hacerlo siguiendo las instrucciones a continuación:

### En Linux/macOS:

```bash
curl -sSL https://install.python-poetry.org | python3
```

### En Windows:

```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```
## Clonar el repositorio
Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/Julianqll/speedups.git
cd speedups
```
## Instalación del proyecto

Una vez clonado el proyecto, puedes usar Poetry para instalar las dependencias del proyecto y configurar el entorno virtual.

-  Instalar las dependencias:
```bash
poetry install
```

- Activar el entorno virtual:

Para activar el entorno virtual gestionado por Poetry, ejecuta:
```bash
poetry shell
```
## Ejecución del programa

Para ejecutar el programa:
```bash
poetry run run-project
```

- En caso existe alguna excepción puede volver a correr el comando: 
```bash
poetry install
```
