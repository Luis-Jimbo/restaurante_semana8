import json
import os
from modelos.producto import Producto

class ArchivoServicio:
    def __init__(self, ruta_archivo: str = "datos/productos.json"):
        self.ruta_archivo = ruta_archivo

    def cargar_productos(self) -> list[Producto]:
        """Carga los productos desde el archivo JSON y los convierte en objetos Producto."""
        productos = []
        
        # Controlar FileNotFoundError si el archivo todavía no existe
        if not os.path.exists(self.ruta_archivo):
            return productos

        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                for item in datos:
                    try:
                        # Reconstruir el objeto Producto a partir del diccionario
                        producto = Producto(
                            codigo=item["codigo"],
                            nombre=item["nombre"],
                            categoria=item["categoria"],
                            precio=float(item["precio"])
                        )
                        productos.append(producto)
                    except (KeyError, ValueError) as e:
                        print(f"Advertencia: Se omitió un registro inválido o incompleto: {e}")
        
        except json.JSONDecodeError:
            print("Error: El archivo productos.json posee un formato JSON inválido.")
        except PermissionError:
            print("Error: No hay permisos suficientes para leer el archivo de datos.")
            
        return productos

    def guardar_productos(self, productos: list[Producto]) -> None:
        """Guarda la lista de objetos Producto en el archivo JSON."""
        try:
            # Asegurar que la carpeta datos exista
            os.makedirs(os.path.dirname(self.ruta_archivo), exist_ok=True)
            
            # Convertir cada objeto Producto a diccionario
            datos = [prod.a_diccionario() for prod in productos]
            
            with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
                
        except PermissionError:
            print("Error: No hay permisos suficientes para escribir en el archivo de datos.")
        except Exception as e:
            print(f"Ocurrió un error inesperado al guardar los productos: {e}")