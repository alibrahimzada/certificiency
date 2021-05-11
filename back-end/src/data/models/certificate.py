from data.models.base_entity import BaseEntity

class Certificate(BaseEntity):

    # put variables to init
    def __init__(self):
        super(Certificate, self).__init__()
   
    def get_all_certificates(self):
        return self.sql_helper.get_rows('Certificate')

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
