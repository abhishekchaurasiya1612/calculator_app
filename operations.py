import math

def add_num(num1,num2):
    return num1+num2
def sub_num(num1,num2):
    return num1-num2
def div_num(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return "Can't divide by zero"
def mul_num(num1,num2):
    return num1*num2
def square_num(num1):
    return num1**2
def sqrt_num(num1):
    return math.sqrt(num1)
def power_num(num1,num2):
    return math.pow(num1,num2)
def factorial_num(num1):
    return math.factorial(int(num1))