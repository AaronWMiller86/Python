# Matrix Builder
rows = int(input("How many rows does the matrix have? "))
columns = int(input("How many columns does the matrix have? "))
matrix = []

print("Enter matrix data row by row: ")
for row in range(rows):
    data = []
    for column in range(columns):
        data.append(int(input()))
    matrix.append(data)

# Matrix Print Loop
for row in range(rows):
    for column in range(columns):
        print(matrix[row][column], end=" ")
    print()

# Sum of each row
for row in range(rows):
    print("The sum of row " + str(row + 1) + " is: " + str(sum(matrix[row])))