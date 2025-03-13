# dict adalah struktur data yang  menyimpan pasangan key value yang unik

# membuat dictionary
data = {"nama":"alice", "age":25, "city":"new york"}
print(data ["nama"]) # output:


# menambah dan mengubah elemen
data["job"] = "engineer" # menambahkan elemen baru
data["age"] = 26 # mengubah nilai yang ada
print(data) # output:


# menghapus elemen
del data["city"]
print(data) # output:
 

# iterasi dalam dictionary
for key, value in data.items():
    print(f"{key}: {value}") # output:

    
# dictionary comprehension
squares = {x:x**2 for x in range(5)}
print(squares) # output: