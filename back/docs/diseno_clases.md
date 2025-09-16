# Documentación del Diseño de Clases

Este documento detalla la arquitectura de software y el diseño de clases para la aplicación de consola del sistema de gestión de usuarios.

## 1. Clases Principales

El sistema se estructura en tres clases principales, cada una con una responsabilidad bien definida para lograr una buena organización y separación de responsabilidades:

* **`Usuario`**: Modela los datos de un usuario.
* **`GestorUsuarios`**: Contiene la lógica de negocio para administrar a los usuarios.
* **`Sistema`**: Maneja la interfaz de usuario y el flujo principal del programa.

---

## 2. Descripción Detallada de Clases

### 2.1. Clase `Usuario` (`usuario.py`)

* **Responsabilidad Principal:** Actuar como un contenedor de datos (modelo) para representar a un único usuario en el sistema.

* **Atributos:**

| Atributo           | Tipo de Dato | Descripción                                      |
| ------------------ | ------------ | ------------------------------------------------ |
| `id_usuario`       | `int`        | Identificador numérico único.                    |
| `nombre_usuario`   | `str`        | Nombre utilizado para el inicio de sesión.       |
| `contraseña`       | `str`        | Clave de acceso del usuario.                     |
| `rol`              | `str`        | Nivel de permisos ("administrador" o "usuario"). |
| `datos_personales` | `str`        | Información adicional del usuario.               |

* **Métodos:**

| Método      | Descripción                                                                 |
| ----------- | --------------------------------------------------------------------------- |
| `__init__`  | Constructor que inicializa todos los atributos de un nuevo objeto `Usuario`. |
| `__str__`   | Devuelve una representación en cadena del objeto con todos sus datos.        |

### 2.2. Clase `GestorUsuarios` (`gestor_usuarios.py`)

* **Responsabilidad Principal:** Encapsular toda la lógica de negocio para la administración de usuarios. **En la versión actual, opera en memoria** (los datos se pierden al cerrar el programa).

* **Atributos:**

| Atributo          | Tipo de Dato        | Descripción                                   |
| ----------------- | ------------------- | --------------------------------------------- |
| `usuarios`        | `List[Usuario]`     | Una lista que contiene todos los objetos `Usuario` registrados. |
| `next_id`         | `int`               | Un contador para simular el ID autoincremental de la base de datos. |

* **Métodos Principales (Públicos):**

| Método              | Descripción                                         |
| ------------------- | --------------------------------------------------- |
| `registrar_usuario` | Crea y añade un nuevo usuario a la lista.          |
| `iniciar_sesion`    | Valida credenciales y devuelve el objeto `Usuario`. |
| `listar_usuarios`   | Imprime la lista de todos los usuarios.             |
| `cambiar_rol`       | Modifica el rol de un usuario existente.            |
| `eliminar_usuario`  | Elimina un usuario de la lista.                     |

* **Métodos Internos (Privados):**

| Método                | Descripción                                                   |
| --------------------- | ------------------------------------------------------------- |
| `_existe_usuario`     | Verifica si un nombre de usuario ya está en uso.              |
| `_validar_contraseña` | Comprueba si una contraseña cumple los requisitos de seguridad. |

### 2.3. Clase `Sistema` (`sistema.py`)

* **Responsabilidad Principal:** Manejar toda la interacción con el usuario (la capa de presentación), incluyendo la visualización de menús y la captura de datos de entrada.

* **Atributos:**

| Atributo          | Tipo de Dato        | Descripción                                       |
| ----------------- | ------------------- | ------------------------------------------------- |
| `gestor`          | `GestorUsuarios`    | Una instancia del gestor para acceder a la lógica de negocio. |
| `usuario_actual`  | `Usuario`           | Guarda el objeto del usuario que ha iniciado sesión.  |

* **Métodos:**

| Método                   | Descripción                                                         |
| ------------------------ | ------------------------------------------------------------------- |
| `mostrar_menu`           | Es el bucle principal que muestra el menú correcto según si hay o no un usuario logueado. |
| `_registrar`             | Pide los datos al usuario y llama al gestor para registrarlo.         |
| `_iniciar_sesion`        | Pide credenciales y llama al gestor para iniciar sesión.             |
| `_menu_administrador`    | Muestra y gestiona las opciones disponibles para el rol de administrador. |
| `_menu_usuario_estandar` | Muestra y gestiona las opciones disponibles para el rol de usuario. |