import math

def add (a, b):
    return a+b

def sub (a, b):
    return a-b

def mult (a, b):
    return a*b

def div (a, b):
    if b == 0:
        return "no zero"
    return a/b

def log (a, base=10):
    return math.log10(a)

def sqr (a):
    return a ** 2

def cos (a):
    return math.cos(a)

def sin (a):
    return math.sin(a)

def sqr_root (a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "no negatives"

def per (a, b):
    if ((a / abs(a) == -1) or (b == 0)):
        return "no negatives"
    else:
        return (a / b) * 100