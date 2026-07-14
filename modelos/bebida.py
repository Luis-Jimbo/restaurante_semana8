# Carpeta: modelos | Archivo: bebida.py

# Importamos la clase base Producto
from modelos.producto import Producto

# Aplicamos HERENCIA: Bebida hereda de Producto
class Bebida(Producto):
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, tamano: str):
        """
        Clase hija que hereda de Producto.
        Agrega el atributo específico 'tamano' requerido por la guía.
        """
        # Inicializamos los atributos heredados de la clase padre usando super()
        super().__init__(codigo, nombre, categoria, precio)
        self.tamano: str = tamano

    def mostrar_informacion(self) -> None:
        """
        Sobrescribe el método mostrar_informacion de la clase base (Polimorfismo).
        Muestra la información del producto e incluye el tamaño específico de la bebida.
        """
        print(f"🥤 [{self.codigo}] {self.nombre:<18} | Cat: {self.categoria:<10} | Precio: ${self.precio:.2f} | Tamaño: {self.tamano}")