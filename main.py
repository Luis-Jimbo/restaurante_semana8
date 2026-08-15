from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

def mostrar_menu() -> None:
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE          ")
    print("========================================")
    print("1. Registrar producto")
    print("2. Buscar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Listar productos")
    print("----------------------------------------")
    print("6. Registrar usuario")
    print("7. Listar usuarios")
    print("----------------------------------------")
    print("8. Mostrar categorías únicas")
    print("9. Salir")
    print("========================================")

def ejecutar_registrar_producto(restaurante: Restaurante) -> None:
    print("\n--- REGISTRAR PRODUCTO ---")
    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    categoria = input("Categoría: ").strip()
    try:
        precio = float(input("Precio: "))
        producto = Producto(codigo, nombre, categoria, precio)
        restaurante.registrar_producto(producto)
    except ValueError:
        print("❌ Error: Ingrese un valor numérico válido para el precio.")

def ejecutar_buscar_producto(restaurante: Restaurante) -> None:
    print("\n--- BUSCAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto a buscar: ").strip()
    p = restaurante.buscar_producto(codigo)
    if p:
        print("✅ ¡Producto encontrado!")
        p.mostrar_informacion()
    else:
        print("❌ Producto no encontrado.")

def ejecutar_actualizar_producto(restaurante: Restaurante) -> None:
    print("\n--- ACTUALIZAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto a actualizar: ").strip()
    p = restaurante.buscar_producto(codigo)
    if p:
        print(f"Producto actual: {p.nombre} (${p.precio:.2f})")
        nuevo_nombre = input("Nuevo nombre: ").strip()
        nueva_cat = input("Nueva categoría: ").strip()
        try:
            nuevo_precio = float(input("Nuevo precio: "))
            restaurante.actualizar_producto(codigo, nuevo_nombre, nueva_cat, nuevo_precio)
        except ValueError:
            print("❌ Error: El precio debe ser un número.")
    else:
        print("❌ No se puede actualizar, el código no existe.")

def ejecutar_eliminar_producto(restaurante: Restaurante) -> None:
    print("\n--- ELIMINAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto a eliminar: ").strip()
    restaurante.eliminar_producto(codigo)

def ejecutar_registrar_usuario(restaurante: Restaurante) -> None:
    print("\n--- REGISTRAR USUARIO ---")
    ide = input("ID / Cédula: ").strip()
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()
    usuario = Usuario(ide, nombre, correo)
    restaurante.registrar_usuario(usuario)

def ejecutar_mostrar_categorias(restaurante: Restaurante) -> None:
    print("\n--- CATEGORÍAS ÚNICAS (Uso de Conjunto / Set) ---")
    categorias = restaurante.obtener_categorias_unicas()
    if not categorias:
        print("⚠️ No hay categorías registradas todavía.")
    else:
        for cat in categorias:
            print(f"🏷️ - {cat}")

if __name__ == "__main__":
    restaurante = Restaurante()

    # TUPLA: Opciones estables del menú
    opciones_validas: tuple[str, ...] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

    # DICCIONARIO: Relaciona cada opción con su función (clave -> valor)
    acciones_menu = {
        "1": lambda: ejecutar_registrar_producto(restaurante),
        "2": lambda: ejecutar_buscar_producto(restaurante),
        "3": lambda: ejecutar_actualizar_producto(restaurante),
        "4": lambda: ejecutar_eliminar_producto(restaurante),
        "5": lambda: restaurante.listar_productos(),
        "6": lambda: ejecutar_registrar_usuario(restaurante),
        "7": lambda: restaurante.listar_usuarios(),
        "8": lambda: ejecutar_mostrar_categorias(restaurante)
    }

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion not in opciones_validas:
            print("❌ Opción inválida. Intente de nuevo.")
            continue

        if opcion == "9":
            print("\n👋 ¡Gracias por usar el sistema del restaurante! Hasta luego.")
            break

        acciones_menu[opcion]()