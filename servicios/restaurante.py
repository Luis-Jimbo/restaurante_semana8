from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class Restaurante:
    def __init__(self) -> None:
        # Inicializar el servicio de archivos para JSON
        self.archivo_servicio = ArchivoServicio()
        
        # LISTAS para colecciones dinámicas de objetos (cargadas desde el JSON)
        self._productos: list[Producto] = self.archivo_servicio.cargar_productos()
        self._usuarios: list[Usuario] = []

    # --- GESTIÓN DE PRODUCTOS ---
    def registrar_producto(self, producto: Producto) -> bool:
        for p in self._productos:
            if p.codigo == producto.codigo:
                print(f"❌ Error: Ya existe un producto con el código '{producto.codigo}'.")
                return False
        self._productos.append(producto)
        # Guardar cambios en el archivo JSON
        self.archivo_servicio.guardar_productos(self._productos)
        print(f"✅ Producto '{producto.nombre}' registrado con éxito.")
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        for p in self._productos:
            if p.codigo == codigo:
                return p
        return None

    def actualizar_producto(self, codigo: str, nuevo_nombre: str, nueva_categoria: str, nuevo_precio: float) -> bool:
        producto = self.buscar_producto(codigo)
        if producto:
            producto.nombre = nuevo_nombre
            producto.categoria = nueva_categoria
            producto.precio = nuevo_precio
            # Guardar cambios en el archivo JSON
            self.archivo_servicio.guardar_productos(self._productos)
            print(f"✅ Producto '{codigo}' actualizado correctamente.")
            return True
        print(f"❌ Error: Producto con código '{codigo}' no encontrado.")
        return False

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if producto:
            self._productos.remove(producto)
            # Guardar cambios en el archivo JSON
            self.archivo_servicio.guardar_productos(self._productos)
            print(f"✅ Producto '{codigo}' eliminado exitosamente.")
            return True
        print(f"❌ Error: No se encontró el producto a eliminar.")
        return False

    def listar_productos(self) -> None:
        if not self._productos:
            print("⚠️ No hay productos registrados.")
            return
        print("\n--- LISTA DE PRODUCTOS ---")
        for p in self._productos:
            p.mostrar_informacion()

    # --- GESTIÓN DE USUARIOS ---
    def registrar_usuario(self, usuario: Usuario) -> bool:
        for u in self._usuarios:
            if u.identificacion == usuario.identificacion:
                print(f"❌ Error: La identificación '{usuario.identificacion}' ya está registrada.")
                return False
        self._usuarios.append(usuario)
        print(f"✅ Usuario '{usuario.nombre}' registrado con éxito.")
        return True

    def listar_usuarios(self) -> None:
        if not self._usuarios:
            print("⚠️ No hay usuarios registrados.")
            return
        print("\n--- LISTA DE USUARIOS ---")
        for u in self._usuarios:
            u.mostrar_informacion()

    # --- CONJUNTO (SET) PARA CATEGORÍAS ÚNICAS ---
    def obtener_categorias_unicas(self) -> set[str]:
        # El set elimina automáticamente los elementos repetidos
        categorias: set[str] = {p.categoria for p in self._productos}
        return categorias