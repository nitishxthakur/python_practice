#Polymorphism : Polymorphism provides a way to perform a single action in different forms.
# Polymorphism is typically achived through method overriding and interfaces.

#Method Overloding: Whenever class contains more than one methods with same
# name and different types parameters called overloading.

class A:
    def show(self):
        print('Welcome');
    def show(self, firstname=''):
        print('Welcome', firstname);
    def show(self,firstname='', lastname=''):
        print('welcome', firstname, lastname);
obj=A();
obj.show()
obj.show('nitish')
obj.show('nitish','thakur')
