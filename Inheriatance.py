#Inheritance:  Inheritance is a fundamental concept in OOP
# that allows a class to inherit attributes and methods from other class.

#Inheritance (Single Inheritance)
class car:      #parent class
    def __init__(self,windows,doors,enginetype):
        self.windows=windows;
        self.doors=doors;
        self.enginetype=enginetype;
    def drive(self):
        print(f'The person will drive the {self.enginetype} car');
car1=car(4,2,'patrol')
car1.drive()


class tesla(car):
    def __init__(self,windows,doors,enginetype,is_selfdriving):
        self.is_selfdriving=is_selfdriving;
        super().__init__(windows, doors, enginetype)
    def selfdriving(self):
        print(f'Tesla supports self driving: {self.is_selfdriving}')
tesla1=tesla(4,2,'patrol',True)
tesla1.selfdriving()

#Multiple Inheritance

#when a class inherite from more than one base classes
class animal:      #Parent Class 1
    def __init__(self,name):
        self.name=name;
    def speak(self):
        print('subclass must implement this method');

class pet:  #Parent Class 2
    def __init__(self,owner):
        self.owner=owner;


class dog(animal,pet):  #Base Class
    def __init__(self,name,owner):
        animal.__init__(self,name);
        pet.__init__(self,owner)
    def speak(self):
        print(f'{self.name} says woof')

#creat object
dog1=dog('dheeraj','woof')
dog1.speak()