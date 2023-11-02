from typing import List
from pydantic import BaseModel
import csv

class SnbData(BaseModel):
    Date: str
    snbband: str
    Value: float

def read_csv_file(file_path: str) -> List[SnbData]:
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)  # skip header row
        data = []
        for row in reader:
            if row[2]:
                data.append(SnbData(Date=row[0], snbband=row[1], Value=float(row[2])))
        return data

data = read_csv_file('./data/processed/processed_snb-data-snbband-en-selection-20190621_0900.csv')
print(data)