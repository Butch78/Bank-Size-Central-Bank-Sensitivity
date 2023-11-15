import csv
from datetime import datetime
from sqlmodel import Session

from app import crud
from app.schema.target_rate import TargetRatesCreate


def import_target_rates(session: Session) -> list[TargetRatesCreate] | None:
    # Check if the database is empty
    target_rate = crud.target_rates.get(db=session, id=1)
    if target_rate:
        return None

    target_rates: list[TargetRatesCreate] = []

    with open(
        "data/processed/processed_snb-data-snboffzisa-en-selection-20231023_0900.csv",
        newline="\n",
    ) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            if row["Value"] == "":
                continue
            target_rate = TargetRatesCreate(
                date=datetime.strptime(row["Date"], "%Y-%m"),
                value=float(row["Value"]),
            )
            target_rates.append(target_rate)

    crud.target_rates.create_multiple(db=session, obj_in=target_rates)

    return target_rates
