# ENCAPSULATION
"""
    Enkapsulasi adalah proses menggabungkan atribut dan metode dalam satu unit. 
Konsep ini adalah salah satu pilar utama yang menjadi dasar paradigma pemrograman 
berorientasi object. Hal ini memungkinkan terciptanya objek dengan serangkaian 
atribut dan perilaku yang telah ditentukan sebelumnya yang dapat diakses dan diubah 
dengan cara yang terkendali. Kita tahu bahwa kelas adalah prototipe yang ditentukan 
pengguna untuk suatu object. Kelas mendefinisikan sekumpulan atribut data dan 
metode, yang mampu memproses data.

  
    Enkapsulasi adalah teknik untuk menyembunyikan operasi internal suatu kelas 
dan hanya memperlihatkan informasi yang diperlukan untuk interaksi eksternal. Hal 
ini memungkinkan terciptanya object dengan perilaku dan properti yang ditetapkan 
dengan jelas, sehingga meningkatkan kegunaan dan keamanannya. Enkapsulasi 
membatasi akses ke data kelas hanya pada metodenya dan menjaga variabel kelas 
tetap bersifat private.
"""


# 1.) Public Access Modifier
"""
Publik Member adalah variabel dan metode yang dapat diakses dari mana saja 
dalam suatu kelas, yaitu, baik di luar maupun di dalam kelas dan dari bagian 
mana pun dari suatu program. Mereka adalah anggota default dan ditentukan 
tanpa kata kunci eksplisit apa pun. 
"""

class MyClass:
    def __init__(self, value):
        self.value = value # Public Attribute 
    
    def show_value(self):   # Public Method
        print(self.value)
    
# Create an object
Object1 = MyClass(10)

# Accessing Public Method
Object1.show_value()

# Accessing Public Attribute
print(Object1.value)

# OUTPUT = 10
#          10

# 2.) PROTECTED ACCESS MODIFIER
"""
Anggota atau variabel kelas yang hanya dapat diakses di dalam kelas dan 
subkelasnya dan tidak di luar kelas disebut anggota terlindungi. Anggota ini 
ditandai dengan awalan nama mereka dengan satu garis bawah ‘_’. Perbedaan 
antara anggota terlindungi dan anggota privat adalah bahwa yang pertama dapat 
diakses di dalam kelas dan melibatkan subkelas, tidak seperti variabel privat. 
Dengan pengubah akses privat, anggota dapat dirujuk di dalam kelas dan subkelas 
berikutnya. Begitu objek kelas dibuat, ia menjalankan metode _init_
"""

class BaseClass:
    def __init__(self, value):
        self._value = value # Protected attribute
        
    def _show_value(self):  # Protected Method
        print(self._value)

class SubClass(BaseClass):
    def display(self):
        self._show_value() # Accessing Protected method from subclass
        
# Create an object
objectt1 = SubClass(20)

# Accessing protected method via public method in subclass
objectt1.display()

# Accessing protected attribute directly (not recommended)
print(objectt1._value)

# OUTPUT = 20
#          20

# 3.) PRIVATE ACCESS MODIFIER
"""
Private Member dalam enkapsulasi adalah variabel yang hanya dapat 
diakses di dalam kelas. Mereka mirip dengan protected member, tetapi yang 
membedakan private member adalah mereka tidak dapat diakses di luar kelas 
atau oleh kelas dasar mana pun. Dalam Python, Anda tidak akan menemukan 
variabel instance private yang tidak dapat diakses kecuali di dalam kelas. Kita 
dapat mendefinisikan pengubah akses private dengan memberi awalan garis 
bawah ganda ‘__’ pada member private. Selain itu, private member dan 
protected member dapat diakses di luar kelas melalui manipulasi nama dalam 
Python.
"""

class MyClass1:
    def __init__(self, value):
        self.__value = value #Private attribute
        
    def __show_value(self):
        print(self.__value)  #Private method
        
    def public_method(self): #Public method
        self.__show_value()  # Acessing private method within the class
        
# crate an object
objecttt1 = MyClass1(30)

# Access private method through a public method
objecttt1.public_method()

#OUTPUT = 30 