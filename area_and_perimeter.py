# Write two functions to find an area of a rectangle and perimeter of the rectangle.

def area(length: int, width: int) -> int | str:
    try:
        return length*width
    except:
        return "Invalid Input"
    
def perimeter(length: int, width: int) -> int | str:
    try:
        return 2*(length+width)
    except:
        return "Invalid Input"
    
try:
    length, width = int(input("Enter length : ")), int(input("Enter width : "))
    area = area(length, width)
    perimeter = perimeter(length, width)
    print("Area = ",area)
    print("Perimeter = ",perimeter)
except TypeError:
    print("Enter Numeric Value")
except ValueError:
    print("Invalid Value")
except:
    print("Error")

