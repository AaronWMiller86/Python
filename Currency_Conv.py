cur_dict = {
    "u2s": 1192.76,
    "u2j": 114.95,
    "u2c": 6.33,
    "u2n": 8.89,
    "s2u": 0.00084,
    "s2j": 0.096,
    "s2c": 0.0053,
    "s2n": 0.0075,
    "j2u": 0.0087,
    "j2s": 10.38,
    "j2c": 0.055,
    "j2n": 0.077,
    "c2u": 0.16,
    "c2s": 188.71,
    "c2j": 18.17,
    "c2n": 1.41,
    "n2u": 0.11,
    "n2s": 134.11,
    "n2j": 12.92,
    "n2c": 0.71,
}

menu_dict = {
    "\n"
    "1": "US Dollar",
    "2": "South Korean Won",
    "3": "Japanese Yen",
    "4": "Chinese Yuan",
    "5": "Norwegian Krone",
}

input_dict = {
    "USD": "Enter $ amount in USD: ",
    "KRW": "Enter ₩ amount in KRW: ",
    "JPY": "Enter ¥ amount in JPY: ",
    "CNY": "Enter ¥ amount in CNY: ",
    "NOK": "Enter kr amount in NOK: ",
}
# Display Menu Options from menu_dict.
for key in menu_dict:
    print(key, ':', menu_dict[key])


def menu(sel1, sel2):

    # USD Conversion Menu (Selection 1)
    if sel1 == "1" and sel2 == "2":
        return dollar_won(input(input_dict["USD"]))
    elif sel1 == "1" and sel2 == "3":
        return dollar_yen(input(input_dict["USD"]))
    elif sel1 == "1" and sel2 == "4":
        return dollar_yuan(input(input_dict["USD"]))
    elif sel1 == "1" and sel2 == "5":
        return dollar_krone(input(input_dict["USD"]))

    # KRW Conversion Menu (Selection 2)
    elif sel1 == "2" and sel2 == "1":
        return won_dollar(input(input_dict["KRW"]))
    elif sel1 == "2" and sel2 == "3":
        return won_yen(input(input_dict["KRW"]))
    elif sel1 == "2" and sel2 == "4":
        return won_yuan(input(input_dict["KRW"]))
    elif sel1 == "2" and sel2 == "5":
        return won_krone(input(input_dict["KRW"]))

    # JPY Conversion Menu (Selection 3)
    elif sel1 == "3" and sel2 == "1":
        return yen_dollar(input(input_dict["JPY"]))
    elif sel1 == "3" and sel2 == "2":
        return yen_won(input(input_dict["JPY"]))
    elif sel1 == "3" and sel2 == "4":
        return yen_yuan(input(input_dict["JPY"]))
    elif sel1 == "3" and sel2 == "5":
        return yen_krone(input(input_dict["JPY"]))

    # CNY Conversion Menu (Selection 4)
    elif sel1 == "4" and sel2 == "1":
        return yuan_dollar(input(input_dict["CNY"]))
    elif sel1 == "4" and sel2 == "2":
        return yuan_won(input(input_dict["CNY"]))
    elif sel1 == "4" and sel2 == "3":
        return yuan_yen(input(input_dict["CNY"]))
    elif sel1 == "4" and sel2 == "5":
        return yuan_krone(input(input_dict["CNY"]))

    # NOK Conversion Menu (Selection 5)
    elif sel1 == "5" and sel2 == "1":
        return krone_dollar(input(input_dict["NOK"]))
    elif sel1 == "5" and sel2 == "2":
        return krone_won(input(input_dict["NOK"]))
    elif sel1 == "5" and sel2 == "3":
        return krone_yen(input(input_dict["NOK"]))
    elif sel1 == "5" and sel2 == "4":
        return krone_yuan(input(input_dict["NOK"]))

    # Invalid Selection / Return
    else:
        print("Invalid Selection")
        return menu(int(input("\nStarting Currency? (1-5): ")), int(input("Resulting Currency? (1-5)): ")))


def dollar_won(cur):
    return print("₩ " + str(round(float(cur), 2) * (cur_dict["u2s"])))


def dollar_yen(cur):
    return print("¥ " + str(round(float(cur), 2) * (cur_dict["u2j"])))


def dollar_yuan(cur):
    return print("¥ " + str(round(float(cur), 2) * (cur_dict["u2c"])))


def dollar_krone(cur):
    return print("kr " + str(round(float(cur), 2) * (cur_dict["u2n"])))


def won_dollar(cur):
    return print("$ " + str(round(float(cur), 2) * (cur_dict["s2u"])))


def won_yen(cur):
    return print("¥ " + str(round(float(cur), 2) * (cur_dict["s2j"])))


def won_yuan(cur):
    return print("¥ " + str(round(float(cur), 2) * (cur_dict["s2c"])))


def won_krone(cur):
    return print("kr " + str(round(float(cur), 2) * (cur_dict["s2n"])))


def yen_dollar(cur):
    return print("$ " + str(round(float(cur), 2) * (cur_dict["j2u"])))


def yen_won(cur):
    return print("₩ " + str(round(float(cur), 2) * (cur_dict["j2s"])))


def yen_yuan(cur):
    return print("¥ " + str(round(float(cur), 2) * (cur_dict["j2c"])))


def yen_krone(cur):
    return print("kr " + str(round(float(cur), 2) * (cur_dict["j2n"])))


def yuan_dollar(cur):
    return print("$ " + str(round(float(cur), 2) * (cur_dict["c2u"])))


def yuan_won(cur):
    return print("₩ " + str(round(float(cur), 2) * (cur_dict["c2s"])))


def yuan_yen(cur):
    return print("¥ " + str(round(float(cur), 2) * (cur_dict["c2j"])))


def yuan_krone(cur):
    return print("kr " + str(round(float(cur), 2) * (cur_dict["c2n"])))


def krone_dollar(cur):
    return print("$ " + str(round(float(cur), 2) * (cur_dict["n2u"])))


def krone_won(cur):
    return print("₩ " + str(round(float(cur), 2) * (cur_dict["n2s"])))


def krone_yen(cur):
    return print("¥ " + str(round(float(cur), 2) * (cur_dict["n2c"])))


def krone_yuan(cur):
    return print("¥ " + str(round(float(cur), 2) * (cur_dict["n2n"])))


menu(input("\nStarting Currency? (1-5): "), input("Resulting Currency? (1-5)): "))
