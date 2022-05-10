import re


def conversion(temp):

    if re.search("C$", temp):
        celsius = re.sub("C$", "", temp)
        print(str(round(int(celsius) * 9 / 5 + 32, 2)) + u'\N{DEGREE SIGN}' + "F")

    elif re.search("F$", temp):
        fahrenheit = re.sub("F$", "", temp)
        print(str(round((int(fahrenheit) - 32) / 1.8, 2)) + u'\N{DEGREE SIGN}' + "C")

    else:
        print("Please include the temperature scale (C or F)")


conversion(input("Enter Temperature and Scale: "))
