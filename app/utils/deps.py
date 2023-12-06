import os

from dotenv import load_dotenv
from sqlmodel import SQLModel, Session, create_engine
from app.utils.import_target_ranges import import_target_ranges
from app.utils.import_deposit_rates import import_deposit_rates
from app.utils.import_target_rates import import_target_rates
from sqlalchemy import text

from app.utils.config import settings

# Connect to the database
load_dotenv(".env")
DBUSER = settings.DBUSER
DBPASS = settings.DBPASS
DBHOST = settings.DBHOST
DBNAME = settings.DBNAME
DATABASE_URI = f"postgresql://{DBUSER}:{DBPASS}@{DBHOST}/{DBNAME}"
if DBHOST != "localhost":
    DATABASE_URI += "?sslmode=require"

engine = create_engine(DATABASE_URI, echo=True)


def get_session():
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def import_data():
    # Use get_session() to get a session
    session = next(get_session())

    # TODO parrallelize so that the data is imported in parallel
    import_target_ranges(session)
    import_deposit_rates(session)
    import_target_rates(session)

    session.close()

    # Use import_target_range() to get a list of TargetRangesCreate objects


def create_read_only_user():
    # TODO create a read-only user

    session = next(get_session())

    # Create a new user if it doesn't already exist

    session.execute(
        text(
            """
            DO
            $do$
            BEGIN
            IF NOT EXISTS (
                SELECT FROM pg_catalog.pg_user 
                WHERE  usename = 'user_read_only') THEN
                
                CREATE USER user_read_only WITH PASSWORD 'LocalPasswordOnly';
            END IF;
            END
            $do$
            """
        )
    )
    session.commit()

    # Grant USAGE privilege to the new user on the public schema
    session.execute(text("GRANT USAGE ON SCHEMA public TO user_read_only;"))
    session.commit()

    # Grant SELECT privilege to the new user on all tables in the public schema
    session.execute(
        text("GRANT SELECT ON ALL TABLES IN SCHEMA public TO user_read_only;")
    )
    session.commit()

    # Set the default privileges to grant SELECT privilege to the new user on future tables
    session.execute(
        text(
            "ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO user_read_only;"
        )
    )
    session.execute(
        text(
            "ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO user_read_only;"
        )
    )
    session.commit()
