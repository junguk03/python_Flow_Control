person = {'name':'uk', 'address':'Seoul', 'interest':'Web'}
print(person['name'])

for say in person:
    print(say, person[say])

persons = [
    {'name':'egoing', 'address':'Seoul', 'interest':'Web'},
    {'name':'basta', 'address':'Seoul', 'interest':'IOT'},
    {'name':'blackdew', 'address':'Tongyeong', 'interest':'ML'}
]

print('------persons--------')
for people in persons:
    for say in people:
        print(say, ':', people[say])
    print('--------------------')