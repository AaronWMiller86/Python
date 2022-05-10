def merge(a, b):
    a.extend(b)
    a.pop(3)
    a.pop(3)
    a.pop(3)
    a.sort()
    return a


merge([1, 3, 5, 0, 0, 0], [2, 4, 6])


def swap(a, b):
    b = a + b
    a = b - a
    b = b - a
    return a, b


swap(5, 7)


def roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    numeral = ""
    i = 0

    while num > 0:
        for _ in range(num // val[i]):
            numeral += syb[i]
            num -= val[i]
        i += 1
    return numeral


roman(465)


def anagram(a, b):
    a = a.lower()
    b = b.lower()

    if sorted(a) == sorted(b):
        return True
    return False


anagram("silent", "listen")


def fizzbuzz(x):
    y = 1
    while y <= x:
        if y % 5 == 0 and y % 3 == 0:
            print("FizzBuzz")
        elif y % 3 == 0:
            print("Buzz")
        else:
            print(y)
        y += 1

#fizzbuzz(16)


def compress(string):
    res = ""
    count = 1

    res += string[0]
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            count += 1
        else:
            if count > 1:
                res += str(count)
            res += string[i+1]
            count = 1
    if count > 1:
        res += str(count)
    return res


compress("abbcc")

def median(a, b):
    a.extend(b)
    a.sort()
    if len(a) % 2 == 0:
        x = len(a) // 2
        y = (len(a) // 2) - 1
        return (a[x] + a[y]) / 2
    else:
        x = len(a) // 2
        return a[x]


median([1,3,5,10], [2,4,6])


def missing(n, a):
    a.sort()
    res = []
    i = 1
    while i < n + 1:
        if i not in a:
            res += str(i)
        i += 1
    return str(a) + " = " + (", ".join(res))


print(missing(6, [2,3,4]))

