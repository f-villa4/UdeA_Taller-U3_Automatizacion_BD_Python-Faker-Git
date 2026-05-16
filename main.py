import os
from faker import Faker
from sqlalchemy import func, insert, select

from dotenv import load_dotenv
from sqlalchemy import Column, Date, Integer, MetaData, String, Table, create_engine, func, insert, select


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

def generar_persona(fake):
    persona = {
        "nombre": fake.name(),
        "correo": fake.email(),
        "fecha_nacimiento": fake.date_of_birth(minimum_age=18, maximum_age=80),
        "ciudad": fake.city(),
        "direccion": fake.address().replace("\n", ", "),
        "telefono": fake.phone_number(),
        "ocupacion": fake.job(),
    }

    return persona

def main():
    load_dotenv()

    database_url = os.getenv("DATABASE_URL")

    if database_url is None:
        raise ValueError("No se encontro DATABASE_URL en el archivo .env")

    engine = create_engine(database_url)

    metadata = MetaData()
    personas = crear_tabla_personas(metadata)

    metadata.create_all(engine)

    fake = Faker("es_CO")
    persona = generar_persona(fake)

    with engine.begin() as connection:
        connection.execute(insert(personas), persona)

    with engine.connect() as connection:
        total = connection.execute(select(func.count()).select_from(personas)).scalar_one()

    print("Registro generado e insertado correctamente.")
    print(f"Total actual en personas_felipe: {total}")

if __name__ == "__main__":
    main()
