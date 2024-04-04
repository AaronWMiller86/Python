def ceasar(text, amount):
    amount = int(amount)
    correction_amount = 26 - amount
    result = ""

    for letter in text:
        if letter.isalpha():
            if chr(ord(letter) + amount).isalpha():
                unicode = ord(letter) + amount
                result += chr(unicode)
            else:
                unicode = ord(letter) - correction_amount
                result += chr(unicode)
        else:
            result += letter
    return "The encrypted sentence is: " + result.lower()

print(ceasar(input("Please enter a sentence: "), input("Please enter cipher stepping amount: ")))