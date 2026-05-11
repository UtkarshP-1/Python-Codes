# Write functions to perform addition, subtraction, multiplication, division on two numbers in Python , return the result and print result.

def addition(num1: int, num2: int) -> int:
    return print(f"addition result = {num1 + num2}")
    
def subtraction(num1: int, num2: int) -> int:
    return print(f"subtraction result = {num1 - num2}")

def multiplication(num1: int, num2: int) -> int:
    return print(f"multiplication result = {num1 * num2}")
    
def division(num1: int, num2: int) -> float:
    if num2 == 0:
        print("Denominator cannot be 0")
    else:
        return print(f"division result = {num1 / num2}")

def division2(num1: int, num2: int) -> float | str:
    try:
        return print(f"division result = {num1 / num2}")
    except:
        return print("Invalid Denominator")

num1, num2 = int(input("Enter num 1 : ")), int(input("Enter num2 : "))

addition(num1,num2)
subtraction(num1,num2)
multiplication(num1,num2)
division(num1,num2)
division2(num1,num2)
