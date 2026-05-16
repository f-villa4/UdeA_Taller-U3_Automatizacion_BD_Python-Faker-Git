# Taller U3 — Automatización de BD con Python, Faker y Git

Proyecto desarrollado para el Taller U3 de Bases de Datos para Ciencia de Datos.

El objetivo es automatizar la creacion y poblado de una base de datos MySQL local usando Python, SQLAlchemy y Faker. El proyecto tambien usa Git y GitHub para llevar control de versiones del desarrollo.

## Estado actual

Hasta el momento se ha realizado:

- Creacion de la carpeta del proyecto.
- Inicializacion del repositorio local con Git.
- Conexion del repositorio local con GitHub.
- Creacion del entorno virtual de Python.
- Instalacion de dependencias iniciales.
- Configuracion de variables de entorno con `.env`.
- Creacion de `.env.example` como plantilla publica.
- Creacion de `.gitignore` para evitar subir credenciales y archivos del entorno virtual.
- Creacion de la base de datos `actividad_3_udea` en MySQL.
- Prueba de conexion entre Python y MySQL.

## Tecnologias usadas

- Python
- MySQL
- DBeaver
- SQLAlchemy
- PyMySQL
- python-dotenv
- Faker
- Git
- GitHub

## Configuracion temporal

El archivo `.env` contiene la conexion real a la base de datos y no debe subirse al repositorio.

El archivo `.env.example` contiene una plantilla como esta:

```env
DATABASE_URL=mysql+pymysql://user:password@localhost:3306/actividad_3_udea
