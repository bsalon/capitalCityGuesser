class QueryFactory:
    def create_create_table_query(table_name, column_tuples):
        table_columns = QueryFactory.__parse_column_tuples(column_tuples)
        return f"CREATE TABLE {table_name} {table_columns}"


    def create_insert_query(table_name, column_tuples):
        table_column_names = QueryFactory.__parse_column_names(column_tuples)
        placeholders = QueryFactory.__create_placeholders(column_tuples)
        return f"INSERT INTO {table_name} {table_column_names} VALUES {placeholders}"


    def __create_placeholders(columns):
        return "(" + ", ".join(["%s"] * len(columns)) + ")"


    def __parse_column_names(column_tuples):
        return "(" + ", ".join([col_name for col_name, col_type in column_tuples]) + ")"


    def __parse_column_tuples(column_tuples):
        return "(" + ", ".join([col_name + " " + col_type for col_name, col_type in column_tuples]) + ")"
