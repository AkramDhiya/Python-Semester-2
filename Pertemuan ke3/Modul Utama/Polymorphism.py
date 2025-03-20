# POLYMORPHISM

"""
    Polymorphism berasal dari bahasa Yunani, yaitu Poly = banyak (many) 
dan Morph = bentuk (forms). Istilah Polymorphism secara harfiah berarti 
“berbagai bentuk atau banyak bentuk”. Polimorphism adalah konsep dasar dalam 
pemrograman yang memungkinkan entitas (seperti : fungsi, method atau 
perilaku) berperilaku berbeda berdasarkan jenis data yang ditangani atau entitas 
dengan nama yang sama yang dapat dieksekusi pada banyak object atau kelas. 

    Keuntungan utama dari polimorfisme adalah memungkinkan kita untuk 
menulis kode yang lebih generik dan dapat digunakan kembali (reusable code).
"""

class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        
    def move(self):
        print('Drive!...')
        
class Boat:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        
    def move(self):
        print('Sail!...')

class Plane:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        
    def move(self):
        print('Fly!...')
        
# Create a Car, boat, plane Objek
Car1 = Car("Ford", "Mustang", 30920)
Boat1 = Boat("Ibiza", "Touring 20", 231086)
Plane1 = Plane("Boeing", "747", 386300)

for x in(Car1, Boat1, Plane1):
    x.move()
    


# OUTPUT :  Drive!...
#           Sail!...
#           Fly!...

""" Kita dapat membuat Polymorphism berdasarkan contoh kasus diatas, dengan membuat kelas Vehicle dan method move(), 
dimana kelas anak akan mewarisi semua method yang dimiliki oleh kelas Vehicle, tetapi dapat menggantinya """

class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        
    def move(self):
        print('Car is Move!...')
        
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print('Boat is Sail!...')

class Plane(Vehicle):
    def move(self):
        print('Plane is Fly!...')
        
# Create a Car, boat, plane Objek
Car1 = Car("Ford", "Mustang", 30920)
Boat1 = Boat("Ibiza", "Touring 20", 231086)
Plane1 = Plane("Boeing", "747", 386300)

for x in(Car1, Boat1, Plane1):
    print(f"Brand  : {x.brand}")
    print(f"Model  : {x.price}")
    print(f"prince : {x.price}")    
    x.move()
    print("\n")
    
"""
OUTPUT =
Brand  : Ford
Model  : 30920
prince : 30920
Car is Move!...


Brand  : Ibiza
Model  : 231086
prince : 231086
Boat is Sail!...


Brand  : Boeing
Model  : 386300
prince : 386300
Plane is Fly!... 

"""