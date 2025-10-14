# El Club Del Mate

🧉 MateClub: Comercio electrónico de la Experiencia Matera
Este es el repositorio del proyecto final para la materia. Nuestro objetivo es desarrollar un e-commerce completamente funcional centrado en la cultura del mate, ofreciendo productos de alta calidad y una experiencia de usuario excepcional.

## 📝 Descripción del Proyecto
MateClub no es solo una tienda online, es un espacio digital para los amantes del mate. Nuestro comercio electrónico se especializa en ofrecer una selección curada de yerbas de productores pequeños, mates artesanales, bombillas de diseño y accesorios únicos. Además, buscamos educar y construir una comunidad a través de contenido de valor y un modelo de suscripción exclusivo.

## 👥 Integrantes del Grupo

- Martín Vijarra
- Luis Gerardo Catalás
- Emilce Agustia Torres
- Luis Gastón Alonso
- Kevin Cristofer Lorea Tannfeld

## 🎯 Público Objetivo
Nuestro e-commerce está dirigido a tres perfiles de clientes principales:

El Matero Experimentado: Busca variedad, calidad y yerbas de orígenes específicos que no se encuentran en supermercados.
El Principiante o Turista: Quiere iniciarse en el mundo del mate y busca un "Kit de Inicio" con todo lo necesario y una guía fácil de seguir.
El "Regalador": Busca un regalo original, de calidad y con identidad cultural para amigos, familiares o clientes corporativos.

## ✨ Propuesta de Valor

¿Qué nos hace diferentes?
- Curación Experta: Seleccionamos cada producto a mano, trabajando con artesanos y pequeños productores de todo el país.
- Comunidad y Cultura: No solo vendemos productos, compartimos la historia y la pasión detrás del mate a través de nuestro blog y redes sociales.
- Suscripción Exclusiva: ofrecemos una caja mensual con "La Yerba del Mes" para descubrir sabores únicos y apoyar a productores locales.
- Experiencia de Usuario: Una plataforma limpia, segura y fácil de usar desde cualquier dispositivo.


## 📜IEEE830
Link del IEEE830: https://docs.google.com/document/d/18mxs_G_R2EQWllAvJqpyUc8nmDZWfDuqXhMY6I2GZLU/edit?tab=t.0

## Link Página Web
https://grupo-22-ispc.github.io/El-Club-Del-Mate/


## ⚙️ Instalación del Proyecto

Este proyecto está desarrollado en Python y utiliza MySQL como base de datos. A continuación se detallan los pasos para instalarlo en modo desarrollador.

### 🔧 Requisitos

- Python 3.10 o superior
- MySQL Server (ej. XAMPP o MySQL Workbench)
- Git

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

### ▶️ Ejecución del Proyecto

Para correr el proyecto, necesitas iniciar el backend y el frontend por separado.

1.  **Para iniciar el Backend (Servidor de Python):**
    En tu terminal, desde la raíz del proyecto, ejecuta:
    ```bash
    python back/app.py
    ```
    El servidor estará corriendo, listo para recibir peticiones.

2.  **Para iniciar el Frontend (Sitio Web):**
    La forma más sencilla es abrir el archivo `front/index.html` directamente en tu navegador web.







