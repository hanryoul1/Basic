def three():
    print("three", end = " ")
    return 3

def five():
    print("five", end = " ")
    return 5

def seven():
    print("seven", end = " ")
    return 7

# main code
three() > five() > seven() # (3 > 5) & (5 > 7)