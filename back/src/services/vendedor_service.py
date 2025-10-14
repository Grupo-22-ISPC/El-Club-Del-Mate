from src.utils.validation import solicitar_float_positivo, solicitar_numero_positivo, solicitar_texto_no_vacio
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
    nombre = solicitar_texto_no_vacio("🏷️ Nombre: ")
    descripcion = input("📝 Descripción: ").strip()
    precio = solicitar_float_positivo("💲 Precio: ")
    stock = solicitar_numero_positivo("📦 Stock: ")
            
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
        id = solicitar_numero_positivo("Ingrese el ID del producto a editar: ")

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
            producto_dao.editar_producto_dao(vendedor, producto)
            print("✅ Producto actualizado.")
        else:
            print("ℹ️ No se modificó ningún campo.")

def eliminar_producto_service(vendedor):
    productos = producto_dao.lista_productos(vendedor)
    id = solicitar_numero_positivo("Ingrese el ID del producto a Eliminar: ")

    producto = None
    for i in productos:
        if i['id_producto'] == id:
            producto = i
            break
    if not producto:
        print("❌ Producto no encontrado.")
        return
    
    producto_dao.eliminar_producto_dao(vendedor,producto)
    