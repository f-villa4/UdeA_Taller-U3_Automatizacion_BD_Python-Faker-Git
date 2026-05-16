import os

from dotenv import load_dotenv
from faker import Faker
from sqlalchemy import Column, Date, Integer, MetaData, String, Table, create_engine, func, insert, select


TOTAL_REGISTROS = 100000
TAMANO_LOTE = 5000


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


def generar_lote_personas(fake, cantidad):
    personas = []

    for _ in range(cantidad):
        persona = generar_persona(fake)
        personas.append(persona)

    return personas


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
    registros_insertados = 0

    with engine.begin() as connection:
        while registros_insertados < TOTAL_REGISTROS:
            registros_restantes = TOTAL_REGISTROS - registros_insertados
            cantidad_lote = min(TAMANO_LOTE, registros_restantes)

            lote_personas = generar_lote_personas(fake, cantidad_lote)

            connection.execute(insert(personas), lote_personas)

            registros_insertados += cantidad_lote
            print(f"Registros insertados: {registros_insertados}")

    with engine.connect() as connection:
        total = connection.execute(select(func.count()).select_from(personas)).scalar_one()

    print(f"Total final en personas_felipe: {total}")


if __name__ == "__main__":
    main()
