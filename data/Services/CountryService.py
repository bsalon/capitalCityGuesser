from ..Database import Database

from ..Entities.Country import Country

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


    def has_at_least_rows(self, rows_count):
        with self.database.connector.cursor(buffered=True) as cursor:
            select_query = QueryFactory.create_select_query(self.table_name, self.column_tuples)
            cursor.execute(select_query)
            data = cursor.fetchall()
            return len(data) >= rows_count


    def clear_table(self):
        with self.database.connector.cursor(buffered=True) as cursor:
            cursor.execute(f"DELETE FROM {self.table_name}")


    def insert_countries(self, countries):
        with self.database.connector.cursor(buffered=True) as cursor:
            insert_query = QueryFactory.create_insert_query(self.table_name, self.column_tuples)
            cursor.executemany(insert_query, countries)

        self.database.connector.commit()


    def get_countries_with_continents(self, continents):
        with self.database.connector.cursor(buffered=True) as cursor:
            select_where_string_query = QueryFactory.create_select_where_string_query(self.table_name, self.column_tuples, 2, continents)
            cursor.execute(select_where_string_query)
            data = cursor.fetchall()
            countries = list(map(lambda c : Country(c[0], c[1], c[2], c[3]), data))
            return countries


    def get_all_countries(self):
        with self.database.connector.cursor(buffered=True) as cursor:
            select_query = QueryFactory.create_select_query(self.table_name, self.column_tuples)
            cursor.execute(select_query)
            all_data = cursor.fetchall()
            all_countries = list(map(lambda c : Country(c[0], c[1], c[2], c[3]), all_data))
            return all_countries


    def __create_table(self):
        with self.database.connector.cursor(buffered=True) as cursor:
            cursor.execute("SHOW TABLES")

            db_tables = (table[0] for table in cursor)
            if (self.table_name not in db_tables):
                create_table_query = QueryFactory.create_create_table_query(self.table_name, self.column_tuples)
                cursor.execute(create_table_query)
