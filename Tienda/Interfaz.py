import pprint
from .Tienda import ClientTypes, Tienda


class Interfaz:
    '''
    Esta Interfaz no esta terminada, en terminos de abstraccion.
    Fue hecha para separar un poco el codigo
    '''

    def __init__(self, Controller: Tienda):
        self.Controller = Controller

    def __printAllData(self, data):
        pprint.pprint(data)
        print()
        input("Presione Enter para continuar\n-> ")

    def headerUpdater(self):
        sesion = self.Controller.getCurrentSession()
        if(sesion):
            return f"\n\nSesion: {sesion}\n"
        else:
            return f"\n\nNo hay sesion de cliente activa\n"

    def login(self):
        selectedID = input(
            "Ingrese el id del cliente\n-> ")
        selectedUserType = input(
            f"""Ingrese el tipo de cliente
            {ClientTypes.PROFESSOR.value}: {ClientTypes.PROFESSOR.name}
            {ClientTypes.STUDENT.value}: {ClientTypes.STUDENT.name}
            {ClientTypes.BECA.value}: {ClientTypes.BECA.name}
            \n-> """)
        self.Controller.logIn(selectedID, ClientTypes(int(selectedUserType)))
        print()
        print()
        print()
        print("Sesion de Cliente Registrada!")
        print()
        self.__printAllData(
            f"{selectedID}, {ClientTypes(int(selectedUserType)).name}")

    def getSesion(self):
        print()
        print()
        print()
        print()
        self.__printAllData(f"{self.Controller.getCurrentSession()}")

    def logout(self):
        self.Controller.logOut()
        print()
        print()
        print()
        print("Sesion del cliente terminada")
        print()
        self.__printAllData("")

    def verProductos(self):
        current = self.Controller.getProducts()
        print()
        print()
        print()
        print("Productos disponibles")
        print()
        self.__printAllData(current)

    def agregarACarrito(self):
        selectedIdProduct = input(
            "Ingrese el id del producto\n-> ")
        selectedIdProductAmount = input(
            "Ingrese la cantidad a agregar al carrito\n-> ")
        self.Controller.addToCart(selectedIdProduct,int(selectedIdProductAmount))

        print()
        print()
        print()
        print("Productos agregados al carrito")
        print()
        self.__printAllData("")

    def retirarDeCarrito(self):
        selectedIdProduct = input(
            "Ingrese el id del producto\n-> ")
        selectedIdProductAmount = input(
            "Ingrese la cantidad a retirar del carrito\n-> ")
        self.Controller.removeFromCart(selectedIdProduct,int(selectedIdProductAmount))
        print()
        print()
        print()
        print("Productos retirados del carrito!")
        print()
        self.__printAllData("")
    
    def verCarrito(self):
        current = self.Controller.getCart()
        print()
        print()
        print()
        print("Carrito de Compras")
        print()
        self.__printAllData(current)

    def checkout(self):
        current = self.Controller.checkout()
        print()
        print()
        print()
        print("Realizando checkout")
        print()
        self.__printAllData(current)
