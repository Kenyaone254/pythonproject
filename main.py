def number_check(a = 1, b = 2):
    if type (a) == int and type (b) == int:
        if a == b:
            return "a and b are equal"
        elif a > b:
            return "a is greater than b"
        elif b > a:
            return "b is greater than a"
        else:
            return "Invalid input"

a = int(input(" Enter number a "))
b = int(input("Enter number b"))

print(number_check(a,b))
