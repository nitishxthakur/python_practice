#Interface: Interface is nothing but an abstract class which
# contains only abstract method but not any normal method.
#note: (i) we can't create object of interface;
      #(ii) we use interface, when an action is common but implementation is different.
      #(iii) all child class should be inherite abstract method.


from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def show(self):
        pass


class square(shape):
    def show(self):
        print('square has square shape');

class circle(shape):
      def show(self):
          print('circle has circle shape');

c=circle()
c.show()

s=square()
s.show()