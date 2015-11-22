def Arithmetic(num1, sign, num2):
    if sign == '+':
        return num1 + num2
    elif sign == '-':
        return num1 - num2
    elif sign == '*':
        return num1 * num2
    elif sign == '/':
        return num1 / num2

while True:
    value = input("Enter : ")

    sign = ('+', '-', '*', '/')
    if value in sign:
        # If the input value isn't number,
        # input again for 'Arithmetic' function.
        _sign = value
        print("Entered :", num_log, _sign)
        value_2 = input("Enter : ")
        if value_2 not in sign:
            num_2 = int(value_2)
            new_num = Arithmetic(num_1, _sign, num_2)
            print("Entered :", new_num)
            num_1 = new_num
            num_log = new_num
        else:
            # If the third input value isn't number,
            # initializing sign value and input again.
            _sign = value_2
            print("Entered :", num_log, _sign)
            value_2 = input("Enter : ")
            num_2 = int(value_2)
            new_num = Arithmetic(num_1, _sign, num_2)
            print("Entered :", new_num)
            num_1 = new_num
            num_log = new_num

    else:
        # If the first input value is number,
        # it is performed.
        print("Entered :", value)
        num_log = value
        num_1 = int(value)