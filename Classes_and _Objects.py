#Classes and Objects: OOP in programming paradigm that uses 'objects' to design applications and computer programs.
# OOP allows for modeling real-world scenarios using classes and objects.

#Instance Variable and Methods
class dog:
    def __init__(self,name,age):   #constructor
        self.name=name;
        self.age=age;

dog1=dog("mayank",3)
print(dog1)
print(dog1.name)
print(dog1.age)

#Define a class with instance method
class dog:
    def __init__(self, name, age):
        self.name=name;
        self.age=age;
    def bark(self):
        print(f'{self.name} says woof');
dog1=dog('mayank',3)
dog1.bark();

#Modeling a bank account

class bank:
    def __init__(self,owner,balance=0):
        self.owner=owner;
        self.balance=balance;
    def deposit(self,amount):
        self.balance+=amount;
        print(f'Deposited {amount} to {self.owner}\'s account. New balance is {self.balance}');
    def withdraw(self, amount):
        if amount>self.balance:
            print('Insufficient Balance');
        else:
             self.balance-=amount;
             print(f'Withdrawed {amount} from {self.owner}\'s account. New balance is {self.balance}');
    def get_balance(self):
        return self.balance;
bank1=bank('nitish',10000)
bank1.deposit(400);
bank1.withdraw(2000)
print(bank1.get_balance())






