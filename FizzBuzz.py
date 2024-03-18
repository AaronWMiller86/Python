# FizzBuzz
# Write a Python program that prints the numbers from 1 to 100. If the number is divisible by 3 print Fizz, if the number is divisible by 5 print Buzz instead of the number. If the number is divisible by 3 and 5 print FizzBuzz instead of the number.

i = 1
while i < 101:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1