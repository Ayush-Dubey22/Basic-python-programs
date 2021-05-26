name = input("Enter your name ")

if len(name) < 3:
    print('Name is too short, must be longer than 3')

elif len(name) <= 50:
    print('Name is fine')

else:
    print('Name is too long')
