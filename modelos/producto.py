class Producto:
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.precio: float = precio

    def mostrar_informacion(self) -> None:
        print(f"📦 [{self.codigo}] {self.nombre:<15} | Cat: {self.categoria:<10} | Precio: ${self.precio:.2f}")