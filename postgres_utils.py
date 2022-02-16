# python3

import psycopg2

class PostgresUtils:

    def __init__(self) -> None:
        pass

    def connect(self, params):
        self.connection = psycopg2.connect(**params)
    
    def execute_command(self, command):
        try:
            curr = self.connection.cursor()
            curr.execute(command)
        except (Exception, psycopg2.DatabaseError) as error:
            print (error)

    def __del__(self):
        print ("closing postgres connection object")
        self.connection.close()

