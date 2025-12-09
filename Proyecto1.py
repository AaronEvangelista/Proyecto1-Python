# Team Aaron - Joel
# Mobile - Tech
# Tienda de celulares

# 3. Mensaje de bienvenida y variables

print("\n¡Bienvenido a Mobile-Tech, tu tienda de celulares de confianza!\n")

nombre_empresa = "Mobile-Tech"
año_fundacion = 2024 
ingresos_mensuales = 50000.50 
es_internacional = True

# 4. Solicitar datos al usuario y conversión

nombre = input("Ingresa tu nombre: ")

# Conversión explícita a entero
edad = int(input("Ingresa tu edad: "))

# Validación de edad con operador de comparación y condicionales:
if edad >= 18:
    es_mayor_de_edad = True
    print("¡Eres mayor de edad! Puedes continuar con tu compra.")   
else:
    es_mayor_de_edad = False
    print(f"Lo sentimos {nombre.capitalize()}, no eres mayor de edad.")
    exit() # Salir del programa si no es mayor de edad

producto = input("Ingresa el producto que deseas comprar (Ej: iphone): ")
print(f"\nGracias {nombre.capitalize()}, estamos procesando tu compra del producto {producto.capitalize()}..!!\n")

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
print(f"Producto: {producto.upper()}") # la primera letra en mayúscula 

print(f"Precio Base: ${precio_base_producto:.2f}")
print(f"Precio con Impuestos: ${precio_con_impuesto:.2f}")
print(f"Descuento aplicado: {descuento_porcentaje * 100}%")
print(f"Precio Final: ${precio_final:.2f}")



# 6. Cadenas (strings) y métodos y petición de frase al usuario
frase_usuario = input("Por favor, ingresa un comentario: ")

# Métodos de String
frase_mayus = frase_usuario.upper()
frase_minus = frase_usuario.lower() 
frase_capitalizada = frase_usuario.capitalize() 

# Slicing
primeros_cinco = frase_usuario[:5]

# Concatenación
frase_concatenada = frase_usuario + " - Gracias por tu comentario."
print(f"Longitud (len()): {len(frase_usuario)}") 
print(f"Primeros 5 caracteres (Slicing): {primeros_cinco}")
print(f"Conteo de 'a' (count()): {frase_minus.count('a')}") 
print(f"¿Es numérica (isnumeric()): {frase_usuario.isnumeric()}") 
print(f"¿Está en mayúsculas (isupper()): {frase_usuario.isupper()}")

# 7. Listas y métodos
productos = ["Samsung S23", "iPhone 15", "Xiaomi 13T", "OnePlus 11"]
precios = [899.00, 1199.00, 699.00]

print("\n--- Creación de Listas de Productos ---")
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


# Lo comentamos porque clear() deja vacía toda la lista
# Metodo clear()
#productos.clear()
#print(f"Lista después de clear(): {productos}")

# Método sort() 
productos.sort()
print(f"Lista ordenada (sort()): {productos}")

# Método reverse()
productos.reverse()
print(f"Lista invertida (reverse()): {productos}")

# Método copy()
productos_copia = productos.copy()
print(f"Copia de productos: {productos_copia}")

# Crea al menos una tupla relacionada con la empresa. Usa count(), index(),concatenación y conversión lista↔tupla.
# 8. Tuplas y métodos
print("\n--- Creación de Tuplas ---")
marcas_disponibles = ("Samsung", "Apple", "Xiaomi", "OnePlus", "Google")
print(f"Tupla inicial de marcas: {marcas_disponibles}")
# Método count()
conteo_apple = marcas_disponibles.count("Apple")
print(f"Número de veces que 'Apple' aparece en la tupla: {conteo_apple}")
# Método index()
indice_xiaomi = marcas_disponibles.index("Xiaomi")
print(f"Índice de 'Xiaomi' en la tupla: {indice_xiaomi}")
# Concatenación
nuevas_marcas = ("Motorola", "Nokia")
todas_marcas = marcas_disponibles + nuevas_marcas
print(f"Tupla después de concatenación: {todas_marcas}")
# Conversión lista ↔ tupla
lista_marcas = list(marcas_disponibles)
tupla_desde_lista = tuple(lista_marcas)
print(f"Tupla convertida desde lista: {tupla_desde_lista}")


"""Crea al menos un set con datos relacionados con la empresa. Usa add(), remove(),
union(), difference(), clear() e in."""
# 9. Sets y métodos
print("\n--- Creación de Sets ---")
categorias = {"Smartphones", "Accesorios", "Tabletas"}
print(f"Set inicial de categorías: {categorias}")
# Método add()
categorias.add("Wearables")
print(f"Set después de add(): {categorias}")
# Método remove()
categorias.remove("Tabletas")
print(f"Set después de remove(): {categorias}")
# Método union()
otras_categorias = {"Laptops", "Desktops"}
todas_categorias = categorias.union(otras_categorias)
print(f"Set después de union(): {todas_categorias}")