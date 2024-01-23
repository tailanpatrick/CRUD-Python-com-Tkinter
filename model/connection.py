from typing import Type
import mysql.connector


class Connection:

    def __init__(self) -> None:
        pass

    def get_Connection(self):
        return mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='dbaulapythonmysql',
                )
        
    def close_connection(self):
        self.__conn.close()
        