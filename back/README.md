## Ejecutar backend
Para ejecutar el backend necesitas:


- Instalar los paquetes necesarios:

```bash
pip install mysql-connector-python python-dotenv
```

- Asegurate de crear la base de datos utilizando el script sql ``01_creacion_db.sql`` que se encuentra dentro de la carpeta ``scripts``

- Debes crear el archivo ``.env`` en la carpeta raíz del repositorio usando el ``.env.example`` como base para el mismo

- Por ultimo ejecutar el archivo ``app.py``

```bash
python app.py
```

### Importante
El programa cuenta con un usuario por defecto, siendo este el ``administrador principal``:

- email: admin@clubdelmate.com
- clave: P@ssw0rd