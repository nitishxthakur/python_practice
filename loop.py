for i in range(21):
    print(i)

for j in range(2,21,3):
    print(j)

names=['nitish','somendra','akhilesh','mayank','dheeraj']
for i in names:
    print(i)
    print(i.title())

for name in names:
    for word in name:
        print(word)


while True:
    first_name=input('Enter your first name:');
    if first_name=='Quit':
        break;
    last_name=input('Enter your last name:');
    full_name=[]
    full_name.append(first_name)
    full_name.append(last_name)
    names.append(full_name)
print(names)




