import MySQLdb

db = MySQLdb.connect(host="localhost", user="root",
                     passwd="hendrawan", db="kampus")
c = db.cursor()
sql = "INSERT INTO Mahasiswa(NIM,Nama,Alamat) VALUES (%s, %s, %s)"
val = ("001", "Hendrawan", "Brebes")
c.execute(sql, val)

#commit untuk apply perubahan data
db.commit()

c.close()
