"""Class Api Service."""
import json
from typing import List
from applestore.applicationservice import ApplicationService
from applestore.csvservice import CsvService


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
        data: List[int] = self.__analyzer(
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

    def __analyzer(self, data: List[int]) -> List[int]:
        newData: List[int] = []
        for row in data:
            if (row['prime_genre'] == 'Music') \
             or (row['prime_genre'] == 'Book'):
                newData.append(row)
        return sorted(newData, key=self.__ordenation, reverse=True)[0:10]

    def __ordenation(self, item: List[str]):
        return item['n_citacoes']

    def __transform(self, data: List[int]) -> List[int]:
        newData: List[int] = []
        for row in data:
            newData.append({
                    "application_id": int(row['id'].replace('"', "")),
                    "track_name": row['trackName'].replace('"', ""),
                    "n_citacoes": int(row['nCitacoes'].replace('"', "")),
                    "size_bytes": int(row['sizeBytes'].replace('"', "")),
                    "price": float(row['Prince'].replace('"', "")),
                    "prime_genre": row['PrimeGenre'].replace('"', "")
                })
        return newData

    def __create_report_csv(self, data: List[int]):
        dataCsv: List[int] = []
        columns: List[int] = [
            "application_id",
            "track_name",
            "n_citacoes",
            "size_bytes",
            "price",
            "prime_genre"
        ]

        for row in data:
            dataCsv.append([
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
            data=dataCsv
        )
