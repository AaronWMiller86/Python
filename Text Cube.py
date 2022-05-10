def text_cube(phrase):
    i = 0
    while i < len(phrase):
        if phrase[i] == " ":
            print("")
        else:
            print(phrase.replace(str(phrase[0]), phrase[i]).upper())
        i += 1


text_cube(input("Enter Phrase: "))

