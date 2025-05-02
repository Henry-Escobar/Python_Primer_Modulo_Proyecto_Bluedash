def mostrar_menu():
    while True:
        print("\nBienvenido a la tienda virtual 🛍️")
        print("¿Qué deseas hacer?\n")
        print("1. Ver catálogo")
        print("2. Agregar producto al carrito")
        print("3. Eliminar producto del carrito")
        print("4. Vaciar carrito")
        print("5. Mostrar carrito")
        print("6. Finalizar compra")
        print("7. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            mostrar_catalogo()
        elif opcion == "7":
            print("Hasta pronto 👋")
            break
        else:
            print("Opción no válida")


def mostrar_catalogo():
    catalogo = [
        {"codigo": "A001", "producto": "Pan", "precio": 1.50},
        {"codigo": "B203", "producto": "Leche", "precio": 3.80},
    ]
    print("\nCatálogo disponible:")
    for item in catalogo:
        print(
            f"Código: {item['codigo']} | Producto: {item['producto']} | Precio: S/{item['precio']:.2f}"
        )


mostrar_menu()
