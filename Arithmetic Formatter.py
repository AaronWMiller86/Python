import re


def arithmetic_arranger(problems, display=False):
    # List to String Conversion /w Seperator.
    stringed = '#'.join(problems)

    # Problem Count
    count = stringed.count('#')

    # Cleaned String to List Conversion
    workable = stringed.replace('#', ' ').split()

    z = "{:>9}"

    # Function for the length of the problem line (in dashes).
    def num_dashes(var1, var2):
        line = []
        if int(var1) > int(var2):
            dash = 0
            while dash < (len(var1) + 2):
                line.append("-")
                dash += 1
            return "".join(line)
        else:
            dash = 0
            while dash < (len(var2) + 2):
                line.append("-")
                dash += 1
            return "".join(line)

    # Function for Problem Solution.
    def solutions(operator, var1, var2):
        if operator == "+":
            return int(var1) + int(var2)
        else:
            return int(var1) - int(var2)

    # Function for the space between operator and second number.
    def op_space(var1, var2):
        space = []
        if len(var1) > len(var2):
            x = (len(var1) - len(var2)) + 1
            y = 0
            while y < x:
                space.append(" ")
                y += 1
            return "".join(space)
        else:
            x = 1
            y = 0
            while y < x:
                space.append(" ")
                y += 1
            return "".join(space)

    # Problem Limit Check
    if count > 4:
        return 'Error: Too many problems.'

    # Digits Only Check
    elif re.search('[a-zA-Z]', stringed):
        return 'Error: Numbers must only contain digits.'

    # Operator Check

    elif re.search('[(*/)]', stringed):
        return "Error: Operator must be '+' or '-'."

    # if 5 Problems
    elif count == 4:
        a, b, c, d, e, f = workable[0], workable[1], workable[2], workable[3], workable[4], workable[5]
        g, h, i, j, k, l = workable[6], workable[7], workable[8], workable[9], workable[10], workable[11]
        m, n, o = workable[12], workable[13], workable[14]

        if int(a) > 9999 or int(c) > 9999 or int(d) > 9999 or int(f) > 9999:
            return 'Error: Numbers cannot be more than four digits.'

        elif int(g) > 9999 or int(i) > 9999 or int(j) > 9999 or int(l) > 9999:
            return 'Error: Numbers cannot be more than four digits.'

        elif int(m) > 9999 or int(o) > 9999:
            return 'Error: Numbers cannot be more than four digits.'

        elif display is True:
            first_row = z.format(str(a)) + z.format(str(d)) + z.format(str(g)) + z.format(str(j)) + z.format(str(m)) + "\n"
            second_row = z.format(str(b) + str(op_space(a, c)) + str(c)) + z.format(
                str(e) + str(op_space(d, f)) + str(f)) + z.format(str(h) + str(op_space(g, i)) + str(i)) + z.format(
                str(k) + str(op_space(j, l)) + str(l)) + z.format(
                str(n) + str(op_space(m, o)) + str(o)) + "\n"
            third_row = z.format(str(num_dashes(a, c))) + z.format(str(num_dashes(d, f))) + z.format(
                str(num_dashes(g, i))) + z.format(str(num_dashes(j, l))) + z.format(str(num_dashes(m, o))) + "\n"
            forth_row = z.format(str(solutions(b, a, c))) + z.format(str(solutions(e, d, f))) + z.format(
                str(solutions(h, g, i))) + z.format(str(solutions(k, j, l))) + z.format(str(solutions(n, m, o)))
            return first_row + second_row + third_row + forth_row

        elif display is False:
            first_row = z.format(str(a)) + z.format(str(d)) + z.format(str(g)) + z.format(str(j)) + z.format(str(m)) + "\n"
            second_row = z.format(str(b) + str(op_space(a, c)) + str(c)) + z.format(
                str(e) + str(op_space(d, f)) + str(f)) + z.format(str(h) + str(op_space(g, i)) + str(i)) + z.format(
                str(k) + str(op_space(j, l)) + str(l)) + z.format(
                str(n) + str(op_space(m, o)) + str(o)) + "\n"
            third_row = z.format(str(num_dashes(a, c))) + z.format(str(num_dashes(d, f))) + z.format(
                str(num_dashes(g, i))) + z.format(str(num_dashes(j, l))) + z.format(str(num_dashes(m, o))) + "\n"
            return first_row + second_row + third_row

    # If 4 Problems:
    elif count == 3:
        a, b, c, d, e, f = workable[0], workable[1], workable[2], workable[3], workable[4], workable[5]
        g, h, i, j, k, l = workable[6], workable[7], workable[8], workable[9], workable[10], workable[11]

        # 4 Problems Digit Limit Check
        if int(a) > 9999 or int(c) > 9999 or int(d) > 9999 or int(f) > 9999:
            return 'Error: Numbers cannot be more than four digits.'

        elif int(g) > 9999 or int(i) > 9999 or int(j) > 9999 or int(l) > 9999:
            return 'Error: Numbers cannot be more than four digits.'

        elif display is True:
            first_row = z.format(str(a)) + z.format(str(d)) + z.format(str(g)) + z.format(str(j)) + "\n"
            second_row = z.format(str(b) + str(op_space(a, c)) + str(c)) + z.format(
                str(e) + str(op_space(d, f)) + str(f)) + z.format(str(h) + str(op_space(g, i)) + str(i)) + z.format(
                str(k) + str(op_space(j, l)) + str(l)) + "\n"
            third_row = z.format(str(num_dashes(a, c))) + z.format(str(num_dashes(d, f))) + z.format(
                str(num_dashes(g, i))) + z.format(str(num_dashes(j, l))) + "\n"
            forth_row = z.format(str(solutions(b, a, c))) + z.format(str(solutions(e, d, f))) + z.format(
                str(solutions(h, g, i))) + z.format(str(solutions(k, j, l)))
            return first_row + second_row + third_row + forth_row

        elif display is False:
            first_row = z.format(str(a)) + z.format(str(d)) + z.format(str(g)) + z.format(str(j)) + "\n"
            second_row = z.format(str(b) + str(op_space(a, c)) + str(c)) + z.format(
                str(e) + str(op_space(d, f)) + str(f)) + z.format(str(h) + str(op_space(g, i)) + str(i)) + z.format(
                str(k) + str(op_space(j, l)) + str(l)) + "\n"
            third_row = z.format(str(num_dashes(a, c))) + z.format(str(num_dashes(d, f))) + z.format(
                str(num_dashes(g, i))) + z.format(str(num_dashes(j, l))) + "\n"
            return first_row + second_row + third_row

    # If 3 Problems:
    elif count == 2:
        a, b, c, d, e, f = workable[0], workable[1], workable[2], workable[3], workable[4], workable[5]
        g, h, i = workable[6], workable[7], workable[8]

        # 3 Problems Digit Limit Check
        if int(a) > 9999 or int(c) > 9999 or int(d) > 9999 or int(f) > 9999 or int(g) > 9999 or int(i) > 9999:
            return 'Error: Numbers cannot be more than four digits.'

        elif display is True:
            first_row = z.format(str(a)) + z.format(str(d)) + z.format(str(g)) + "\n"
            second_row = z.format(str(b) + str(op_space(a, c)) + str(c)) + z.format(
                str(e) + str(op_space(d, f)) + str(f)) + z.format(str(h) + str(op_space(g, i)) + str(i)) + "\n"
            third_row = z.format(str(num_dashes(a, c))) + z.format(str(num_dashes(d, f))) + z.format(
                str(num_dashes(g, i))) + "\n"
            forth_row = z.format(str(solutions(b, a, c))) + z.format(str(solutions(e, d, f))) + z.format(
                str(solutions(h, g, i)))
            return first_row + second_row + third_row + forth_row

        elif display is False:
            first_row = z.format(str(a)) + z.format(str(d)) + z.format(str(g)) + "\n"
            second_row = z.format(str(b) + str(op_space(a, c)) + str(c)) + z.format(
                str(e) + str(op_space(d, f)) + str(f)) + z.format(str(h) + str(op_space(g, i)) + str(i)) + "\n"
            third_row = z.format(str(num_dashes(a, c))) + z.format(str(num_dashes(d, f))) + z.format(
                str(num_dashes(g, i)))
            return first_row + second_row + third_row

    # If 2 Problems:
    elif count == 1:
        a, b, c, d, e, f = workable[0], workable[1], workable[2], workable[3], workable[4], workable[5]

        if int(a) > 9999 or int(c) > 9999 or int(d) > 9999 or int(f) > 9999:
            return 'Error: Numbers cannot be more than four digits.'

        elif display is True:
            first_row = z.format(str(a)) + z.format(str(d)) + "\n"
            second_row = z.format(str(b) + str(op_space(a, c)) + str(c)) + z.format(
                str(e) + str(op_space(d, f)) + str(f)) + "\n"
            third_row = z.format(str(num_dashes(a, c))) + z.format(str(num_dashes(d, f))) + "\n"
            forth_row = z.format(str(solutions(b, a, c))) + z.format(str(solutions(e, d, f)))
            return first_row + second_row + third_row + forth_row

        elif display is False:
            first_row = z.format(str(a)) + z.format(str(d)) + "\n"
            second_row = z.format(str(b) + str(op_space(a, c)) + str(c)) + z.format(
                str(e) + str(op_space(d, f)) + str(f)) + "\n"
            third_row = z.format(str(num_dashes(a, c))) + z.format(str(num_dashes(d, f)))
            return first_row + second_row + third_row

    elif count == 0:
        a, b, c = workable[0], workable[1], workable[2]

        if int(a) > 9999 or int(c) > 9999:
            return 'Error: Numbers cannot be more than four digits.'

        elif display is True:
            first_row = z.format(str(a)) + "\n"
            second_row = z.format(str(b) + str(op_space(a, c)) + str(c)) + "\n"
            third_row = z.format(str(num_dashes(a, c))) + "\n"
            forth_row = z.format(str(solutions(b, a, c)))
            return first_row + second_row + third_row + forth_row

        elif display is False:
            first_row = z.format(str(a)) + "\n"
            second_row = z.format(str(b) + str(op_space(a, c)) + str(c)) + "\n"
            third_row = z.format(str(num_dashes(a, c))) + "\n"
            return first_row + second_row + third_row


print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']))
