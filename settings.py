import logging
import os
from dotenv import load_dotenv

log = logging.getLogger()
log.setLevel(logging.DEBUG)
env = load_dotenv()


class PostgresConfiguration:
    POSTGRES_DB_PORT = os.getenv('POSTGRES_PORT')
    POSTGRES_DB_NAME = os.getenv('POSTGRES_DB_NAME')
    POSTGRES_DB_USER = os.getenv('POSTGRES_USER')
    POSTGRES_DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_DB_HOST = os.getenv('POSTGRES_HOST')

    @property
    def postgres_db_path(self):
        return f'postgresql://{self.POSTGRES_DB_USER}:{self.POSTGRES_DB_PASSWORD}@' \
            f'{self.POSTGRES_DB_HOST}:' \
            f'{self.POSTGRES_DB_PORT}/{self.POSTGRES_DB_NAME}'
