# Aaron - joel
# Mobile - Tech
# Tienda de celulares

"""Proyecto: “Mi Primera Empresa en Python”
Objetivo:
Crear un programa en Python que represente una empresa, utilizando las herramientas
básicas del lenguaje para gestionar productos, clientes y datos.
"""

# 3. Mensaje de bienvenida y variables
# ------------------------------------
print("¡Bienvenido a Mobile-Tech, tu tienda de celulares de confianza!")

nombre_empresa = "Mobile-Tech"
año_fundacion = 2024 
ingresos_mensuales = 50000.50 
es_internacional = True

# 4. Solicitar datos al usuario y conversión
# -----------------------------------------
nombre = input("Ingresa tu nombre: ")
# Conversión explícita a entero
try:
    edad = int(input("Ingresa tu edad: "))
except ValueError:
    print("Edad inválida. Se establecerá en 0.")
    edad = 0

producto = input("Ingresa el producto que deseas comprar (Ej: iPhone): ")

# 5. Operadores aritméticos, de comparación y lógicos
precio_base_producto = 999.00
impuesto_porcentaje = 0.16 # 16% de IVA

# Aritméticos: Suma, Multiplicación y Resta
precio_con_impuesto = precio_base_producto * (1 + impuesto_porcentaje) # Multiplicación para el 16% de IVA

# Aritméticos: Módulo (%) para saber si el precio es 'par' en la parte entera (solo por ejemplo)
es_precio_par = (int(precio_base_producto) % 2) == 0

# Aritméticos: División Entera 
unidades_por_caja = 10
cajas_necesarias = 100 // unidades_por_caja 

# Comparación:
es_mayor_de_edad = edad >= 18

# Lógico: Descuento del 10% si es mayor de 18 Y no es producto en oferta (simulado)
producto_en_oferta = False
descuento_porcentaje = 0.10 if es_mayor_de_edad and not producto_en_oferta else 0.00
precio_final = precio_con_impuesto - (precio_con_impuesto * descuento_porcentaje)

print("\n--- Resultados de Compra y Empresa ---")
print(f"Empresa: {nombre_empresa.upper()}")
print(f"Año de Fundación: {año_fundacion}")
print(f"Ingresos Anuales Aproximados: ${ingresos_mensuales * 12:.2f}") 

print(f"\nCliente: {nombre.capitalize()}")
print(f"Edad: {edad}")
print(f"Producto: {producto.startswith('iP')}")

print(f"Precio Base: ${precio_base_producto:.2f}")
print(f"Precio con Impuestos: ${precio_con_impuesto:.2f}")
print(f"Descuento aplicado: {descuento_porcentaje * 100}%")
print(f"Precio Final: ${precio_final:.2f}")

print(f"¿Es mayor de edad?: {es_mayor_de_edad}") 

# 6. Cadenas (strings) y métodos
# ------------------------------
print("\n--- Análisis de Frase (Actividad) ---")
frase_usuario = input("Por favor, ingresa una frase para analizar: ")

# Métodos de String
frase_mayus = frase_usuario.upper()
frase_minus = frase_usuario.lower() 
frase_capitalizada = frase_usuario.capitalize() 

# Slicing
primeros_cinco = frase_usuario[:5]

# Concatenación
analisis_concatenado = f"La frase analizada es: '{frase_usuario}'"

print(analisis_concatenado)
print(f"Longitud (len()): {len(frase_usuario)}") 
print(f"Primeros 5 caracteres (Slicing): {primeros_cinco}")
print(f"Conteo de 'a' (count()): {frase_minus.count('a')}") 
print(f"¿Es numérica (isnumeric()): {frase_usuario.isnumeric()}") 
print(f"¿Está en mayúsculas (isupper()): {frase_usuario.isupper()}")

# 7. Listas y métodos
productos = ["Samsung S23", "iPhone 15", "Xiaomi 13T"]
precios = [899.00, 1199.00, 699.00]

print("\n--- Gestión de Listas de Productos ---")
print(f"Lista inicial de productos: {productos}")

# Método append()
productos.append("Motorola")
precios.append(599.00)
print(f"Lista después de append(): {productos}")

# Método insert()
productos.insert(1, "Google Pixel ") # Inserta en la posición 1
precios.insert(1, 1099.00)
print(f"Lista después de insert() Pixel: {productos}")

# Método remove()
productos.remove("Samsung S23")
precios.pop(0)
print(f"Lista después de remove() Samsung: {productos}")

# Método pop() 
producto_eliminado = productos.pop()
precio_eliminado = precios.pop()
print(f"Producto eliminado con pop(): {producto_eliminado}")
print(f"Lista después de pop(): {productos}")

# Método sort() 
productos.sort()
print(f"Lista ordenada (sort()): {productos}")

# Método reverse()
productos.reverse()
print(f"Lista invertida (reverse()): {productos}")

# Método copy()
productos_copia = productos.copy()
print(f"Copia de productos: {productos_copia}")
