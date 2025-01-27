# Proyecto: Simulador de Brazo Robótico con API de Control

## Descripción
Este proyecto es un simulador de brazo robótico controlado mediante una API desarrollada con FastAPI. El sistema permite mover articulaciones individuales, controlar el efector final, grabar trayectorias y ejecutarlas en un entorno virtual. Además, ofrece la posibilidad de integrarse con hardware físico, extendiendo su funcionalidad más allá de la simulación.

## Características Principales
- **Control de articulaciones**: Mueve articulaciones individuales del brazo robótico a ángulos deseados.
- **Movimientos cartesianos**: Especifica la posición del efector final en coordenadas (X, Y, Z).
- **Grabación de trayectorias**: Graba y almacena secuencias de movimientos.
- **Simulador virtual**: Visualiza el brazo robótico en un entorno virtual utilizando PyBullet.
- **Integración con hardware (opcional)**: Controla un brazo robótico físico mediante hardware compatible.

## Tecnologías Utilizadas
- **Lenguaje**: Python
- **Framework para la API**: FastAPI
- **Simulador**: PyBullet
- **Validación de datos**: Pydantic
- **Pruebas**: Pytest
