def fibonacci(n):
    count = 0
    i = 1
    x = 0
    while count < int(n):
        y = i + x
        x = i
        i = y
        count += 1
    return x


print(fibonacci(10))