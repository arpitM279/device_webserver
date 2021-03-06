# python3

import mysql.connector
from mysql.connector import Error

class MySQLUtils:

    def __init__(self) -> None:
        pass

    def create_server_connection(self, config):
        try:
            self.connection = mysql.connector.connect(**config)
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")

    def execute_command(self, command):
        cursor = self.connection.cursor()
        try:
            cursor.execute(command)
            print("command executed successfully")
        except Error as err:
            print(f"Error: '{err}'")
