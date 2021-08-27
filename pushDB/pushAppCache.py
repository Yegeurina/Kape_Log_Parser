import MySQLdb

connection = MySQLdb.Connect(host='localhost', 
                                user='root', 
                                passwd='root', 
                                db='remakekape',
                                local_infile=True)

cursor = connection.cursor()

logfile = 'AppCache.csv'
query = "LOAD DATA INFILE '%s' INTO TABLE remakekape.appcache FIELDS TERMINATED BY ',';" %(logfile)
cursor.execute( query )

connection.commit()
