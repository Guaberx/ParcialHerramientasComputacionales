# ParcialHerramientasComputacionales

---

## Descripcion

Este programa realiza la simulacion de una tienda con varios productos. Es posible agregar varios productos con su respectivo nombre, cantidad y precio.

Cada cliente tiene una sesion a la cual esta asociada un carrito de compras.

El programa da solucion al problema con la funcion "checkout" en `Tienda.py`, que es el archivo encargado de la logica del negocio del programa. imprime ”El Rol con cedula Numero, debe pagar Valor por el producto Codigo” como se pide en el documento, al tener la sesion iniciada con algun usuario, agregar productos al carrito de compras y realizar el checkout.


---

## Indicaciones de Uso

- Para correr el programa ejecutar `python App.py` en la carpeta raiz.

- Cuando el programa este en ejecucion, mostrara una interfaz de consola con las opciones que permite. Ademas, Muestra en la primera linea, la sesion activa en ese momento o si no hay ninguna sesion de cliente aun y en la segunda linea, la opcion utilizada anteriormente (-1 si no se ha usado ninguna opcion)

```text
No hay sesion de cliente activa

Seleccion Anterior -1

0. Salir del Programa
1. Login Comprador
2. Logout Comprador
3. Ver Productos
4. Agregar Producto a Carrito
5. Retirar Producto de Carrito
6. Ver Carrito
7. Checkout
```

```text
Sesion: {'id': '123', 'clientType': <ClientTypes.PROFESSOR: 1>}

Seleccion Anterior 1

0. Salir del Programa
1. Login Comprador
2. Logout Comprador
3. Ver Productos
4. Agregar Producto a Carrito
5. Retirar Producto de Carrito
6. Ver Carrito
7. Checkout
```

- Es posible modificar los productos en App.py. Ahi, es donde se inicializan todos los datos del programa. Es decir, los productos y donde se inyecta la interfaz grafica.

---

## Extras

### Estas funciones son extra y no fueron tan rigurosamente probadas

- Es posible ver los productos disponibles en la tienda con la opcion "Ver productos"
- Es posible agregar productos a la tienda con la opcion "Agregar Productos"
