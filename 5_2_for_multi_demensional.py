persons = [
    ['egoing', 'seoul', 'Web'],
    ['basta', 'Seoul', 'IOT'],
    ['blackdew', 'Tongyeong', 'ML'],
]
print(persons[0][0])

for name, address, interest in persons:
    print(name+' lives in '+address+'. he likes '+interest)

name, address, interest = ['egoing', 'seoul', 'Web']
print(name, address, interest)