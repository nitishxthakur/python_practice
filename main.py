name='nitish KUmar ThakuR'
name2=' nitish KUmar ThakuR   '
print(name)
print(name.upper())
print(name.lower())
print(name.title())
print(f'My name is {name.title()}')
print(f'\tMy name is- {name.title()}');
print(f'\nMy name is-- {name.title()}');

# rstrip removes whitespaces from right side
print(f'My name is {name2.rstrip().title()}');

# lstrip removes whitespaces from left side
print(f'My name is{name2.lstrip().title()}');

#strip removes whitespaces from both left & right sides
print(f'My name is {(name2.strip()).title()}');

linkdin_link='https://www.linkedin.com/in/nitishxthakur/'
print(f'\tMy name is {name.title()}\n\tI study in Amity Universiy Gurugram\n\tMy linkdin link is {linkdin_link.strip()}')



