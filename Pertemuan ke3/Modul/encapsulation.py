# Encapsulation menyembunyikan detail implementasi dan hanya menampilkan bagian yang diperlukan melalui modifier public, protected, dan private

class BankAkun:
    
    def __init__(self, pemilik, saldo):    
        self.pemilik = pemilik # Public Attribut
        self.__saldo = saldo   # Private Attribut
    
    def deposite(self, jumlah):
        self.__saldo += jumlah
        return f"deposit sebesar {jumlah}, saldo baru: {self.__saldo}"
    
    def __CekSaldo(self):
        return f"saldo {self.pemilik}: {self.__saldo}"
    
    def TampilkanSaldo(self):
        return self.__CekSaldo()
    
# Membuat objek dari class BankAkun
akun1 = BankAkun("Akram", 10000000)
print(akun1.TampilkanSaldo())

# Output = 