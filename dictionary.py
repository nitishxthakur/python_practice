user={"first_name":"nitish","last_name":"thakur", "id":"0"}
print(user)

all_users=user.items()
print(all_users)

for k,v in user.items():
    print(f'key:{k.title()}')
    print(f'value:{v.title()}')
print(user['first_name'])


