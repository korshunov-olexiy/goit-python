def sanitize_phone_number(phone):
    repl_chr = "(-)+ "
    return ''.join(filter(lambda s: s not in repl_chr, phone))

print( sanitize_phone_number("    +38 (095) 3245678   ") )
