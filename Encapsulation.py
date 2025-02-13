#Encapsulaion : Encapsulation is the concept of wrapping data and methods together
# as a single unit . It restricts direct access to some of the object's components,
# which is a means of preventing accidental interference and misuse of data.

#By using encapsulation, we can restrict the variables and methods access globally
# by making it private or protected.

#single underscore(_): protected.
#double underscore(__): private.


class A:
    _a=10;
    __b=20;
    def show(self):
        print(f'a={self._a}');
        print(f'b={self.__b}');
obj=A();
obj.show()
print(f'outside of class {obj._a}')
print(f'outside of class {obj.__b}')