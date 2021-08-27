import MySQLdb

connection = MySQLdb.Connect(host='localhost', 
                                user='root', 
                                passwd='root', 
                                db='remakekape',
                                local_infile=True)

cursor = connection.cursor()

query = "TRUNCATE setup_api;"
cursor.execute( query )

logfile = 'INF.csv'
query = "LOAD DATA INFILE '%s' INTO TABLE remakekape.setup_api FIELDS TERMINATED BY ',';" %(logfile)
cursor.execute( query )

connection.commit()
