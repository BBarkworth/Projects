for i in range(1, 101):
    if i % 15 == 0:
        print("Fizzbuzz", i)
    elif i % 5 == 0:
        print("Buzz", i)
    elif i % 3 == 0:
        print("Fizz", i)
    else:
        print(i)