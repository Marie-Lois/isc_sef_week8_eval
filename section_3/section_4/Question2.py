def factorial(a):
    for i in range(a):
        a = a * (a - 1)
        print(a)
factorial(3)