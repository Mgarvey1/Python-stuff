class EmobilisStudent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def hello_me(self):
            print(f"My name {self.name} and I'm {self.age} years old")
#creating an object
myobj=EmobilisStudent("Marcus",17)
myobj.hello_me()

class Alliancehigh:
    def __init__(self,name,admission):
        self.name=name
        self.admission=admission
    def hello_me(self):
        print(f"My name {self.name} and my admission number is {self.admission} in Alliance high school")
myobject=Alliancehigh("Marcus Garvey", 13654)
myobject.hello_me()
myobject=Alliancehigh("Gideon Masek", 13555)
myobject.hello_me()
myobject=Alliancehigh("Timo Mpenda madem", 13245)
myobject.hello_me()

#create a class called magari, it should have model, make nd year properties
#create min of 3 objects

class magari:
    def __init__(self,model,make,year):
        self.model=model
        self.make=make
        self.year=year
    def cars(self):
        print(f"This ia a {self.model} {self.make} manufactured and assembled in the year {self.year} in Japan")
mycar=magari("Toyota","land cruiser",1990)
mycar.cars()
mycar=magari("BMW","X5",2022)
mycar.cars()
mycar=magari("Mercedes","Benz E250",2012)
mycar.cars()
mycar=magari("Rolls Royce","Phantom",2015)
mycar.cars()
mycar=magari("Lamborghini","Gallado",1978)
mycar.cars()

class



