def is_valid_password(password):
    return len(password) >= 8 and \
        any(l.isdigit() for l in password) and \
        any(l.islower() for l in password) and \
        any(l.isupper() for l in password)

# EXAMPLE:
pwd = "aX1brdwza"
print(is_valid_password(pwd))
