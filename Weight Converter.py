weight = input("Enter your Weight ")
type = input('Is it in (L)bs or (K)gs ')

if type.upper() == "L":
    print("Your weight =", 0.45 * float(weight))

elif type.upper() == "K":
    print("Your weight =", 2.20462 * float(weight))

else:
    print("Invalid input")

