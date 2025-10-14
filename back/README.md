### 📋 Pasos de Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone https://URL_DE_TU_REPOSITORIO.git
    cd EL-CLUB-DEL-MATE
    ```

2.  **Crea y activa un entorno virtual (muy recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instala las dependencias:**
    Este comando utiliza el archivo `requirements.txt` para instalar todas las librerías de Python necesarias con sus versiones exactas (proceso conocido como "unfreezing").
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configura las variables de entorno:**
    Crea un archivo llamado `.env` en la raíz del proyecto. Puedes copiar el contenido de `.env.example` y rellenarlo con tus credenciales locales:
    ```env
    DB_HOST=localhost
    DB_PORT=tu_puerto
    DB_USER=root
    DB_PASSWORD=tu_clave_aqui
    DB_NAME=club_del_mate

    ```

5.  **Prepara la Base de Datos:**
    1.  **Asegúrate de que tu servidor de MySQL esté corriendo.**

    2.  **Crea la base de datos** con el nombre que especificaste en tu archivo `.env` (ej: `club_del_mate`).

    3.  **Ejecuta los scripts en el siguiente orden** para crear la estructura y cargar los datos:
    * **Primero, las tablas:** `back/scripts/creacion_db.sql`
    * **Segundo, los datos iniciales:** `back/scripts/club_del_mate_datos_iniciales.sql`
    * **Tercero, las vistas:** `back/scripts/club_del_mate_vistas.sql`

### Importante
El programa cuenta con un usuario por defecto, siendo este el ``administrador principal``:

- email: admin@clubdelmate.com
- clave: P@ssw0rd