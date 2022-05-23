import Tienda


def main():
    productos = [
        {"name": "Papas", "price": 1000},
        {"name": "Sopa", "price": 1500},
        {"name": "Chicle", "price": 300},
        {"name": "Pan", "price": 500},
        {"name": "Tomate", "price": 500},
        {"name": "Manzana", "price": 1200},
    ]
    tienda = Tienda.Tienda(productos)
    interfaz = Tienda.Interfaz(tienda)

    opciones = [
        {
            "name": "Salir del Programa",
            "function": lambda: None,
            "args": None
        },
        {
            "name": "Login Comprador",
            "function": interfaz.login,
            "args": None
        },
        {
            "name": "Logout Comprador",
            "function": interfaz.logout,
            "args": None
        },
        {
            "name": "Ver Productos",
            "function": interfaz.verProductos,
            "args": None
        },
        {
            "name": "Agregar Producto a Carrito",
            "function": interfaz.agregarACarrito,
            "args": None
        },
        {
            "name": "Retirar Producto de Carrito",
            "function": interfaz.retirarDeCarrito,
            "args": None
        },
        {
            "name": "Ver Carrito",
            "function": interfaz.verCarrito,
            "args": None
        },
        {
            "name": "Checkout",
            "function": interfaz.checkout,
            "args": None
        },
    ]
    Menu = Tienda.Menu(opciones)
    Menu.setHeaderUpdater(interfaz.headerUpdater)
    Menu.run()


if(__name__ == "__main__"):
    main()
