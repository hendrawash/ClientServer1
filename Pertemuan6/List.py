fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
print("-----------------------\n")

print(fruits[1])

# Menambah data ke List
fruits.append("mango")

for fruit in fruits:
    print(fruit)
print("-----------------------\n")

#Menghapus data dari List
fruits.remove("banana")
for fruit in fruits:
    print(fruit)
print("-----------------------\n")