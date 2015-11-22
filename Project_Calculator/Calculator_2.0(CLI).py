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
    if value in sign: # If the input value isn't number,
        _sign = value
        print("Entered :", num_log, _sign)
        value_2 = input("Enter : ") # input again for 'Arithmetic' function.
        if value_2 not in sign: # And checking...
            num_2 = int(value_2) # Changing...
            new_num = Arithmetic(num_1, _sign, num_2) # Running...
            print("Entered :", new_num) # Printing!
            num_1 = new_num
            num_log = new_num
        else:
            _sign = value_2 # If the third input value isn't number,
            value_2 = input("Enter : ") # initializing sign value and input again.
            num_2 = int(value_2) # Changing...
            new_num = Arithmetic(num_1, _sign, num_2) # Running...
            print("Entered :", new_num) # Printing!
            num_1 = new_num
            num_log = new_num

    else: # If the first input value is number, it is performed.
        print("Entered :", value)
        num_log = value
        num_1 = int(value)

