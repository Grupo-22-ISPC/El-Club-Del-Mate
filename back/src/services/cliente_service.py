from src.db import direccion_dao
from src.db import cliente_dao


def ver_mis_datos(cliente):
    return {
        "nombre": cliente.nombre,
        "email": cliente.email,
        "rol": cliente.rol.nombre
    }

def editar_nombre(cliente, nuevo_nombre: str):    
    return cliente_dao.actualizar_nombre(cliente, nuevo_nombre)

def ver_mis_direcciones(cliente):
    direcciones = direccion_dao.obtener_direcciones_por_usuario(cliente.id)
 
    if not direcciones:
        return "📭 No tenés direcciones registradas."

    resultado = "\n📌 Tus direcciones registradas:\n"
    for i, d in enumerate(direcciones, start=1):
        resultado += f"""
🗂️ Dirección {d["id_direccion"]}
   🏠 Calle: {d['calle']} {d['numero']}
   🌆 Localidad: {d['localidad']}
   🗺️ Provincia: {d['provincia']}
   📮 Código Postal: {d['codigo_postal']}
"""
    return resultado



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
    # resultado = cliente.agregar_direccion(direccion)

    # if resultado:
    #     print("✅ Dirección agregada correctamente.")
    # else:
    #     print("❌ Hubo un problema al agregar la dirección.")


    return direccion_dao.insertar_direccion(cliente.id, direccion)

def eliminar_direccion(cliente):
    direccion_id = input("numero de la direccion a borrar: ")#

    return direccion_dao.eliminar_direccion(cliente.id, direccion_id)
