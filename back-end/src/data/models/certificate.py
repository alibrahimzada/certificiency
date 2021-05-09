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

        sql = """INSERT INTO \"Certificate\"
                 VALUES ()"""
        status = self.sql_helper.execute(sql)
        print(status)


    def delete_certificate(self, data):
        sql = """ 
            DELETE FROM \"Certificate\"
            WHERE ={}
        """.format(data[''])
        status = self.sql_helper.execute(sql)
        print(status)


    def update_certificate(self, data):
        sql = """
            UPDATE \"Certificate\"
            SET 
            WHERE 
        """

        status = self.sql_helper.execute(sql)
        print(status)