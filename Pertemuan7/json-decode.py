import json

data = '[{ "nama" : "Hendrawan", "alamat" : "Kaligangsa Wetan Brebes" },' \
       '{ "nama" : "Yanto", "alamat" : "Tegal" }]'

result = json.loads(data)

for x in result:
    print(x['nama'])
