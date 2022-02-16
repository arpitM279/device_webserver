# python3

import psycopg2

class PostgresUtils:

    def __init__(self) -> None:
        pass

    def connect(self, params):
        self.connection = psycopg2.connect(**params)
    
    def add_table(self, table_name):
        pass