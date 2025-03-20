class Customer:
    def __init__(self, idnumber, nama, telepon):
        self.idnumber = idnumber
        self.nama = nama
        self.telepon = telepon
        
    def _tampil_profil(self): # protected method
        print(f"ID : {self.idnumber}, Nama: {self.nama}, telepon : {self.telepon}")
        
class Member(Customer):
    def __init__(self, idnumber, nama, telepon, hrgmember, diskon):
        super().__init__(idnumber, nama, telepon)
        self.hrgmember = hrgmember
        self.diskon = diskon
        
    def __get_hargamember(self):# Private Method
        return f"Harga Member : {self.hrgmember}"
   
    def __get_diskon(self):# Private Method
        return f"Diskon Member : {self.diskon}%" 
        
    def tampilkan_info_member(self): # Public Method untuk akses Private Method
        self._tampil_profil()
        print(self.__get_hargamember())
        print(self.__get_diskon())
        
class NonMember(Customer):
    def __init__(self, idnumber, nama, telepon, hrgnonmember): 
        super().__init__(idnumber, nama, telepon)
        self.hrgnonmember = hrgnonmember
        
    def __get_harganonmember(self): # Private Method 
        return f"Harga Non member : {self.hrgnonmember}"      
    def tampilkan_info_nonmember(self): # Public method untuk akses ke private
        self._tampil_profil()
        print(self.__get_harganonmember())
        
#contoh penggunaan program
print("Data Member : ")
member1 = Member("MEM87", "Akram", "098342423423", 70000, 10)
member1.tampilkan_info_member()

print("\nData Non Member : ")
nonmember1 = NonMember("NOMEM67", "kuapi", "09834533423", 90000)
nonmember1.tampilkan_info_nonmember()