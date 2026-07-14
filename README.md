# Sistema de Gestión de Restaurante - Semana 8 (SOLID)

Proyecto desarrollado para aplicar principios de diseño de software y POO en Python.

## Estudiante: Luis Jimbo

## Principios SOLID Aplicados:
* **SRP (Responsabilidad Única):** Cada clase tiene una tarea clara; `Producto` y `Bebida` solo guardan datos, `Restaurante` gestiona listas y `main.py` maneja la interfaz.
* **OCP (Abierto/Cerrado):** Se implementó `Bebida` como una extensión mediante herencia sin modificar el código base del servicio.
* **LSP (Sustitución de Liskov):** Tanto `Producto` como `Bebida` se almacenan en la misma lista `_productos` y son tratados de forma polimórfica sin necesidad de verificar su tipo.

## Estructura del Proyecto:
* `modelos/`: Contiene las entidades (Producto, Bebida, Cliente).
* `servicios/`: Contiene la lógica administrativa (`Restaurante`).
* `main.py`: Punto de entrada y menú interactivo.

## Instrucciones de ejecución:
1. Asegúrese de tener instalado Python.
2. Ejecute el comando: `python main.py`
3. Siga las instrucciones del menú interactivo en la consola.

## Reflexión:
Diseñar proyectos bajo principios SOLID es fundamental para que el software sea mantenible, escalable y fácil de entender por otros desarrolladores, evitando el "código espagueti".