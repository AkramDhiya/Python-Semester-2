# list adalah tipe data yang digunakan untuk menyimpan koleksi atau kumpulan item dalam satu variabel. List bisa berisi berbagai tipe data seperti angka, string, atau bahkan list lainnya.

# membuat list dari range
numbers = [x for x in range(5)]
print(numbers) # output: [0, 2, 4, 6, 8]


# menggunakan kondisi dalam list comprehension
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers) # output: [0, 2, 4, 6, 8]


# mengubah elemen dalam list
squares = [x**2 for x in range(5)]
print(squares) # output: [0, 1, 4, 9, 16]


# nested list comprehension
matrix = [[x for x in range(3)]for y in range (3)]
print(matrix) 
print("\n") # output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]


# menggunakan kondisi tanpa list comprehension
list = [1,2,3,4,5,6,7,8,9,10]
newlist = []
for x in list:
    if x % 2 == 0:
        newlist.append(x)
        print(newlist)
print("\n") # output:
