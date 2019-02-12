"""Class Application Service."""
from applestore.models import Application
from typing import List


class ApplicationService:
    """Application model management service."""

    # noinspection PyMethodMayBeStatic
    def persist(self, data: List[int]) -> None:
        """Persist in database."""
        for row in data:
            application: Application = Application(
                application_id=row['application_id'],
                track_name=row['track_name'],
                n_citacoes=row['n_citacoes'],
                size_bytes=row['size_bytes'],
                price=row['price'],
                prime_genre=row['prime_genre']
            )
            application.save()
