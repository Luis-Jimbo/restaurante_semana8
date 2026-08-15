# Sistema de Gestión de Restaurante - Semana 9

**Estudiante:** Luis Jimbo

## Descripción del Proyecto
Evolución del sistema de gestión para un restaurante, aplicando programación orientada a objetos y las principales estructuras de datos de Python de forma justificada.

## Estructura del Proyecto
* `restaurante_app/`
  * `modelos/`: Contiene `producto.py` y `usuario.py`.
  * `servicios/`: Contiene `restaurante.py` para la lógica del sistema.
  * `main.py`: Punto de ejecución e interfaz por consola.
* `README.md`: Documentación del proyecto.

## Uso de Estructuras de Datos
* **Lista (`list`):** Administra colecciones dinámicas de objetos `Producto` y `Usuario` dentro del servicio.
* **Tupla (`tuple`):** Mantiene de forma estable las opciones permitidas del menú principal.
* **Diccionario (`dict`):** Relaciona las opciones del menú con sus funciones respectivas (clave -> valor).
* **Conjunto (`set`):** Extrae automáticamente las categorías de los productos registrados eliminando duplicados.

## Instrucciones de Ejecución
1. Tener Python instalado.
2. Ejecutar en la terminal: `python main.py`