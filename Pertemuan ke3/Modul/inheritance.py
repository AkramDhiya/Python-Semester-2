class mobil:
    def __init__(self, merek, model, negara, tahun):
        self.merek = merek
        self.model = model
        self.negara = negara
        self.tahun = tahun

class MobilSport(mobil):
    def __init__(self, merek, model, negara, tahun, kecepatan_maks):
        super().__init__(merek, model, negara, tahun)
        self.kecepatan_maks = kecepatan_maks
    
    def deskripsi(self):
        return f"mobil {self.merek} {self.model} keluaran negara {self.negara} tahun {self.tahun} dengan kecepatan maksimal {self.kecepatan_maks} km"
    
#membuat objek darai class mobilsport
MobilSport1 = MobilSport("Ferrari", "4356", "prancis", 2006, 140)
print(MobilSport1.deskripsi())