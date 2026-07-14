# Archivo: main.py | Punto de arranque del sistema

from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def mostrar_menu():
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("----------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("----------------------------------------")
    print("6. Salir")
    print("========================================")

if __name__ == "__main__":
    mi_restaurante = Restaurante()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("\n--- REGISTRAR PRODUCTO ---")
            cod = input("Código: ")
            nom = input("Nombre: ")
            cat = input("Categoría: ")
            pre = float(input("Precio: "))
            mi_restaurante.registrar_producto(Producto(cod, nom, cat, pre))
            
        elif opcion == "2":
            print("\n--- REGISTRAR BEBIDA ---")
            cod = input("Código: ")
            nom = input("Nombre: ")
            cat = input("Categoría: ")
            pre = float(input("Precio: "))
            tam = input("Tamaño (ej. 350ml): ")
            mi_restaurante.registrar_producto(Bebida(cod, nom, cat, pre, tam))
            
        elif opcion == "3":
            print("\n--- REGISTRAR CLIENTE ---")
            ide = input("ID/Cédula: ")
            nom = input("Nombre: ")
            cor = input("Correo: ")
            mi_restaurante.registrar_cliente(Cliente(ide, nom, cor))
            
        elif opcion == "4":
            mi_restaurante.listar_productos()
            
        elif opcion == "5":
            mi_restaurante.listado_clientes()
            
        elif opcion == "6":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida.")