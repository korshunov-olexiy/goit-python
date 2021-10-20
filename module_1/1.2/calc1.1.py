# # === Example #1
# def standard_input():
#     yield "10"
#     yield "+"
#     yield "5"
#     yield "6"
#     yield "/"
#     yield "3"
#     yield "-"
#     yield "a"
#     yield "2"
#     yield "*"
#     yield "6"
#     yield "="

# === Example #2

def standard_input():
    yield "2"
    yield "3"
    yield "-"
    yield "1"
    yield "+"
    yield "10"
    yield "*"
    yield "/"
    yield "2"
    yield "="


result = None
operand = None
operator = None
wait_for_number = True

while True:
    inp = input("")
    if wait_for_number:
        try:
            if operator is None:
                result = float(inp)
                wait_for_number = not wait_for_number
            else:
                operand = float(inp)
                if operator == "+":
                    result += operand
                elif operator == "-":
                    result -= operand
                elif operator == "/":
                    result /= operand
                elif operator == "*":
                    result *= operand
                wait_for_number = not wait_for_number
        except:
            print(f"{inp} is not a number. Try again.")
    elif not inp.isdigit() and inp != "=":
        if inp in ['+', '-', '/', '*']:
            operator = inp
            wait_for_number = not wait_for_number
        else:
            print(f"{inp} is not '+' or '-' or '/' or '*'. Try again")
    else:
        if inp == "=":
            break
        else:
            print(f"{inp} is not '+' or '-' or '/' or '*'. Try again")
# выводим результат:
print(f"result: {result}")
