import csv
from datetime import datetime
from collections import defaultdict
from sqlmodel import Session

from app.schema.target_range import TargetRangesCreate
from app import crud

# class Record(BaseModel):
#     date: datetime
#     d0: str
#     d1: str
#     value: float


# records = []

# with open(
#     "data/processed/processed_snb-data-zikrepro-en-selection-20231002_1430.csv",
#     newline="\n",
# ) as csvfile:
#     reader = csv.DictReader(csvfile, delimiter=";")
#     for row in reader:
#         record = Record(
#             date=datetime.strptime(row["Date"], "%Y-%m"),
#             d0=row["D0"],
#             d1=row["D1"],
#             value=float(row["Value"]),
#         )
#         records.append(record)

# print(records)


def import_target_range(session: Session) -> list[TargetRangesCreate] | None:
    # Check if the database is empty
    target_range = crud.target_ranges.get(session, id=1)
    if target_range:
        return None

    # Using TargetRangesCreate and the file "data/processed/processed_snb-data-snbband-en-selection-20190621_0900.csv"
    # create a list of TargetRangesCreate objects
    # and import them into the database

    # Create a list of TargetRangesCreate objects
    target_ranges: list[TargetRangesCreate] = []

    # Open the file "data/processed/processed_snb-data-snbband-en-selection-20190621_0900.csv"
    # and read the data into the list of TargetRangesCreate objects

    # Initialize an empty dictionary
    data = defaultdict(dict)

    # Open the file and create a csv.reader object
    with open(
        "data/processed/processed_snb-data-snbband-en-selection-20190621_0900.csv",
        newline="\n",
    ) as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        next(reader)  # Skip the header row
        for row in reader:
            date, d0, value = row
            date = datetime.strptime(date.strip('"'), "%Y-%m-%d")
            value = float(value.strip('"'))
            # If the D0 field is "UG", add an entry with the date as the key and a dictionary with "lower_bound" as the key and the value as the value
            if d0.strip('"') == "UG":
                data[date]["lower_bound"] = value
            # If the D0 field is "OG", add an entry to the existing dictionary for the date with "upper_bound" as the key and the value as the value
            elif d0.strip('"') == "OG":
                data[date]["upper_bound"] = value

    # Iterate over the data dictionary
    for date, bounds in data.items():
        # Create a TargetRangesCreate instance for each item
        target_range = TargetRangesCreate(
            date=date,
            lower_bound=bounds["lower_bound"],
            upper_bound=bounds["upper_bound"],
        )
        # Add the TargetRangesCreate instance to the list
        target_ranges.append(target_range)

    # Load the list of TargetRangesCreate objects into the database

    crud.target_ranges.create_multiple(db=session, obj_in=target_ranges)

    return target_ranges


def import