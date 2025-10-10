from src.db.pedido_producto import pedido_producto_dao
from src.db import pedido_dao
from src.db import producto_dao
from src.db import direccion_dao
from src.db import cliente_dao



def editar_nombre_service(cliente):
    print(f"\nNombre actual:{cliente.nombre} ")
    while True:
        nuevo_nombre = input("🏷️ Nombre: ").strip()
        if nuevo_nombre:
            break
        print("❌ El nombre no puede estar vacío. Inténtalo de nuevo.")

    return cliente_dao.actualizar_nombre(cliente, nuevo_nombre)

def ver_mis_direcciones(cliente):
    direcciones = direccion_dao.obtener_direcciones_por_usuario(cliente.id)
 
    if not direcciones:
      return  print("📭 No tenés direcciones registradas.")

    resultado = "\n📌 Tus direcciones registradas:\n"
    for i, d in enumerate(direcciones, start=1):
        resultado += f"""
🗂️ Dirección {d["id_direccion"]}
   🏠 Calle: {d['calle']} {d['numero']}
   🌆 Localidad: {d['localidad']}
   🗺️ Provincia: {d['provincia']}
   📮 Código Postal: {d['codigo_postal']}
"""
    return print(resultado)

def agregar_direccion_service(cliente):
    print("\n📬 Ingresá los datos de tu nueva dirección:")
    calle = input("🏠 Calle: ").strip()
    numero = input("numero: ").strip()
    localidad = input("🌆 Localidad: ").strip()
    provincia = input("🗺️ Provincia: ").strip()
    codigo_postal = input("🌎 C.P: ").strip()

    direccion = {
       "calle":   calle,
        "numero": numero,
        "localidad":localidad,
        "provincia":provincia,
        "codigo_postal":codigo_postal
    }

    return direccion_dao.agregar_direccion_dao(cliente.id, direccion)

def eliminar_direccion_service(cliente):
    direccion_id = input("Ingrese el numero de direccion que desee borrar: ")
    return direccion_dao.eliminar_direccion_dao(cliente.id, direccion_id)

def realizar_pedidos(cliente):
    productos = producto_dao.obtener_todos_los_productos()
    if not productos:
        print("ℹ️ No hay productos disponibles.")
        return
    
    print("\n🛒 Productos disponibles:")
    for p in productos:
        print(f"{p['id_producto']}️⃣ {p['nombre']} - ${p['precio']} (Stock: {p['stock']})")

    carrito = []
    while True:
        id_input = input("👉  Ingresá el ID del producto (o ENTER para finalizar) ").strip()
        if not id_input:
            break
        if not id_input.isdigit():
            print("❌ ID inválido.")
            continue

        id_producto = int(id_input)
        producto = next((p for p in productos if p['id_producto'] == id_producto), None)
        if not producto:
            print("❌ Producto no encontrado.")
            continue
    
        cantidad_input = input(f"🧮 ¿Cuántas unidades de '{producto['nombre']}'?: ").strip()
        if not cantidad_input.isdigit():
            print("❌ Cantidad inválida.")
            continue

        cantidad = int(cantidad_input)
        if cantidad > producto['stock']:
            print("⚠️ Stock insuficiente.")
            continue

        carrito.append({'id_producto': id_producto, 'cantidad': cantidad, 'precio': producto['precio']})

    if not carrito:
        print("ℹ️ No se seleccionaron productos.")
        return
    
    cantidad_total = sum(item['cantidad'] for item in carrito)
    id_pedido = pedido_dao.crear_pedido(cliente, cantidad_total)
    if not id_pedido:
        print("❌ No se pudo crear el pedido.")
        return

    for item in carrito:
        pedido_producto_dao(id_pedido, item['id_producto'], item['cantidad'])
        producto_dao.descontar_stock(item['id_producto'], item['cantidad'])

    print(f"\n✅ Pedido #{id_pedido} creado con éxito.")
    total = sum(item['cantidad'] * item['precio'] for item in carrito)
    print(f"💰 Total: ${total:.2f}")

def productos_disponibles_service(cliente):
    print("🛒 Productos disponibles:")
    productos = producto_dao.obtener_todos_los_productos()
    hay_stock = False
    print("🛍️  Productos:")
    for producto in productos:
        if producto['stock'] > 0:
            print(f"-Nombre: {producto['nombre']} | Decripcion: {producto['descripcion']} |  Precio: ${producto['precio']} | STOCK: {producto['stock']}")
            hay_stock = True
    if not hay_stock:
        print("⚠️ No hay productos disponibles en este momento.")
    
def mis_pedidos_service(cliente):
    pedidos = pedido_dao.obtener_pedidos_con_detalle(cliente)
    
    if not pedidos:
      return  print("ℹ️ No se encontraron pedidos.")

    print("\n📦 Tus pedidos:")
    pedido_actual = None
    total_pedido = 0

    for fila in pedidos:
        if fila['id_pedido'] != pedido_actual:
            if pedido_actual is not None:
                print(f"   💰 Total del pedido: ${total_pedido:.2f}\n")
            pedido_actual = fila['id_pedido']
            total_pedido = 0
            print(f"🧾 Pedido #{fila['id_pedido']} - Fecha: {fila['fecha_pedido']}")

        print(f"   🛒 {fila['producto']} x{fila['cantidad']} → ${fila['precio']} c/u → Total: ${fila['total_por_producto']}")
        total_pedido += fila['total_por_producto']

    print(f"   💰 Total del pedido: ${total_pedido:.2f}\n")

def ver_datos_service(cliente):
    print(f"\nDatos Personales\nNombre: {cliente.nombre}\nEmail: {cliente.email}\nRol: {cliente.rol.nombre}")
    ver_mis_direcciones(cliente)
    