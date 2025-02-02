user={"first_name":"nitish","last_name":"thakur", "id":"0"}
print(user)

all_users=user.items()
print(all_users)

for k,v in user.items():
    print(f'key:{k.title()}')
    print(f'value:{v.title()}')
print(user['first_name'])

positive_int={x:x**2 for x in range(10)}
print(positive_int)

#Accessing dictionary elements
print(positive_int[5])
print(positive_int.keys())

#adding and deltion of items
positive_int[11]=121   #add 11:121 key value pair
del positive_int[1]    #delete 1 key value pair
print(positive_int)

#iteration over dictionary
for y,z in positive_int.items():
    print(f'{y}:{z}')

#dictionary comprihansion
cube_val={x:x**3 for x in range(10)}
print(cube_val)

#merge two dictionaries
sqr_val1={x:x**2 for x in range(5)}
sqr_val2={x:x**2 for x in range(5,10)}
merge_val12={**sqr_val1,**sqr_val2}
print(merge_val12)