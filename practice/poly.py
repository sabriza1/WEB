from abc import ABC, abstractmethod
class Employee (ABC):
    def __init__ (self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    @abstractmethod
    def work(self):
        pass

    def display_info(self):
        print(f"name: {self.name}, age: {self.age}, salary: {self.salary}" )


class Developer (Employee):
    def __init__ (self, name, age, salary, programming_language):
        super().__init__( name, age, salary)
        self.programming_language = programming_language

    
    def work(self):
        print(f"{self.name} пишет код на {self.programming_language}.")

class Manager (Employee):
    def __init__(self,name,age,salary,team_size):
        super().__init__(name,age,salary)
        self.team_size = team_size

    def work(self):
        print(f"{self.name} управляет командой из {self.team_size} человек.")

dev = Developer("Aida", 35, 4000, "python")
man = Manager("Maks", 30, 7000, "10")

dev.display_info()
dev.work()
 
man.display_info()
man.work()

#другой метод

from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def info(self):
        pass


class Developer(Employee):
    def work(self):
        return "Aida пишет код на Python."

    def info(self):
        return "Имя: Aida, Возраст: 35, Зарплата: 40000"

class Manager(Employee):
    def work(self):
        return "Maks управляет командой из 10 человек."

    def info(self):
        return "Имя: Maks, Возраст: 30, Зарплата: 70000"

def show_work(employee):
    print(employee.work())

def show_info(employee):
    print(employee.info())

show_work(Developer())
show_work(Manager())

show_info(Developer())
show_info(Manager())




    
        
