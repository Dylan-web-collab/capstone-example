import math

def add (a, b):
    return a+b

def sub (a, b):
    return a-b

def mult (a, b):
    return a*b

def div (a, b):
    if b == 0:
        return "no negative"
    return a/b

def log (a):
    if a == 0:
        return "no negative"
    return math.log(a)

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
    if a >= 0 & b >= 0:
        return (a/b) * 100
    else:
        return "no negatives"