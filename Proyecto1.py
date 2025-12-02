# Aaron - joel
# Mobile - Tech
# Tienda de celulares

"""Usa un mensaje de bienvenida y crea variables como: nombre_empresa,
año_fundacion, ingresos_mensuales, es_internacional.
4. Pide datos al usuario: nombre, edad y producto. Convierte la edad a entero.
5. Usa operadores aritméticos (+ - * / % // **), de comparación (> < >= <= == !=) y
lógicos (and or not)."""

# Mensaje de bienvenida
print("¡Bienvenido a Mobile-Tech, tu tienda de celulares de confianza!")

# Variables
nombre_empresa = "Mobile-Tech"
año_creacion = 2025
ingresos_mensuales = 50000
es_internacional = True

# Solicitar datos al usuario
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
print(totalProducto)
producto = input("Ingresa el producto que deseas comprar: ")

# Operadores aritméticos
precio_producto = 950.50 # Precio fijo para el ejemplo de venta
descuento = 0.15  # 15% de descuento si el cliente es mayor de 18 años
precio_final = precio_producto - (precio_producto * descuento) if edad >= 18 else precio_producto

# Operadores de comparación y lógicos
es_mayor_de_edad = edad >= 18
puede_comprar = es_mayor_de_edad and producto != ""

# Mostrar resultados
print(f"Cliente: {nombre}")
print(f"Edad: {edad}")
print(f"Producto seleccionado: {producto}")
print(f"Precio final: ${precio_final}")
print("¿Puede comprar?:", "Sí" if puede_comprar else "No")


# Lista de productos
productos = ["Samsung ", "iPhone", "Xiaomi"]
precios = [799.99, 999.99, 599.99]
totalProducto =  productos + precios


# nuevas ofertas 
productos.add("Oppo")
print(productos)

# productos elimandos
productos.remove("Xiaomi")

# lista ordenada 
print(productos.sort())


# tupla 
producto_tuple = tuple()
print(producto_tuple)

 



