"""Class Api Service."""
import json
from typing import List
from applestore.applicationservice import ApplicationService
from applestore.csvservice import CsvService


class ApiService:
    """Service Api AppleStore."""

    __csvAppleStore: str = ''
    __reportsFile: str = ''
    __applicationService: ApplicationService
    __csvService: CsvService

    def __init__(
        self,
        csvAppleStore: str,
        applicationService: ApplicationService,
        csvService: CsvService,
        reportsFile: str,
    ):
        """Construct."""
        self.__csvAppleStore = csvAppleStore
        self.__applicationService = applicationService
        self.__csvService = csvService
        self.__reportsFile = reportsFile

    def consumer(self) -> str:
        """Consume and generate data or api json."""
        data: List[int] = self.__analyzer(
            data=self.__transform(
                data=self.__csvService.extract(
                    csvPathFile=self.__csvAppleStore
                )
            )
        )
        self.__applicationService.persist(data=data)
        self.__createReportCsv(data=data)
        return json.dumps({
            'pathReportCsv': self.__reportsFile,
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

    def __createReportCsv(self, data: List[int]):
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

        self.__csvService.createCsv(
            csvPathFile=self.__reportsFile,
            columns=columns,
            data=dataCsv
        )
