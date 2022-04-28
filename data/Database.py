import mysql.connector


class Database:
    def __init__(self, db_name, *args, **kwargs):
        self.connector = mysql.connector.connect(*args, **kwargs)
        self.__create_database(db_name)


    def __create_database(self, db_name):
        with self.connector.cursor(buffered=True) as cursor:
            cursor.execute("SHOW DATABASES")

            databases = (db[0] for db in cursor)
            if (db_name not in databases):
                cursor.execute(f"CREATE DATABASE {db_name}")

        self.connector.database = db_name
