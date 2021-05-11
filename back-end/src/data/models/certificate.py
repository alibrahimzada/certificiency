from data.models.base_entity import BaseEntity

class Certificate(BaseEntity):

    # put variables to init
    def __init__(self):
        super(Certificate, self).__init__()
   
    
    def get_column_names(self):
        sql = """SELECT column_name
                 FROM information_schema.columns
                 WHERE table_name = 'Certificate';"""
        
        column_names = self.sql_helper.query_all(sql)
        return column_names

    def get_all_certificates(self):
        column_names = self.get_column_names()

        sql = """SELECT *
                 FROM \"Certificate\""""

        res = self.sql_helper.query_all(sql)

        certificates = []
        for i in range(len(res)):
            certificate_details = {}

            for j in range(len(res[i])):
                table_column = column_names[j][0]
                cell_value = res[i][j]

                certificate_details[table_column] = cell_value
            
            certificates.append(certificate_details)

        return certificates

    def insert_certificate(self, data):
        query = """INSERT INTO \"Certificate\"
                   values({}, '{}');""".format(data['certificate_id'], data['certificate_name'])

        try:        
            rows_affected = self.sql_helper.execute(query)
            if rows_affected > 0:
                return {"status": "success"}
            return {"status": "fail"}
        
        except:
            return {"status": "fail"}


    def delete_certificate(self, data):
        query = """ 
                DELETE FROM \"Certificate\"
                WHERE certificate_id={}""".format(data['certificate_id'])

        rows_affected = self.sql_helper.execute(query)
        
        if rows_affected > 0:
            return {'status': 'success'}
        return {'status': 'fail'}


    def update_certificate(self, data):
        query = """
            UPDATE \"Certificate\"
            SET certificate_name = '{}'
            WHERE certificate_id={}""".format(data['certificate_name'], data['certificate_id'])

        rows_affected = self.sql_helper.execute(query)

        if rows_affected > 0:
            return {'status': 'success'}
        return {'status': 'fail'}
