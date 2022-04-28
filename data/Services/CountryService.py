from ..Database import Database
from .QueryFactory import QueryFactory


class CountryService:
    def __init__(self):
        self.db_name = "geography"
        self.table_name = "countries"
        self.database = Database(self.db_name, host="localhost", user="root", passwd="c0MM0N1ty+")
        self.column_tuples = [("country_id", "INTEGER AUTO_INCREMENT PRIMARY KEY"),
                              ("name", "VARCHAR(127) UNIQUE NOT NULL"),
                              ("continent", "VARCHAR(127) NOT NULL"),
                              ("capital_city", "VARCHAR(127) NOT NULL")]
        self.__create_table()


    def __create_table(self):
        with self.database.connector.cursor(buffered=True) as cursor:
            cursor.execute("SHOW TABLES")

            db_tables = (table[0] for table in cursor)
            if (self.table_name not in db_tables):
                create_table_query = QueryFactory.create_create_table_query(self.table_name, self.column_tuples)
                cursor.execute(create_table_query)
