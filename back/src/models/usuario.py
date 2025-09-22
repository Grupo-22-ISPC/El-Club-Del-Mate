import hashlib
import re
import string

from src.services.usuario_service import cambiar_rol_usuario, mostrar_usuarios_registrados
from src.core import menu_cliente, menu_vendedor,menu_admin


class Usuario():

    ROLES = {
        1: "admin",
        2: "usuario",
        3: "vendedor"
    }


    def __init__(self,id_usuario,nombre,email,contrasena,rol_id):
        self.__id = id_usuario
        self._nombre = nombre
        self._email = email
        self._contrasena = contrasena
        self._rol = rol_id

    
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

    @property
    def nombre_rol(self):
        return self.ROLES.get(self._rol, "Rol desconocido")


    @rol.setter
    def rol(self,nuevo_rol:int):
        if nuevo_rol not in (1,2,3):
            raise ValueError("Rol invalido. Debe ser 1(admin), 2(cliente), 3(vendedor)")
        self._rol = nuevo_rol

    
    @property
    def contrasena(self):
        return self._contrasena
    
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
        return f"Usuario({self.email},{self.nombre},{self.rol})"
    
    def mostrar_menu(self):
        raise NotImplementedError("Este método debe ser implementado por cada rol.")

   





class Vendedor(Usuario):
    def mostrar_menu_cli(self):
        menu_vendedor(self)


class Cliente(Usuario):
    def mostrar_menu_cli(self):
        menu_cliente(self)
    
       


class Admin(Usuario):
    def mostrar_menu(self):
        menu_admin.menu_admin_cli(self)

    @staticmethod
    def listar_usuarios():
        mostrar_usuarios_registrados()
    
    @staticmethod
    def cambiar_rol():
       nuevo_rol = cambiar_rol_usuario()
       print(nuevo_rol) 
    
    def eliminar_usuario(self):
        pass