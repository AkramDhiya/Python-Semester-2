# adalah struktur data yang mirip dengan list, tetapi bersifat immutable (tidak bisa diubah setelah di ubah)

# membuat tabel
my_tuple = (1,2,3,4,5)
print(my_tuple[0])
print("\n") # out: {1, 2, 3, 4, 5}


# operasi pada tuple
print(len(my_tuple)) # output:5
print(my_tuple[1:4]) # output:(2,3,4)
print("\n") # out:


# tuple packing dan unpacking
person = ("alice", 25, "engineer")
name, age, job = person
print(name) #out: alice
print(age) #out: 25
print(job) #out: engineer
print("\n")
