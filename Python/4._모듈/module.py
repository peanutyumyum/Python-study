def add(num1, num2):
    result = num1 + num2
    return result

def sub(num1, num2):
    if num1 >= num2:
        result = num1 - num2
    else:
        result = num2 - num1
    return result

print(add(3, 4))