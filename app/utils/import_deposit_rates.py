import csv
from datetime import datetime
from sqlmodel import Session

from app.schema.deposit_rate import DepositRatesCreate
from app import crud


def import_deposit_rates(session: Session) -> list[DepositRatesCreate] | None:

    if crud.deposit_rates.get(session, id=1):
        return None
    

    deposit_rates: list[DepositRatesCreate] = []

    with open("data/processed/processed_snb-data-zikrepro-en-selection-20231002_1430.csv", newline="\n") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            deposit_rate = DepositRatesCreate(
                date=datetime.strptime(row["Date"], "%Y-%m"),
                value=float(row["Value"]),
            )
            deposit_rates.append(deposit_rate)

    crud.deposit_rates.create_multiple(session, obj_in=deposit_rates)

    return deposit_rates


    


