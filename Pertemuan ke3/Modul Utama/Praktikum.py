class Person:
    def __init__(self, nama, umur, telepon):
        self.nama = nama
        self._umur = umur # protected attribute
        self.__telepon = telepon # private attribute
        
    def get_telepon(self): # getter untuk telepon
        return self.__telepon 
    
    def set_telepon(self, new_telepon): # setter untuk telepon
        self.__telepon = new_telepon 
        
    def _show_umur(self): # mengakses atribut umur
        return f"umur : {self._umur}"
    
    def _show_telepon(self): # private method untuk menampilkan telepon
        return f"telepon : {self.__telepon}"
    
    def show(self):
        umur_info = self._show_umur()
        telepon_info = self._show_telepon() # memanggil method
        return f"nama : {self.nama}, {umur_info}, {telepon_info}"
    
# Jelaskan nama kelas, atribut dan metode yang ada pada kelas tersebut! 
"""
nama kelas ini adalah person,
atribut dalam kelas person ada 3 jenis :
public attribute, bisa di akses dari mana saja contohnya self.nama = nama
protected attribute, digunakan di dalam kelas person atau turunannya contohnya 
private attribute, tidak bisa di akses langsung di luar kelas contohnya self.__telepon = telepon

get_telepon() (public) -> getter untuk __telepon
set_telepon(new_telepon) (public) -> setter untuk __telepon
show() (public) -> menampilkan informasi lengkap
_show_umur() (protected) -> mengembalikan informasi umur
__show_telepon() (private) -> mengembalikan informasi telepon

konsep nya yaitu
- engkapsulation (menyembunyikan atribut __telepon dengan private access)
- protected vs private (perbedaan aksesbeilitas _umur dan __telepon)
- getter dan setter untuk mengakses atribut yang bersifat private
"""
# subclass dari person
class lecture(Person):
    def __init__(self, nama, umur, telepon):
        super().__init__(nama, umur, telepon) #memanggil konstruktor parent
        self.__honor = 0 # private attribute
        
    def set_honor(self, honor):  #setter method
        self.__honor = honor
        
    def get_honor(self):         #getter method
        return self.__honor

"""
atribut dalam kelas lecture
self.honor (private attribut), sehingga hanya dapat di akses dari dalam kelas itu
digunkan untuk menyimpan honor dari seorang dosen

method dalam kelas lecture
def set_honor(self, honor) -> setter method
    digunakan untuk menetapkan nilai atribut __honor
def get_honor(self)        -> getter method
    digunakan untuk mengambil (mengembalikan) nilai dari __honor
"""
# membuat objek dari kelas person
person1 = Person("Akram", 19, '123456789')
print('nama :', person1.nama)
print('telepon :', person1.get_telepon())
person1.set_telepon('08121233293')
print('telepon baru :', person1.get_telepon())
print(person1._show_umur())
print(person1.show())

# membuat objek dari kelas lecture
lecture1 = lecture("afrizal", 32, "9283248343")
lecture1.set_honor(50000)
print('Honor :', lecture1.get_honor())    