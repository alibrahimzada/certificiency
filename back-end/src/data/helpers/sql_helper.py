import psycopg2

class ISqlHelper:
    def get_connection(self):
        pass

    def query_all(self, sql: str):
        pass

    def query_first_or_default(self, sql):
        pass

    def execute(self, sql: str):
        pass

    def get_column_names(self, sql:str):
        pass

    def get_rows(self, sql: str):
        pass



class SqlHelper(ISqlHelper):

    def __init__(self):
        self.is_test_db = False

    def get_connection(self):
        db_name = ''
        if self.is_test_db:
            db_name = 'certificiency-test'
        else:
            db_name = 'certificiency'

        con = psycopg2.connect("dbname={} user=postgres password=123456789".format(db_name))

        con.autocommit = True
        return con

    def query_all(self, sql):
        con = self.get_connection()

        
        cur = con.cursor()

        cur.execute(sql)

        records = cur.fetchall()

        cur.close()

        con.close()

        return records

    def query_first_or_default(self, sql):
        con = self.get_connection()

        cur = con.cursor()

        cur.execute(sql)

        records = cur.fetchone()

        cur.close()

        con.close()

        return records

    def execute(self, sql: str):
        con = self.get_connection()

        cur = con.cursor()

        cur.execute(sql)
        rows_affected = cur.rowcount
        cur.close()

        con.close()

        return rows_affected


    def get_column_names(self, table_name):
        query = """SELECT column_name
                 FROM information_schema.columns
                 WHERE table_name = '{}';""".format(table_name)
        
        column_names = self.query_all(query)
        return column_names

    def get_rows(self, query, table_name):
        column_names = self.get_column_names(table_name)

        res = self.query_all(query)

        rows = []
        for i in range(len(res)):
            row_details = {}

            for j in range(len(res[i])):
                table_column = column_names[j][0]
                cell_value = res[i][j]

                row_details[table_column] = cell_value
            
            rows.append(row_details)

        return rows

    def get_single_instance(self, table_name, primary_key_name, primary_key):
        query = """ SELECT *
                    FROM \"{}\"
                    WHERE {}={}
                """.format(table_name, primary_key_name, primary_key)

        instance = self.query_first_or_default(query)
        columns = self.get_column_names(table_name)

        data = {}
        for i in range(len(instance)):
            table_column = columns[i][0]
            cell_value = instance[i]
            data[table_column] = cell_value

        return data
