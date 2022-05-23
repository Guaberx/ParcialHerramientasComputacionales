
class Menu:
    def __init__(self, options) -> None:
        self.options = options
        self.prevSelection = -1
        self.endSelection = 0
        self.header = None

    def run(self):
        while self.prevSelection != self.endSelection:
            print("\n"*100)
            if(self.headerUpdater):
                self.header = self.headerUpdater()
            if(self.header):
                print(self.header)
            print(f"Seleccion Anterior {self.prevSelection}\n")
            try:
                self.mainLoop()
            except ValueError:
                self.printError(
                    f"Por favor ingrese un numero entero como opcion")
            except Exception as e:
                self.printError(f"{type(e).__name__}: {e}")
        print("Terminando Ejecucion del Programa!...")

    def mainLoop(self) -> int:
        for o in range(len(self.options)):
            print(f'{o}. {self.options[o]["name"]}')

        print()
        selection = -1
        # Guarda para asegurarse que la seleccion es valida en las options
        while selection >= len(self.options) or selection < 0:
            if(selection):
                if(isinstance(selection, int)):
                    selection = int(input("Seleccione una opcion\n-> "))

        # Ejecutar la funcion correspondiente
        current = self.options[selection]
        current["function"]() if current["args"] == None else current["function"](
            current["args"])
        # Update prevSelection
        self.prevSelection = selection

    def updateOptions(self, newOptions: list):
        self.options = newOptions

    def setHeader(self, newHeader: str):
        self.header = newHeader

    def setHeaderUpdater(self, headerUpdater: callable):
        self.headerUpdater = headerUpdater

    # Verifica si la opcion tiene el formato correct. De lo contrario crea una Excepcion
    def __optionVerifier(self, option: dict):
        if(not ("name" in option and "function" in option and "args" in option)):
            raise Exception(f"opcion no valida: {option}")
        if(not callable(option["function"])):
            raise Exception(
                f"option['function'] debe ser una funcion: {option['function']}")

    def printError(self, e):
        print()
        print()
        print("-------------------------------------------------------------")
        print("-------------------------------------------------------------")
        print(e)
        print("-------------------------------------------------------------")
        print("-------------------------------------------------------------")
        print()
        print()
        input("Presione Enter para continuar\n-> ")
