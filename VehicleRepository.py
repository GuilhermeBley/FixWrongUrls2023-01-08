import mysql.connector

class VehicleRepository:
    def __init__(self, hostName, userName, password, database):
        self.mydb = mysql.connector.connect(
            host=hostName,
            user=userName,
            password=password,
            database=database,
            autocommit=False
            )
        
    def getWithInvalidPartialKey(self, skip = 0, take = 1000):
        mycursor = self.mydb.cursor()
        sql = 
            "SELECT * FROM *** WHERE PartialKey Like '\% \%' LIMIT %s, %s"
        val = (take, skip)
        mycursor.execute(sql, val)
        return mycursor.fetchall()

    # idFs is 'FileStream' and idFsmd is 'File Stream Meta Data'
    def updateFileAndFileMetaData(self, idFs, idFsmd, newPartialKey, newUrl):
        mycursor = self.mydb.cursor()
        mydb = self.mydb

        sql = 
            @"UPDATE ** SET PartialKey = %s, Url = %s where id = %s;"
        val = (newPartialKey, newUrl, idFs)
        mycursor.execute(sql, val)
        
        sql = 
            @"UPDATE ** SET PartialKey = %s where id = %s;"
        val = (newPartialKey, idFsmd)
        mycursor.execute(sql, val)

        
        mydb.commit()
