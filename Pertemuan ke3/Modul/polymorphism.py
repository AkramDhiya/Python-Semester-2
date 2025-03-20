# Polymorphism memungkinkan method yang sama digunakan oleh class yang berbeda, dengan implementasi yang berbeda

class Kendaraan:
    def bergerak(self):
        return "Kendaraan sedang bergerak"
    
class Mobil(Kendaraan):
    def bergerak(self):
        return "Mobil sedang berjalan di jalan raya"
    
class Pesawat(Kendaraan):
    def bergerak(self):
        return "Pesawat sedang terbang di udara"
    
# Polymorphism dengan looping
Kendaraan = [Mobil(), Pesawat()]
for k in Kendaraan:
    print(k.bergerak())
    
# Output =

# Penjelasan =
# Mobil dan Pesawat adalah subclass dari Kendaraan

# Method bergerak() memiliki implementasi berbeda pada masing-masing class.

# saat looping, python secara otomatis memanggil method bergerak() yang sesuai dengan objeknya