from os import error
from src.db import producto_dao


def lista_productos_service(vendedor):
    productos = producto_dao.lista_productos(vendedor)

    if not productos:
      return  print("📭 No tenés productos agregados.")

    resultado = "\n📌 Tus Productos: \n"
    for i, d in enumerate(productos, start=1):
        resultado += f"""
🧾 Producto {i}
   🆔 ID: {d['id_producto']}
   🏷️ Nombre: {d['nombre']}
   📝 Descripción: {d['descripcion']}
   💲 Precio: ${d['precio']}
   📦 Stock disponible: {d['stock']}
"""
    return print(resultado)
     
    
def agregar_producto_service(vendedor):
        #nombre no puede estar vacio
        while True:
            nombre = input("🏷️ Nombre: ").strip()
            if nombre:
                break
            print("❌ El nombre no puede estar vacío. Inténtalo de nuevo.")

        descripcion = input("📝 Descripción: ").strip()

        #validacion para float
        while True:
            precio_input = input("💲  Precio: ").strip()
            try:
                precio = float(precio_input)
                if precio >= 0:
                    break
                print("❌ El precio no puede ser negativo. Inténtalo de nuevo.")
            except ValueError:
                print("❌ El precio debe ser un número válido. Inténtalo de nuevo.")

        #validacion stock 
        while True:
            stock_input = input("📦 Stock: ").strip()
            if stock_input.isdigit():
                stock = int(stock_input)
                break
            print("❌ Ingresa un número entero positivo")
            
        producto = {
            "nombre": nombre,
            "descripcion": descripcion,
            "precio": precio,
            "stock": stock,
            "id_usuario": vendedor.id
        }
        return producto_dao.agregar_producto_dao(vendedor,producto)

def editar_producto_service(vendedor):
        productos = producto_dao.lista_productos(vendedor)
        while True:
            id_input = input("Ingrese el ID del producto a editar: ").strip()
            if id_input.isdigit():
                id = int(id_input)
                break
            print("❌ Ingresa un número entero positivo")

        producto = None
        for i in productos:
            if i['id_producto'] == id:
                producto = i
                break
        if not producto:
            print("❌ Producto no encontrado.")
            return
            
        print("\n✏️ Dejá vacío cualquier campo que no quieras modificar.")

        nuevo_nombre = input(f"Nombre actual: {producto['nombre']} → Nuevo: ").strip()
        nueva_descripcion = input(f"Descripción actual: {producto['descripcion']} → Nueva: ").strip()
        nuevo_precio = input(f"Precio actual: {producto['precio']} → Nuevo: ").strip()
        nuevo_stock = input(f"Stock actual: {producto['stock']} → Nuevo: ").strip()

        
        if nuevo_nombre:
            producto["nombre"] = nuevo_nombre
        if nueva_descripcion:
            producto["descripcion"] = nueva_descripcion
        if nuevo_precio:
            try:
                precio = float(nuevo_precio)
                if precio >= 0:
                    producto["precio"] = precio
            except ValueError:
                print("❌ Precio inválido ignorado.")
        if nuevo_stock:
            if nuevo_stock.isdigit():
                producto["stock"] = int(nuevo_stock)

        if producto:
            print(vendedor,producto)
            producto_dao.editar_producto_dao(vendedor, producto)
            print("✅ Producto actualizado.")
        else:
            print("ℹ️ No se modificó ningún campo.")

def eliminar_producto_service(vendedor):
    productos = producto_dao.lista_productos(vendedor)
    while True:
        id_input = input("Ingrese el ID del producto a Eliminar: ").strip()
        if id_input.isdigit():
            id = int(id_input)
            break
        print("❌ Ingresa un número entero positivo")

    producto = None
    for i in productos:
        if i['id_producto'] == id:
            producto = i
            break
    if not producto:
        print("❌ Producto no encontrado.")
        return
    
    producto_dao.eliminar_producto_dao(vendedor,producto)
    