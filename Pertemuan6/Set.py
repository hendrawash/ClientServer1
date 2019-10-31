fruits = {"apple", "banana", "cherry"}

for fruit in fruits:
    print(fruit)
print("-----------------------\n")

#Menambah data
fruits.add("Mango")
for fruit in fruits:
    print(fruit)
print("-----------------------\n")

#Menghapus Data
fruits.remove("banana")
fruits.add("Mango")
for fruit in fruits:
    print(fruit)
print("-----------------------\n")