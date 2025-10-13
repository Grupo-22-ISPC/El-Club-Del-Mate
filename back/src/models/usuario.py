import hashlib
import re
import string

<<<<<<< HEAD
from src.services.usuario_service import cambiar_rol_usuario, mostrar_usuarios_registrados
from src.core import menu_cliente, menu_vendedor,menu_admin


class Usuario():

    ROLES = {
        1: "admin",
        2: "cliente",
        3: "vendedor"
    }


    def __init__(self,id_usuario,nombre,email,contrasena,rol_id):
        self.__id = id_usuario
        self._nombre = nombre
        self._email = email
        self._contrasena = contrasena
        self._rol = rol_id

=======
from src.services import vendedor_service
from src.services import cliente_service
from src.models.direccion import Direccion
from src.models.rol import Rol
from src.services.usuario_service import cambiar_rol_usuario, eliminar_usuario_por_email, mostrar_usuarios_registrados
from src.core import menu_cliente, menu_vendedor,menu_admin



class Usuario():

    def __init__(self, id_usuario, nombre, email, contrasena, rol:Rol, direcciones:Direccion = None):
        self._id = id_usuario
        self._nombre = nombre
        self._email = email
        self._contrasena = contrasena
        self._rol = rol
        self._direcciones = direcciones if direcciones else []

    @property
    def id(self):
        return self._id
>>>>>>> e896cd1b9b7e6a074f11a9af10d82223f183ac3e
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nuevo_nombre:str):
        if len(nuevo_nombre) < 2:
            raise ValueError("EL nombre debe tener al menos 2 caracteres")
        self._nombre = nuevo_nombre

<<<<<<< HEAD

=======
>>>>>>> e896cd1b9b7e6a074f11a9af10d82223f183ac3e
    @property
    def email(self):
        return self._email

<<<<<<< HEAD

=======
>>>>>>> e896cd1b9b7e6a074f11a9af10d82223f183ac3e
    @property
    def rol(self):
        return self._rol

<<<<<<< HEAD
    @property
    def nombre_rol(self):
        return self.ROLES.get(self._rol, "Rol desconocido")


    @rol.setter
    def rol(self,nuevo_rol:int):
        if nuevo_rol not in (1,2,3):
            raise ValueError("Rol invalido. Debe ser 1(admin), 2(cliente), 3(vendedor)")
        self._rol = nuevo_rol

=======
    @rol.setter
    def rol(self,nuevo_rol:Rol):
      self._rol = nuevo_rol
>>>>>>> e896cd1b9b7e6a074f11a9af10d82223f183ac3e
    
    @property
    def contrasena(self):
        return self._contrasena
    
<<<<<<< HEAD
=======
    @property
    def direcciones(self):
        return self._direcciones
    
    @direcciones.setter
    def direcciones(self,nueva_direccion):
        if not all(isinstance(d,Direccion) for d in nueva_direccion):
            raise TypeError("Todas las direcciones deben ser instancias de la clase Direccion")
        self._direcciones = nueva_direccion
    
>>>>>>> e896cd1b9b7e6a074f11a9af10d82223f183ac3e
    @contrasena.setter
    def contrasena(self, nueva_contrasena :str):
        if len(nueva_contrasena) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")
        if not re.search(r"[A-Z]", nueva_contrasena):
            raise ValueError("Debe contener al menos una mayúscula")
        if not re.search(r"[a-z]",nueva_contrasena):
            raise ValueError("Debe contener al menos una minúscula")
        if not re.search(r"[0-9]",nueva_contrasena):
            raise ValueError("Debe contener al menos un número")
        if not any(caracter in string.punctuation for caracter in nueva_contrasena):
            raise ValueError("Debe contener al menos un carácter especial")
        
        
        self._contrasena = hashlib.sha256(nueva_contrasena.encode()).hexdigest()

    def __str__(self):
        # Muestra el objeto como texto
<<<<<<< HEAD
        return f"Usuario({self.email},{self.nombre},{self.rol})"
=======
        return f"Usuario({self.email},{self.nombre},{self.rol},{self.direcciones})"
>>>>>>> e896cd1b9b7e6a074f11a9af10d82223f183ac3e
    
    def mostrar_menu(self):
        raise NotImplementedError("Este método debe ser implementado por cada rol.")

<<<<<<< HEAD
   



=======
>>>>>>> e896cd1b9b7e6a074f11a9af10d82223f183ac3e


class Vendedor(Usuario):
    def mostrar_menu(self):
        menu_vendedor.menu_vendedor_cli(self)

<<<<<<< HEAD
=======
    def lista_productos(self):
        vendedor_service.lista_productos_service(self)

    def agregar_producto(self):
        vendedor_service.agregar_producto_service(self)

    def editar_producto(self):
        vendedor_service.editar_producto_service(self)

    def eliminar_producto(self):
        vendedor_service.eliminar_producto_service(self)

>>>>>>> e896cd1b9b7e6a074f11a9af10d82223f183ac3e

class Cliente(Usuario):
    def mostrar_menu(self):
        menu_cliente.menu_cliente_cli(self)
<<<<<<< HEAD
    
=======

    def ver_datos(self):
        return cliente_service.ver_datos_service(self)

    def editar_nombre(self):
        return cliente_service.editar_nombre_service(self)

    def agregar_direccion(self):
        return cliente_service.agregar_direccion_service(self)

    def eliminar_direccion(self):
        return cliente_service.eliminar_direccion_service(self)
    
    def ver_productos_disponibles(self):
        return cliente_service.productos_disponibles_service(self)
    
    def realizar_pedidos(self):
        return cliente_service.realizar_pedidos(self)
    
    def ver_mis_pedidos(self):
        return cliente_service.mis_pedidos_service(self)

>>>>>>> e896cd1b9b7e6a074f11a9af10d82223f183ac3e
       


class Admin(Usuario):
    def mostrar_menu(self):
        menu_admin.menu_admin_cli(self)

<<<<<<< HEAD
    @staticmethod
    def listar_usuarios():
        mostrar_usuarios_registrados()
    
    @staticmethod
    def cambiar_rol():
       nuevo_rol = cambiar_rol_usuario()
       print(nuevo_rol) 
    
    def eliminar_usuario(self):
        pass
=======
    def listar_usuarios(self):
        mostrar_usuarios_registrados(self)
    
    def cambiar_rol(self):
        cambiar_rol_usuario(self)
        
    def eliminar_usuario(self):
        eliminar_usuario_por_email(self)
>>>>>>> e896cd1b9b7e6a074f11a9af10d82223f183ac3e
