# Taller U3: Automatización de Base de Datos con Python, Faker y Git

## Objetivo general

Desarrollar un proyecto en Python que automatice la creación y el poblado de una base de datos MySQL local, utilizando SQLAlchemy para la conexión y gestión de la tabla, Faker para la generación de datos ficticios y Git/GitHub para el control de versiones del desarrollo.

## Objetivos específicos

- Configurar un proyecto Python desde cero usando un entorno virtual.
- Proteger las credenciales de conexión mediante variables de entorno.
- Conectar Python con una base de datos MySQL local.
- Verificar la conexión entre Python y MySQL antes de ejecutar el proceso principal.
- Crear automáticamente una tabla en MySQL usando SQLAlchemy.
- Generar datos ficticios coherentes con la librería Faker.
- Insertar 100.000 registros en la base de datos mediante inserción por lotes.

## Descripción del proyecto

Este proyecto crea automáticamente una tabla llamada `personas_felipe` dentro de una base de datos MySQL local llamada `actividad_3_udea`.

La tabla contiene una clave primaria y siete atributos generados con Faker. El script principal se encarga de conectarse a MySQL, crear la tabla si no existe, generar datos ficticios e insertar 100.000 registros usando lotes de 5.000 registros.

La conexión a la base de datos se realiza mediante la variable `DATABASE_URL`, almacenada en un archivo `.env`. Este archivo no se sube al repositorio porque contiene credenciales reales.

## Archivos del proyecto

- `main.py`: script principal del proyecto.
- `test_mysql.py`: script usado para verificar la conexión inicial entre Python y MySQL.
- `.env.example`: plantilla pública para configurar la conexión.
- `.gitignore`: archivo que evita subir credenciales, entorno virtual y archivos temporales.
- `requirements.txt`: listado de dependencias necesarias.
- `README.md`: documentación del proyecto.

## Configuración del entorno

Crear el entorno virtual:

```powershell
python -m venv .venv
```

Activar el entorno virtual en PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```powershell
python -m pip install -r requirements.txt
```

## Configuración de la base de datos

Crear la base de datos en MySQL:

```sql
CREATE DATABASE actividad_3_udea;
```

Crear un archivo `.env` en la raíz del proyecto usando como referencia el archivo `.env.example`.

Contenido esperado de `.env.example`:

```env
DATABASE_URL=mysql+pymysql://user:password@localhost:3306/actividad_3_udea
```

En el archivo `.env` real se deben reemplazar `user` y `password` por las credenciales reales de MySQL.

## Ejecución del proyecto

Ejecutar el script principal:

```powershell
python main.py
```

El programa realiza los siguientes pasos:

1. Carga la variable `DATABASE_URL` desde el archivo `.env`.
2. Crea la conexión con MySQL usando SQLAlchemy.
3. Define la tabla `personas_felipe`.
4. Crea la tabla automáticamente si no existe.
5. Genera datos ficticios con Faker.
6. Agrupa los datos en lotes de 5.000 registros.
7. Inserta los registros en MySQL.
8. Muestra en consola el total final de registros insertados.

## Estructura de la tabla

La tabla `personas_felipe` contiene:

- `id`: clave primaria autoincremental.
- `nombre`: nombre generado con Faker.
- `correo`: correo electrónico generado con Faker.
- `fecha_nacimiento`: fecha de nacimiento generada con Faker.
- `ciudad`: ciudad generada con Faker.
- `direccion`: dirección generada con Faker.
- `telefono`: teléfono generado con Faker.
- `ocupacion`: ocupación generada con Faker.

## Funcionamiento del código

El archivo `main.py` está organizado en funciones para separar responsabilidades.

La función `crear_tabla_personas()` define la estructura de la tabla usando SQLAlchemy.

La función `generar_persona()` crea un diccionario con los datos de una persona ficticia. Las claves del diccionario coinciden con los nombres de las columnas de la tabla.

La función `generar_lote_personas()` crea una lista de diccionarios. Esta lista representa un lote de registros.

La función `main()` coordina todo el proceso: carga la configuración, crea la conexión, crea la tabla, genera los datos e inserta los registros.

La inserción se realiza por lotes mediante:

```python
connection.execute(insert(personas), lote_personas)
```

Esto permite enviar una lista completa de diccionarios a la base de datos, evitando insertar los 100.000 registros uno por uno.

## Validación en DBeaver

Para comprobar que los registros fueron insertados correctamente, ejecutar en DBeaver:

```sql
SELECT COUNT(*) FROM personas_felipe;
```

El resultado esperado es:

```text
100000
```

## Verificación de conexión entre Python y MySQL

Antes de ejecutar el script principal, se puede verificar la conexión con el archivo `test_mysql.py`.

Ejecutar:

```powershell
python test_mysql.py
```

El script carga la variable `DATABASE_URL` desde `.env`, intenta conectarse a MySQL usando SQLAlchemy y ejecuta una consulta sencilla para comprobar la base de datos activa.

Resultado esperado:

```text
Conexion exitosa a la base de datos: actividad_3_udea
```

Esta verificación permite confirmar que Python puede comunicarse correctamente con MySQL antes de crear la tabla e insertar los registros.

## Prueba de inserción inicial

También se realizó una prueba inicial insertando un solo registro generado con Faker antes de pasar a la inserción masiva. Esta prueba permitió confirmar que la tabla `personas_felipe` recibía correctamente los datos generados desde Python y que las claves del diccionario creado por Faker coincidían con las columnas definidas en SQLAlchemy. Una vez validado este flujo con un registro individual, se adaptó la lógica para generar listas de diccionarios e insertarlas por lotes. Esta verificación se puede realizar con el código presentado estableciendo las variables

```python
TOTAL_REGISTROS = 1
TAMANO_LOTE = 1
```

## Recomendaciones

- Ejecutar el script desde el entorno virtual activado.
- Si se hicieron pruebas previas, limpiar la tabla antes de una ejecución final:

```sql
TRUNCATE TABLE personas_felipe;
```

## Control de versiones

El proyecto fue desarrollado usando Git y GitHub. El historial de commits evidencia las etapas principales del desarrollo:

- Configuración inicial del proyecto.
- Creación de la tabla con SQLAlchemy.
- Generación de datos con Faker.
- Inserción masiva por lotes.
- Documentación y validación final.

_Realizado por Felipe Villa Velásquez._