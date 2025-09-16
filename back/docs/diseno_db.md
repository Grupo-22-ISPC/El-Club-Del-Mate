# Documentación del Diseño de la Base de Datos

Este documento detalla el diseño, la estructura y las relaciones de la base de datos `planificador_usuarios`, implementada en MySQL.

## 1. Proceso de Diseño

* **Identificación de Entidades:** Se identificaron dos entidades principales para el sistema: `Usuario` (la persona que usa el sistema) y `Rol` (el tipo de permisos que tiene).
* **Normalización:** El diseño cumple con la **Tercera Forma Normal (3FN)**. La información del rol (`nombre`) se separó en su propia tabla (`roles`) para evitar redundancias y dependencias transitivas en la tabla `usuarios`. Un usuario tiene un `id_rol`, y ese `id_rol` determina el nombre del rol.

## 2. Esquema Relacional

El esquema consta de dos tablas relacionadas: `roles` y `usuarios`.

### Tabla `roles`

* **Propósito:** Almacenar los diferentes tipos de roles que pueden existir en el sistema.

* **Definición:**

| Nombre de Columna | Tipo de Dato  | Restricciones      | Descripción                                |
| ----------------- | ------------- | ------------------ | ------------------------------------------ |
| `id_rol`          | `INT`         | `PRIMARY KEY`, `AUTO_INCREMENT` | Identificador numérico único para el rol. |
| `nombre`          | `VARCHAR(50)` | `NOT NULL`         | Nombre descriptivo del rol (ej. "Administrador"). |

### Tabla `usuarios`

* **Propósito:** Almacenar la información de cada cuenta de usuario registrada.

* **Definición:**

| Nombre de Columna  | Tipo de Dato   | Restricciones          | Descripción                                        |
| ------------------ | -------------- | ---------------------- | -------------------------------------------------- |
| `id_usuario`       | `INT`          | `PRIMARY KEY`, `AUTO_INCREMENT` | Identificador numérico único para el usuario.     |
| `nombre_usuario`   | `VARCHAR(50)`  | `NOT NULL`, `UNIQUE`   | Nombre de usuario para iniciar sesión. No se repite. |
| `contraseña`       | `VARCHAR(100)` | `NOT NULL`             | Contraseña del usuario. (Debe ser hasheada en un sistema real). |
| `datos_personales` | `VARCHAR(255)` | `NULL`                 | Información adicional del usuario (nombre, email, etc.). |
| `id_rol`           | `INT`          | `NOT NULL`, `FOREIGN KEY` | Referencia a la tabla `roles` para definir los permisos del usuario. |

## 3. Relaciones

* **Tipo de Relación:** Existe una relación de **uno a muchos** entre `roles` y `usuarios`.
* **Descripción:** Un rol puede ser asignado a muchos usuarios diferentes, pero cada usuario puede tener asignado un único rol.
* **Implementación:** Esta relación se establece mediante la clave foránea (`FOREIGN KEY`) en la columna `id_rol` de la tabla `usuarios`, que apunta al `id_rol` de la tabla `roles`.