import hashlib
import re
import string

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
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nuevo_nombre:str):
        if len(nuevo_nombre) < 2:
            raise ValueError("EL nombre debe tener al menos 2 caracteres")
        self._nombre = nuevo_nombre

    @property
    def email(self):
        return self._email

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self,nuevo_rol:Rol):
      self._rol = nuevo_rol
    
    @property
    def contrasena(self):
        return self._contrasena
    
    @property
    def direcciones(self):
        return self._direcciones
    
    @direcciones.setter
    def direcciones(self,nueva_direccion):
        if not all(isinstance(d,Direccion) for d in nueva_direccion):
            raise TypeError("Todas las direcciones deben ser instancias de la clase Direccion")
        self._direcciones = nueva_direccion
    
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
        return f"Usuario({self.email},{self.nombre},{self.rol},{self.direcciones})"
    
    def mostrar_menu(self):
        raise NotImplementedError("Este método debe ser implementado por cada rol.")



class Vendedor(Usuario):
    def mostrar_menu(self):
        menu_vendedor.menu_vendedor_cli(self)

    def lista_productos(self):
        vendedor_service.lista_productos_service(self)

    def agregar_producto(self):
        vendedor_service.agregar_producto_service(self)

    def editar_producto(self):
        vendedor_service.editar_producto_service(self)

    def eliminar_producto(self):
        vendedor_service.eliminar_producto_service(self)


class Cliente(Usuario):
    def mostrar_menu(self):
        menu_cliente.menu_cliente_cli(self)

    def ver_datos(self):
        return cliente_service.ver_mis_datos(self)

    def editar_nombre(self, nuevo_nombre):
        return cliente_service.editar_nombre(self, nuevo_nombre)

    def agregar_direccion(self):
        return cliente_service.agregar_direccion(self)

    def eliminar_direccion(self):
        return cliente_service.eliminar_direccion(self)
    
    def ver_mis_pedidos(self):
        pass

    def ver_productos_disponibles(self):
        return cliente_service.ver_productos_disponibles(self)
    
    def realizar_pedidos(self):
        return cliente_service.realizar_pedidos(self)

       


class Admin(Usuario):
    def mostrar_menu(self):
        menu_admin.menu_admin_cli(self)

    @staticmethod
    def listar_usuarios():
        mostrar_usuarios_registrados()
    
    @staticmethod
    def cambiar_rol():
        cambiar_rol_usuario()
        
    
    @staticmethod
    def eliminar_usuario():
        eliminar_usuario_por_email()