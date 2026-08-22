class Producto:
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float):
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.precio: float = precio

    def mostrar_informacion(self) -> None:
        print(f"📦 [{self.codigo}] {self.nombre:15} | Cat: {self.categoria:15} | Precio: ${self.precio:.2f}")

    def a_diccionario(self) -> dict:
        """Convierte el objeto Producto a un diccionario compatible con JSON."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio
        }