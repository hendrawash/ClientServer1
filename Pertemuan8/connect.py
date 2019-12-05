import MySQLdb

db = MySQLdb.connect(host="localhost", user="root",
                     passwd="", db="kampus")
c = db.cursor()
c.execute("select version()")
rows = c.fetchall()
for row in rows:
    print("MySQL Version %s" % row[0])

c.close()
