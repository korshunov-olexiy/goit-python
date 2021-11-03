def makeupper(fn):
    def wrapper(val):
        return "<u>" + fn(val.upper()) + "</u>"
    return wrapper

def makebold(fn):
    def wrapped(val):
        return "<b>" + fn(val) + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped(val):
        return "<i>" + fn(val) + "</i>"
    return wrapped

@makeupper
@makebold
@makeitalic
def hello(val):
    return val

print(hello("hello world"))
