import os

from dotenv import load_dotenv
from sqlmodel import SQLModel, Session, create_engine
from app.utils.import_target_ranges import import_target_ranges
from app.utils.import_deposit_rates import import_deposit_rates

# Connect to the database
load_dotenv(".env")
DBUSER = os.environ["DBUSER"]
DBPASS = os.environ["DBPASS"]
DBHOST = os.environ["DBHOST"]
DBNAME = os.environ["DBNAME"]
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

    import_target_ranges(session)
    import_deposit_rates(session)
    

    session.close()

    # Use import_target_range() to get a list of TargetRangesCreate objects
