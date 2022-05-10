scram_dict = {
    "a": "z",
    "e": "v",
    "i": "r",
    "o": "l",
    "u": "f",
}


def scramble(phrase):
    for key in scram_dict:
        phrase = phrase.replace(key, scram_dict[key])
    return phrase


print(scramble(input("Enter phrase to scramble: ")))


def unscramble(phrase):
    for key in scram_dict:
        phrase = phrase.replace(scram_dict[key], key)
    return phrase


print(unscramble(input("Enter phrase to unscramble: ")))
