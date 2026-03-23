# 🏥 RehabGuard API | Secure Rehabilitation Management System

![Status](https://img.shields.io/badge/Estado-En_Desarrollo_🚀-2ea44f?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

Una API RESTful robusta y segura diseñada para la gestión de historiales clínicos y pautas de rehabilitación física.

Este proyecto nace de la intersección entre **10+ años de experiencia en ciencias de la salud y el deporte**, y el desarrollo Backend moderno. Su objetivo es proporcionar una arquitectura limpia, segura y escalable para aplicaciones del sector _Healthcare_ (HealthTech).

---

## ✨ Características Principales

- 🏛️ **Arquitectura de 3 Capas:** Separación clara entre modelos de datos (SQLAlchemy), esquemas de validación (Pydantic) y lógica de rutas.
- 🔐 **Seguridad Integrada:** Gestión de credenciales mediante variables de entorno (.env) y protección de la capa de datos.
- 🧪 **Validación Estricta:** Uso intensivo de Pydantic para asegurar la integridad de los datos médicos.
- 📖 **Validación Estricta:** Generación automática de Swagger UI para facilitar la integración con clientes Frontend.

---

## 🛠️ Stack Tecnológico

- **Lenguaje:** Python 3.12.3
- **Framework:** FastAPI
- **Servidor:** Uvicorn
- **Base de Datos:** MySQL 8.0+/9.0+
- **ORM:** SQLAlchemy
- **Servidor:** Uvicorn+ PyMySQL + Cryptography

---

## 💻 Instalación y Uso Local

1.  **Clona el repositorio:**

    ```bash
    git clone [https://github.com/davidvalades/rehab-api-core.git](https://github.com/davidvalades/rehab-api-core.git)
    cd rehab-api-core
    ```

2.  **Crea y activa el entorno virtual**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instala las dependencias**

    ```bash
     pip install -r requirements.txt
    ```

4.  **Configuracion de Variables de Entorno**
    Crea un archivo _.env_ en la raiz del proyecto con tus credenciales de base de datos:

        ```bash
        DB_USER=tu_usuario
        DB_PASSWORD=tu_contraseña
        DB_HOST=localhost_o_ip
        DB_PORT=3306
        DB_NAME=rehab_db
        ```

5.  **Ejecuta el servidor**
    ```bash
    uvicorn main:app --reload
    ```

---

## 📁 Estructura del Proyecto

    rehab-api-core/
    ├── db/          # Configuración y conexión a Base de Datos
    ├── models/      # Modelos de tablas (SQLAlchemy)
    ├── schemas/     # Modelos de validación de datos (Pydantic)
    ├── main.py      # Punto de entrada de la aplicación
    └── .env         # Variables de entorno (no trackeado por Git)

---

_⭐ Desarrollado por: [David Valadés Navarro](https://github.com/davidValades) - Backend-focused Developer | Cybersecurity Learner_

---
