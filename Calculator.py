amount = float(input('Enter first amount '))
amount2 = float(input('Enter second amount '))
unit = input('What do you want to do? (EG:- +, -, *, /) ')

if unit == ('+') :
    x = amount + amount2
    print(x)

elif unit == ('-') :
    y = amount - amount2
    print(y)

elif unit == ('*') :
    z = amount * amount2
    print(z)

elif unit == ('/') :
    q = amount / amount2
    print(q)

else:
    print('Invalid input')