#lambda function is small anonymous function defined using the lambda keyword.
#they can have any number of arguments but only one expression.
from win32ui import types

sqr=lambda x:x**2;
print(sqr(5))

sum_value=lambda x,y,z:x+y+z;
print(sum_value(3,4,5))

odd_num=lambda num:num%2!=0;
print(odd_num(8))

#a map function applies a given function to all items in an input list or any other
#iterable and returns a map object.this is particularly useful for transforming data
#in a list comprenhensively.

def square(num):
    return num*num;
nums=[1,2,3,4,5]

print(list(map(square, nums)))

sq=list(map(lambda x:x*x,nums))
print(sq)

nums1=[1,2,3,4]
nums2=[5,6,7,8]
sum1=list(map(lambda x,y:x+y, nums1,nums2))
print(sum1)

str1=['1','2','3','4']
int1=list(map(int,str1))
print(type(int1[1]))

words=['apple','banana','cucumber','dragon fruit']
words1=list(map(str.upper,words))
print(words1)


def get_name(person):
    return(person['name']);
person=[
    {'name':'krish','age':32},
    {'name':'jack','age':33}
]
names=list(map(get_name,person))
print(names)


#The filter function constructs an iterator from elements of an iterable
#for which a function return true. it is used to filter out items from a
#list based on a condition.

def even(num):
    if num%2==0:
        return True;
lst=[1,2,3,4,5,6]
even_lst=list(filter(even, lst))
print(even_lst)

#filter with lambda function
nums3=[1,2,3,4,5,6,7,8,9]
greater_than_five=list(filter(lambda x:x>5,nums3))
print(greater_than_five)

#filter with a lambda function and multiple conditions
nums4=[1,2,3,4,5,6,7,8,9,10]
even_and_greater_than_five=list(filter(lambda x:x>5 and x%2==0, nums4))
print(even_and_greater_than_five)

#filter to check if the age is greater than 25 in dictionaries
people=[
    {'name':'krish','age':32},
    {'name':'jack','age':33}
]
def age_greater_than_25(person):
    return person['age']>25
name_list=list(filter(age_greater_than_25, people))
print(name_list)