def ceasar(text, amount):
    amount = int(amount)
    correction_amount = 26 - amount
    result = ""

    for letter in text:
        if letter.isalpha():
            if chr(ord(letter) + amount).isalpha():
                result += chr(ord(letter) + amount)
            else:
                result += chr(ord(letter) - correction_amount)
        else:
            result += letter
    return "The encrypted sentence is: " + result

print(ceasar(input("Please enter a sentence: "), input("Please enter cipher stepping amount: ")))