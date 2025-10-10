from src.db import producto_dao
from src.db import direccion_dao
from src.db import cliente_dao



def editar_nombre(cliente, nuevo_nombre: str):   
    print(f"\nNombre actual:{cliente.nombre} ")
    nuevo_nombre = input("Nuevo nombre: ")
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

def agregar_direccion(cliente):
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

    return direccion_dao.insertar_direccion(cliente.id, direccion)

def eliminar_direccion(cliente):
    direccion_id = input("Ingrese el numero de direccion que desee borrar: ")
    return direccion_dao.eliminar_direccion(cliente.id, direccion_id)


def realizar_pedidos(cliente):
    pass

def ver_productos_disponibles(cliente):
    return producto_dao.obtener_todos_los_productos()


def ver_mis_datos(cliente):
    print(f"\nDatos Personales\nNombre: {cliente.nombre}\nEmail: {cliente.email}\nRol: {cliente.rol.nombre}")
    cliente.ver_mis_direcciones()
    