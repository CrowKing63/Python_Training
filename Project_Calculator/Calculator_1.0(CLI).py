while True:
    num1 = input("Enter number.\n")
    sign = input("Enter sign.\n")
    num2 = input("Enter number.\n")
    print(num1, sign, num2, '= ', end='')
    if sign == '+':
        print(int(num1) + int(num2))
    elif sign == '-':
        print(int(num1) - int(num2))
    elif sign == '*':
        print(int(num1) * int(num2))
    elif sign == '/':
        print(int(num1) / int(num2))