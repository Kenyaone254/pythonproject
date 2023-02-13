def calculator(c,d):
    if type(c) == int and type(d) == int:
        sum = c + d
        difference = c - d
        product = c * d
        if d == 0:
            return "division by zero not allowed"
        else:
            division = c / d
            if c == d:
                return "c and d are equal\n sum: {}\n difference: {}\n product: {}\n division: {}".format(sum,difference,product,division)
            else:
                return "sum: {}\n difference: {}\n product: {}\n division: {}".format(sum,difference,product,division)
    else:
        return "invalid inout"
    c = int(input(" Enter number c "))
    d = int(input("Enter number d"))

    print(calculator(c, d))

