days = {"senin": "SENIN",
        "selasa": "SELASA",
        "rabu": "RABU",
        "kamis": "KAMIS",
        "jumat": "JUMAT"}

for day in days:
    print(day)
print("-----------------------\n")

for day in days:
    print(days[day])
print("-----------------------\n")

#Menambahkan data
days["sabtu"] = "SABTU"
for day in days:
    print(days[day])
print("-----------------------\n")

#Menghapus data
days.pop("jumat")
for day in days:
    print(days[day])
print("-----------------------\n")
