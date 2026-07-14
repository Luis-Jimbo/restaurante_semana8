# Carpeta: servicios | Archivo: restaurante.py

from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self) -> None:
        """
        Clase de servicio que administra las colecciones del sistema.
        Cumple con el principio de Responsabilidad Única (SRP).
        """
        # REQUISITO: Almacenar Producto y Bebida en una misma colección (Liskov/LSP)
        self._productos: list[Producto] = []
        self._clientes: list[Cliente] = []

    # ==========================================
    #           MÉTODOS PARA PRODUCTOS
    # ==========================================
    def registrar_producto(self, nuevo_producto: Producto) -> bool:
        """
        Registra un producto o bebida validando que el código no se repita.
        """
        # REQUISITO: Validar que no se repitan códigos de productos
        for prod in self._productos:
            if prod.codigo == nuevo_producto.codigo:
                print(f"❌ Error: Ya existe un producto registrado con el código '{nuevo_producto.codigo}'.")
                return False
        
        self._productos.append(nuevo_producto)
        print(f"✅ '{nuevo_producto.nombre}' registrado con éxito.")
        return True

    def listar_productos(self) -> None:
        """
        Muestra todos los productos y bebidas registrados en el sistema.
        Aplica Polimorfismo puro al llamar a mostrar_informacion().
        """
        if not self._productos:
            print("⚠️ No hay productos o bebidas en el menú.")
            return

        print("\n==========================================")
        print("          MENÚ DEL RESTAURANTE")
        print("==========================================")
        # REQUISITO: Polimorfismo sin usar condicionales para preguntar el tipo
        for prod in self._productos:
            prod.mostrar_informacion()
        print("==========================================")

    # ==========================================
    #           MÉTODOS PARA CLIENTES
    # ==========================================
    def registrar_cliente(self, nuevo_cliente: Cliente) -> bool:
        """
        Registra un cliente validando que la identificación sea única.
        """
        # REQUISITO: Validar que no se repitan identificaciones
        for cli in self._clientes:
            if cli.identificacion == nuevo_cliente.identificacion:
                print(f"❌ Error: Ya existe un cliente con la identificación '{nuevo_cliente.identificacion}'.")
                return False

        self._clientes.append(nuevo_cliente)
        print(f"✅ Cliente '{nuevo_cliente.nombre}' registrado con éxito.")
        return True

    def listado_clientes(self) -> None:
        """Muestra la lista de todos los clientes registrados."""
        if not self._clientes:
            print("⚠️ No hay clientes registrados todavía.")
            return

        print("\n==========================================")
        print("          CLIENTES REGISTRADOS")
        print("==========================================")
        for cli in self._clientes:
            cli.mostrar_informacion()
        print("==========================================")