# Carpeta: modelos | Archivo: producto.py

class Producto:
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float):
        """
        Clase base que representa un producto general del restaurante.
        Se utilizan anotaciones de tipo para cumplir con los requisitos.
        """
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.precio: float = precio

    def mostrar_informacion(self) -> None:
        """Método base que será heredado y sobrescrito por las clases hijas."""
        print(f"📦 [{self.codigo}] {self.nombre:<18} | Cat: {self.categoria:<10} | Precio: ${self.precio:.2f}")