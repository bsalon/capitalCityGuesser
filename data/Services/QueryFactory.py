class QueryFactory:
    def create_create_table_query(table_name, column_tuples):
        table_columns = QueryFactory.__parse_column_tuples(column_tuples)
        return f"CREATE TABLE {table_name} {table_columns}"


    def __parse_column_tuples(column_tuples):
        return "(" + ", ".join([col_name + " " + col_type for col_name, col_type in column_tuples]) + ")"
