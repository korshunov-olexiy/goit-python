from basic_classes import *

def standard_input():
    yield "Vasya"
    yield "22.02.1995"
    yield "222-222-22-22;333-222-11-00"
    yield "address #1"
    yield "em1@gmail.com"
    yield "note #1"


input_rec = InterfaceCMD()

try:
    rec = Record(input_rec)
except SpecifyAttrError as attr_error:
    print(attr_error)

print("================================")
print(rec)
