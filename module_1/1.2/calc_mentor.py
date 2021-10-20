operator = None
operand = None
wait_for_number = True
result = None
while operator != '=':
    if wait_for_number:
        raw_operand = input('Type a number ')
        try:
            operand = float(raw_operand)
            wait_for_number = False
        except ValueError:
            print(f'{raw_operand} is not a number')
            continue
        if result is None:
            result = operand
        else:
            if operator == '+':
                result += operand
            elif operator == '-':
                result -= operand
            elif operator == '*':
                result *= operand
            elif operator == '/':
                try:
                    result /= operand
                except ZeroDivisionError:
                    print('Cannot devide by zero')
                    wait_for_number = True
    else:
        operator = input('Operation? +, -, *, / ')
        if operator in ('+', '-', '*', '/', '='):
            wait_for_number = True
        else:
            print(f"{operator} is not '+' or '-' or '/' or '*'. Try again")
print(result)
