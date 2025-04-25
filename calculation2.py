# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "0 ga bo‘lish mumkin emas!"
    return x / y

print("Oddiy kalkulyator")
a = float(input("1-sonni kiriting: "))
b = float(input("2-sonni kiriting: "))

print("Yig‘indi:", add(a, b))
print("Ayirma:", subtract(a, b))
print("Ko‘paytma:", multiply(a, b))
print("Bo‘linma:", divide(a, b))