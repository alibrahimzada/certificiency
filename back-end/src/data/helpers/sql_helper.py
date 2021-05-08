import psycopg2

class ISqlHelper:
    def get_connection(self):
        pass

    def query_all(self, sql: str):
        pass

    def query_first_or_default(self, sql: str):
        pass

    def execute(self, sql: str):
        pass


class SqlHelper(ISqlHelper):

    def get_connection(self):
        con = psycopg2.connect("dbname=postgres user=postgres password=123456789")

        return con

    def query_all(self, sql):
        con = self.get_connection()

        
        cur = con.cursor()

        cur.execute(sql)

        records = cur.fetchall()

        cur.close()

        return records

    def query_first_or_default(self, sql):
        con = self.get_connection()

        cur = con.cursor()

        cur.execute(sql)

        records = cur.fetchone()

        cur.close()

        return records

    def execute(self, sql: str):
        con = self.get_connection()

        cur = con.cursor()

        cur.execute(sql)

        cur.close()

        return True