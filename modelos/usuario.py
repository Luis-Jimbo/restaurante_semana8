class Usuario:
    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo

    def mostrar_informacion(self) -> None:
        print(f"👤 ID: {self.identificacion:<10} | Nombre: {self.nombre:<15} | Correo: {self.correo}")