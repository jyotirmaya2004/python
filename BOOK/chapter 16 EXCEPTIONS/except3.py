def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

try:
    print(divide(10, 0))
except ValueError as e:
    print(e) 