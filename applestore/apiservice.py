import json
import csv
from typing import List
from applestore.models import Application

class ApiService:
    workfile = ''
    reportsFile = ''

    def __init__(self, workfile: str, reportsFile: str):
        self.workfile = workfile
        self.reportsFile = reportsFile

    def consumer(self) -> str:
        data: List[int]  = self.analyzer(self.transform(self.extract()))
        self.persist(data)
        self.createReportCsv(data)
        return json.dumps({
            'pathReportCsv': self.reportsFile,
            'data': data
        })

    def extract(self) -> List[int]:
        with open(self.workfile, newline='') as csvfile:
            data: List[int] = []
            csvList = csv.reader(csvfile, delimiter=',')
            for row in csvList:
                data.append({
                    "id" : row[1],
                    "trackName": row[2],
                    "nCitacoes" : row[6],
                    "sizeBytes" : row[3],
                    "Prince" : row[5],
                    "PrimeGenre" : row[12]
                });
        data.pop(0)
        return data

    def analyzer(self, data: List[int]) -> List[int]:
        newData: List[int] = []
        for row in data:
            if (row['prime_genre'] == 'Music') or (row['prime_genre'] == 'Book'):
                newData.append(row)
        return sorted(newData, key=self.ordenation, reverse=True)[0:10]

    def ordenation(self, item: List[str]):
        return item['n_citacoes']

    def transform(self, data: List[int]) -> List[int]:
        newData: List[int] = []
        for row in data:
            newData.append({
                    "application_id" : int(row['id'].replace('"', "")),
                    "track_name" : row['trackName'].replace('"', ""),
                    "n_citacoes" : int(row['nCitacoes'].replace('"', "")),
                    "size_bytes" : int(row['sizeBytes'].replace('"', "")),
                    "price" : float(row['Prince'].replace('"', "")),
                    "prime_genre" : row['PrimeGenre'].replace('"', "")
                })
        return newData

    def createReportCsv(self, data: List[int]):
        fileOutput: str = self.reportsFile
        with open(fileOutput, 'w') as csvFile:
            c = csv.writer(csvFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            c.writerow(["application_id","track_name","n_citacoes","size_bytes","price","prime_genre"])
            for row in data:
                c.writerow([row["application_id"], row["track_name"], row["n_citacoes"], row["size_bytes"], row["price"], row["prime_genre"]])

    def persist(self, data: List[int]):
        for row in data:
            application: Application = Application(
                application_id = row['application_id'],
                track_name = row['track_name'],
                n_citacoes = row['n_citacoes'],
                size_bytes = row['size_bytes'],
                price = row['price'],
                prime_genre = row['prime_genre']
            )
            application.save()
