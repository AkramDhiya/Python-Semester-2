# set adalah koleksi elemen yang bersifat unik dan tidak berurutan

#membuat set
my_set = {1,2,3,4,4,5}
print(my_set) # output tanpa duplikat
print("\n")


# operasi pada set
set1 = {1,2,3}
set2 = {2,4,5}

print(set1|set2) # union : {1,2,3,4,5} (Union menggabungkan dua atau lebih himpunan dan menghilangkan elemen duplikat.)
print(set1&set2) # intersection : {3} (menampilkan data duplikat)
print(set1 - set2) # diffrence : {1,2} (Difference mengambil elemen yang hanya ada di satu set dan tidak ada di set lain.)
print(set1 ^ set2) # symentric diffrence : {1,2,4,5} (tidak menampilkan data yang duplikat)
print("\n")

# menambahkan dan menghapus elemen
my_set.add(6)
my_set.remove(3)
print(my_set)