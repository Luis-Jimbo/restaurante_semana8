# Carpeta: modelos | Archivo: cliente.py

class Cliente:
    def __init__(self, identificacion: str, nombre: str, correo: str):
        """
        Clase que representa a un cliente registrado en el restaurante.
        Cumple con el principio de Responsabilidad Única (SRP).
        """
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo

    def mostrar_informacion(self) -> None:
        """Muestra de manera ordenada los datos del cliente."""
        print(f"👤 ID: {self.identificacion:<10} | Nombre: {self.nombre:<18} | Correo: {self.correo}")