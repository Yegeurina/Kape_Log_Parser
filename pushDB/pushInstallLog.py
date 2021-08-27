import MySQLdb

connection = MySQLdb.Connect(host='localhost', 
                                user='root', 
                                passwd='root', 
                                db='remakekape',
                                local_infile=True)

cursor = connection.cursor()

logfile = 'Install_Log.csv'
query = "LOAD DATA INFILE '%s' INTO TABLE remakekape.installlog FIELDS TERMINATED BY ',';" %(logfile)
cursor.execute( query )

connection.commit()

logfile = 'Install_fileCreate.csv'
query = "LOAD DATA INFILE '%s' INTO TABLE remakekape.fileCreate FIELDS TERMINATED BY ',';" %(logfile)
cursor.execute( query )

connection.commit()

logfile = 'Install_arpCreate.csv'
query = "LOAD DATA INFILE '%s' INTO TABLE remakekape.arpCreate FIELDS TERMINATED BY ',';" %(logfile)
cursor.execute( query )

connection.commit()