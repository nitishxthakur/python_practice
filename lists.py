
names=['nitish','somendra','akhilesh','mayank','dheeraj']
print(names)
names.append('aman')
print(names)

names.insert(0,'amity')
print(names)

print(f'First Member of the list is {names[0].title()}')
print(f'Last Member of the list is {names[-1].title()}')

names.pop()
print(names)

names.pop(0)
print(names)

names.remove('akhilesh')
print(names)

names.sort()
print(names)
print(f'This name list is sorted {sorted(names)}')

names.reverse()
print(names)

print(names)
print(names[0:-2])
print(names[:-2])
print(names[2:])

numberlist=list(range(0,35))
print(numberlist)

numberlist2=list(range(0,35,5))
print(numberlist2)