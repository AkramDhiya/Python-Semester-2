# Pemrograman Berorientasi Objek (OOP) adalah paradigma pemrograman yang berfokus pada objek

# Class adalah blueprint atau cetak biru untuk membuat objek. 
# Class mendefinisikan properti (atribut) dan fungsi (method) dari suatu objek

class mobil:
    def __init__(self, merek, model, negara, tahun):
        self.merek = merek
        self.model = model
        self.negara = negara
        self.tahun = tahun
        
    def deskripsi(self):
        return f"mobil {self.merek} {self.model} keluaran {self.negara} tahun {self.tahun}"
    
#membuaat objek dari class mobil
mobil1 = mobil("piguet", "408", "prancis", 3042)
print(mobil1.deskripsi())

# Output = 


