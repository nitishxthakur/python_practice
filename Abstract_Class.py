#Abstract Class : abstract class is a class that contains one or more abstract method
# is called abstract class.
#Note:
#(i) an object of an abstract class can not be created.
#(ii)python provides 'abc' module to work with abstraction.
#(iii)we use @astractmethod decorator to define abstract method.
#(iv) we use abstract method when action is common but impletentation is different.


from abc import ABC, abstractmethod
class car(ABC):
    def show(self):
        print('every car has 4 wheels');
        @abstractmethod
        def speed(self):  #abstract method, every car has some speed but it's vary. that's why we don't pass any fixed value here.
            pass
class maruti(car):
    def speed(self):      #implementation1, maruti has different speed
        print('maruti speed is 100km/h');
class suzuki(car):   #implementaion2, suzuki has different speed.
    def speed(self):
        print('suzuki speed is 70km/h');
obj=maruti()
obj.show()
obj.speed()