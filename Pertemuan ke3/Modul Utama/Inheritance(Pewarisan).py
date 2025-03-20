# INHERITANCE

"""
    Dengan Pewarisan (Inheritance), kita dapat mendefinisikan kelas yang 
mewarisi semua metode dan properti dari kelas lain, tanpa harus membuat kelas 
baru dari awal. Turunannya disebut kelas anak (child class) dan yang 
mewariskannya disebut kelas induk (parent class). Kelas anak mewarisi atribut dari 
kelas induk, dan kita bisa menggunakan atribut tersebut seolah atribut itu 
didefinisikan juga di dalam kelas anak. Kelas anak juga bisa menimpa (override) 
data dan metode dari induknya dengan data dan metodenya sendiri. Satu kelas 
anak bisa mewarisi karakteristik dari satu atau beberapa kelas induk.
"""

# Parent class : Person
class Person:
    def __init__(self, idnumber, name, address, gender):
        self.idnumber = idnumber
        self.name = name
        self.address = address
        self.gender = gender
        
    def get_name(self):
        print(self.name)
        
    def show_person(self):
        print('idnumber : ', self.idnumber) 
        print('name : ', self.name) 
        print('address : ', self.address) 
        print('gender : ', self.gender)
        
#child class : Employee(pegawai)
class Employee(Person):
    def __init__(self, idnumber, name, address, gender, job, department, salary):
        # memanggil __init__ kelas person menggunakan fungsi super()
        super().__init__(idnumber, name, address, gender)
        self.job = job
        self.department = department
        self.salary = salary
        
    def get_salary(self):
        print(f'salary : Rp {self.salary:,}')
        
    def show_employee(self):
        print('idnumber :', self.idnumber)
        print('name :', self.name)
        print('job :', self.job)
        print('department :', self.department)
        print('salary :', self.salary)
        
# membuat sebuah object (instance) dari kelas employee
pegawai1 = Employee('123', 'Akram Dhiya', 'Tangerang' , 'Laki-Laki', 'Data Engineer', 'Divisi IT', 5200000)
pegawai1.show_employee()
pegawai1.get_salary()

#OUTPUT
"""
idnumber : 123
name : Akram Dhiya
job : Data Engineer
department : Divisi IT
salary : 5200000
salary : Rp 5,200,000
"""
        
    
