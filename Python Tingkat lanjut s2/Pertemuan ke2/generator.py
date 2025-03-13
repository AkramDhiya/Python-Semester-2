# adalah fungsi yang mengembalikan nilai satu per satu menggunakan kata kunci yield, yang lebih menghemat memori daripada list

# membuat generator
def my_generator():
    for i in range(5):
        yield i
         
         
gen = my_generator()
print(next(gen)) # out: 0
print(next(gen)) # out: 1
print(next(gen)) # out: 2
print(next(gen)) # out: 3
print("\n")


# generator expression
gen_exp = (x**2 for x in range(5))
print(next(gen_exp)) # out: 0
print(next(gen_exp)) # out: 1
print(next(gen_exp)) # out: 4
print(next(gen_exp)) # out: 9
print(next(gen_exp)) # out: 16
print("\n")


# generator vs list
#menggunakan list
nums_list = [x**2 for x in range(1000000)]
# menggunakan generator
nums_gen = [x**2 for x in range(1000000)]


# ""generator penulisan ekspresinya sama dengan list""


# generator lebih hemat memori karena elemen dibuat saat di butuhkan, tidak langsung di simpan di RAM

# KESIMPULAN
# 1.) list comprehension adalah cara ringkas dan efisien untuk membuat list berdasarkan iterable dengan ekspresi dan kondisi

# 2.) dictionary menyimpan pasangan key value, mendukung iterasi, dan bisa digunakan untuk menyimpan data tersebut

# 3.) set digunakan untuk menyimpan elemen unik dan mendukung operasi matematika seperti union dan intersection

# 4.) tuple adalah struktur data yang mirip list tetapi immutable, cocok untuk menyimpan data yang tidak boleh di ubah

# 5.) memungkinkan pembuatan nilai satu per satu secara efisien, menghemat memori dibandingkan list biasa

#dengan memahami konsep konsep ini, kita bisa menulis kode python yang lebih efisien dan optimal

# yield = hasil
