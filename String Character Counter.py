x = "My test line again."
counter = 0
i = 1

while i < len(x):
    if x == ' ':
        i += 1
    else:
        counter += 1
        i += 1

print(counter)