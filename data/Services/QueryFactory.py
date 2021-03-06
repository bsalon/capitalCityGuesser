class QueryFactory:
    def create_create_table_query(table_name, column_tuples):
        table_columns = QueryFactory.__parse_column_tuples(column_tuples)
        return f"CREATE TABLE {table_name} ({table_columns})"


    def create_insert_query(table_name, column_tuples):
        nongenerated_column_tuples = QueryFactory.__filter_generated_columns(column_tuples)
        table_column_names = QueryFactory.__parse_column_names(nongenerated_column_tuples)
        placeholders = QueryFactory.__create_placeholders(nongenerated_column_tuples)
        return f"INSERT INTO ({table_name}) {table_column_names} VALUES ({placeholders})"


    def create_select_query(table_name, column_tuples):
        table_column_names = QueryFactory.__parse_column_names(column_tuples)
        return f"SELECT {table_column_names} FROM {table_name}"


    def create_select_where_string_query(table_name, column_tuples, column_index, column_values):
        table_column_names = QueryFactory.__parse_column_names(column_tuples)
        where_column = QueryFactory.__parse_column_names([column_tuples[column_index]])
        constraints = QueryFactory.__create_where_string_constraints(where_column, column_values)
        return f"SELECT {table_column_names} FROM {table_name} WHERE {constraints}"


    def __create_where_string_constraints(where_column, column_values):
        return " OR ".join([f"{where_column}='{val}'" for val in column_values])


    def __filter_generated_columns(column_tuples):
        return [(col, t_col) for col, t_col in column_tuples if ("AUTO" not in t_col and "GENERATED" not in t_col)]


    def __create_placeholders(columns):
        return ", ".join(["%s"] * len(columns))


    def __parse_column_names(column_tuples):
        return ", ".join([col_name for col_name, col_type in column_tuples])


    def __parse_column_tuples(column_tuples):
        return ", ".join([col_name + " " + col_type for col_name, col_type in column_tuples])
