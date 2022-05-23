from enum import Enum, unique, auto

# Tipos de estados que puede tener un cupo en el parqueadero
# Python no tiene Enums por defecto, por lo que es necesario utilizar una libreria que viene nativamente con python


@unique
class ClientTypes(Enum):
    PROFESSOR = auto()
    STUDENT = auto()
    BECA = auto()

# La siguiente linea muestra otra manera de utilizarlo
# cupoEstados = Enum("ESTADO", "PARQUEADO DESPARQUEADO PAGADO")


class Tienda:
    def __init__(self, products: list[object] = [], idTienda: str = "0") -> None:
        '''
        products es un diccionario de objetos que representan un producto
        cada objeto se identifica por un id unico

        Este constructor se encarga de crear ids unicos para los productos,
        por lo que solo es necesario pasar una lista de productos con nombre, precio y stock

        cada producto tiene la siguiente representacion
        products:{
            "id":{ # String, Id unico del producto
                "name": "Nombre del producto", # String, Nombre del producto
                "price": 123, # Integer, Precion unitario del producto
                "stock": 123 # Integer, Cantidad en stock del producto
            },
            .
            .
            .
        }

        En este caso. La aplicacion persiste el carrito de los usuarios (En memoria)

        '''
        # Se utiliza para diferenciar productos unicos. Cada vez que se agrega un producto, este id incrementa
        self.idProducts = 0
        self.products = {}
        self.idStore = idTienda
        for p in products:
            self.addProduct(p)

        # Representa la sesion activa del comprador actual i.e.
        # En este caso es un objeto con la cedula y el tipo de cliente (profesor, estudiante)
        self.currentSession = {'id': None, 'clientType': None}
        self.carts = {}  # El carrito de compras de los compradores. Cada carrito se identifica por su cedula

    def isSessionActive(self) -> bool:
        return self.currentSession['id'] != None and self.currentSession['clientType'] != None

    def checkSesionActive(self):
        if(not self.isSessionActive()):
            raise Exception('No hay sesion de usuario activa')
    
    def checkCart(self):
        self.checkSesionActive()
        if(not self.currentSession['id'] in self.carts):
            self.carts[self.currentSession['id']] = {}

    def getCurrentSession(self):
        return self.currentSession if self.currentSession['id'] else None

    def logIn(self, idUser: int, clientType: ClientTypes):
        self.currentSession = {'id': idUser, 'clientType': clientType}

    def logOut(self):
        self.currentSession = {'id': None, 'clientType': None}

    def addProduct(self, newProduct: object) -> None:
        newProductId = self.idStore + str(self.idProducts)
        self.idProducts += 1
        self.products[newProductId] = newProduct

    def getProducts(self):
        return self.products

    def updateProductStock(self, idProduct: str, newStock: int) -> int:
        self.products[idProduct]['stock'] = newStock
        return self.products[idProduct]['stock']

    def addToProductStock(self, idProduct: str, newStock: int) -> int:
        self.products[idProduct]['stock'] += newStock
        return self.products[idProduct]['stock']

    def addToCart(self, productId, amount):
        self.checkSesionActive()

        # Se verifica si existe el carrito. si no, se crea
        if(not self.currentSession['id'] in self.carts):
            self.carts[self.currentSession['id']] = {}
        # Se verifica si existe el producto en el carrito. si no, se crea
        if(not productId in self.carts[self.currentSession['id']]):
            self.carts[self.currentSession['id']][productId] = amount
        # En caso de que ya se hayan agregado productos antes, se agregan al carrito
        else:
            self.carts[self.currentSession['id']][productId] += amount

    def removeFromCart(self, productId, amount):
        self.checkSesionActive()

        # Se verifica si existe el carrito.
        if(not self.currentSession['id'] in self.carts):
            raise Exception('El cliente no tiene un carrito')
        # Se verifica si existe el producto en el carrito.
        if(not productId in self.carts[self.currentSession['id']]):
            raise Exception('El cliente no tiene este producto en el carrito')
        # Se modifica la cantidad en el carrito
        else:
            # Se verifica de que hayan suficientes productos para quitar
            if(self.carts[self.currentSession['id']][productId] - amount < 0):
                raise Exception(
                    'No se puede quitar mas productos de los que hay en el carrito')
            self.carts[self.currentSession['id']][productId] -= amount

    def getCart(self):
        self.checkSesionActive()
        self.checkCart()
        return self.carts[self.currentSession['id']]

    def checkout(self) -> int:
        '''
        Retorna el calculo de todos los productos en el carrito, en un mensaje especificado en el parcial
        y el carrito

        ”El Rol con cedula Numero, debe pagar Valor por el producto Codigo”

        Actualiza el carrito del cliente dejando todo en 0
        '''
        # Calcular Pago total
        self.checkSesionActive()
        currentCart = self.carts[self.currentSession['id']]
        total = 0
        for i in currentCart:
            total += currentCart[i] * self.products[i]['price']

        # Aplicar descuento
        descuento = 0
        if(self.currentSession['clientType'] == ClientTypes.PROFESSOR):
            descuento = .2
        if(self.currentSession['clientType'] == ClientTypes.STUDENT):
            descuento = .3
        if(self.currentSession['clientType'] == ClientTypes.BECA):
            descuento = .5
        totalConDescuento = total * (1-descuento)

        # Retornar resultado
        message = f"El {self.currentSession['clientType'].name} con cedula {self.currentSession['id']}, debe pagar {totalConDescuento} por los productos"
        return message, self.carts[self.currentSession['id']]
