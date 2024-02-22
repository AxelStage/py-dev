"""
interview coding challange:
Write a programm that prints out the numbers from 1 to 100.
But for multiples of three print out "fizz" instead of the number and for multiples of five print "buzz".
For numbers that are multiples of both print "fizzbuzz"
"""


# version 1
def fizzbuzz_v1():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)


# version 2
def fizzbuzz_v2():
    for number in range(1, 101):
        if number % (3 * 5) == 0:
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)


# version 3
def fizzbuzz_v3():
    for number in range(1, 101):
        if number % 3 == 0:
            if number % 5 == 0:
                print("fizzbuzz")
            else:
                print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)


# testing
fizzbuzz_v2()
