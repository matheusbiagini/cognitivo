"""Class Csv Service."""
import csv
from typing import List


class CsvService:
    """Csv service."""

    def extract(self, csvPathFile: str) -> List[int]:
        """Extract csv."""
        with open(csvPathFile, newline='') as csvfile:
            data: List[int] = []
            csvList = csv.reader(csvfile, delimiter=',')
            for row in csvList:
                data.append({
                    "id": row[1],
                    "trackName": row[2],
                    "nCitacoes": row[6],
                    "sizeBytes": row[3],
                    "Prince": row[5],
                    "PrimeGenre": row[12]
                })
        data.pop(0)
        return data

    def createCsv(self, csvPathFile: str, columns: List[int], data: List[int]):
        """Create csv file."""
        with open(csvPathFile, 'w') as csvFile:
            c = csv.writer(csvFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            c.writerow(columns)
            for row in data:
                c.writerow(row)