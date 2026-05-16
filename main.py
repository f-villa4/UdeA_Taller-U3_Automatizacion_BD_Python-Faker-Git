import os

from dotenv import load_dotenv
from sqlalchemy import Column, Date, Integer, MetaData, String, Table, create_engine


def crear_tabla_personas(metadata):
    personas = Table(
        "personas_felipe",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("nombre", String(100), nullable=False),
        Column("correo", String(150), nullable=False),
        Column("fecha_nacimiento", Date, nullable=False),
        Column("ciudad", String(100), nullable=False),
        Column("direccion", String(255), nullable=False),
        Column("telefono", String(50), nullable=False),
        Column("ocupacion", String(120), nullable=False),
    )

    return personas


def main():
    load_dotenv()

    database_url = os.getenv("DATABASE_URL")

    if database_url is None:
        raise ValueError("No se encontro DATABASE_URL en el archivo .env")

    engine = create_engine(database_url)

    metadata = MetaData()
    crear_tabla_personas(metadata)

    metadata.create_all(engine)

    print("Tabla personas_felipe creada correctamente o ya existia.")


if __name__ == "__main__":
    main()
