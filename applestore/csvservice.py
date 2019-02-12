"""Class Csv Service."""
import csv
from typing import TypeVar
from typing import List

T = TypeVar('T')


class CsvService:
    """Csv service."""

    # noinspection PyMethodMayBeStatic
    def extract(self, csv_path_file: str) -> List[T]:
        """Extract csv."""
        with open(csv_path_file, newline='') as csvfile:
            data: List[T] = []
            csv_list = csv.reader(csvfile, delimiter=',')
            for row in csv_list:
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

    # noinspection PyMethodMayBeStatic
    def create(
        self,
        csv_path_file: str,
        columns: List[str],
        data: List[T]
    ) -> None:
        """Create csv file."""
        with open(csv_path_file, 'w') as csvFile:
            c = csv.writer(csvFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            c.writerow(columns)
            for row in data:
                c.writerow(row)
