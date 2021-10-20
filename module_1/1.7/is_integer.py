def is_integer(s):
    s = s.strip().replace('-', '').replace('+', '')
    if len(s) == 0 or not s.isdigit():
        return False
    elif len(s) >= 1 and s.isdigit():
        return True


digit = "  -12  "
print(digit.strip().isdigit())
print(is_integer(digit))
