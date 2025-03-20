#

# CLASS AND OBJECT

"""
    Kelas (Class) pada bahasa Python dapat dikatakan sebagai cetak biru 
(blueprint) dari object (atau instance) yang ingin dibuat. Kelas adalah cetakannya 
atau definisinya, sedangkan obyek (atau instance) adalah obyek nyatanya. Atribut 
merepresentasikan variabel yang dimiliki oleh sebuah obyek. Sedangkan perilaku 
merepresentasikan fungsi yang dimiliki sebuah obyek.
"""

class Kendaraan:
    def __init__(self, merk, type, warna, harga):
        self.merk = merk
        self.type = type
        self.warna = warna
        self.harga = harga
        
    def get_harga(self):
        print(f"Harga : Rp {self.harga:,}")
        
    def tampil_profil(self):
        print('merek :', self.merk)
        print('type :', self.type)
        print('warna :', self.warna )
        print('harga :', self.harga )
        
# Membuat sebuah object (instance) dari kelas kendaraan
MyCar = Kendaraan('Toyota', 'Sedan', 'Merah', 1850000000) 
MyCar.tampil_profil()
MyCar.get_harga()

#OUTPUT
"""
merek : Toyota
type : Sedan
warna : Merah
harga : 1850000000
Harga : Rp 1,850,000,000
"""