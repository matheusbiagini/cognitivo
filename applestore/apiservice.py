"""Class Api Service."""
import json
from typing import List
from typing import TypeVar
from applestore.applicationservice import ApplicationService
from applestore.csvservice import CsvService

T = TypeVar('T')


class ApiService:
    """Service Api AppleStore."""

    __csv_apple_store: str = ''
    __reports_file: str = ''
    __application_service: ApplicationService
    __csv_service: CsvService

    def __init__(
        self,
        csv_apple_store: str,
        application_service: ApplicationService,
        csv_service: CsvService,
        reports_file: str,
    ):
        """Construct."""
        self.__csv_apple_store = csv_apple_store
        self.__application_service = application_service
        self.__csv_service = csv_service
        self.__reports_file = reports_file

    def consumer(self) -> str:
        """Consume and generate data or api json."""
        data: List[T] = self.__analyzer(
            data=self.__transform(
                data=self.__csv_service.extract(
                    csv_path_file=self.__csv_apple_store
                )
            )
        )
        self.__application_service.persist(data=data)
        self.__create_report_csv(data=data)
        return json.dumps({
            'pathReportCsv': self.__reports_file,
            'data': data
        })

    def __analyzer(self, data: List[T]) -> List[T]:
        new_data: List[T] = []
        for row in data:
            if (row['prime_genre'] == 'Music') \
             or (row['prime_genre'] == 'Book'):
                new_data.append(row)
        return sorted(new_data, key=self.__ordenation, reverse=True)[0:10]

    # noinspection PyMethodMayBeStatic
    def __ordenation(self, item: List[T]) -> int:
        return item['n_citacoes']

    # noinspection PyMethodMayBeStatic
    def __transform(self, data: List[T]) -> List[T]:
        new_data: List[T] = []
        for row in data:
            new_data.append({
                    "application_id": int(row['id'].replace('"', "")),
                    "track_name": row['trackName'].replace('"', ""),
                    "n_citacoes": int(row['nCitacoes'].replace('"', "")),
                    "size_bytes": int(row['sizeBytes'].replace('"', "")),
                    "price": float(row['Prince'].replace('"', "")),
                    "prime_genre": row['PrimeGenre'].replace('"', "")
                })
        return new_data

    def __create_report_csv(self, data: List[T]):
        data_csv: List[T] = []
        columns: List[str] = [
            "application_id",
            "track_name",
            "n_citacoes",
            "size_bytes",
            "price",
            "prime_genre"
        ]

        for row in data:
            data_csv.append([
                row["application_id"],
                row["track_name"],
                row["n_citacoes"],
                row["size_bytes"],
                row["price"],
                row["prime_genre"]
            ])

        self.__csv_service.create(
            csv_path_file=self.__reports_file,
            columns=columns,
            data=data_csv
        )
