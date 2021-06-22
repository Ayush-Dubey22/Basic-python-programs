import random

print(random.randint(1, 6))
while True:
    start = input('Roll the dice? (Y/N):  ').upper()
    if start == 'Y':
        print(random.randint(1, 6))
    if start == 'N':
        print('Goodbye')
        break
else:
    print('')