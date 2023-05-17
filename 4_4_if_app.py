input_id = input("id: ")
id = 'junguk'
input_password = input('password: ')
password = '1111'
if input_id == id:
    if input_password == password:
        print("Welcome, junguk")
    else:
        print("wrong password")    
else:
    print("wrong id")