# 1. Write a Class Painting with method calculatePaintingCost.
# Write a Class FlatPainting with noOfRooms which is inheritated from Class Painting.
# Override calculatePaintingCost.(Assume per room painting cost is 10000)
# Write a Class BulidingPainting with noOfFlats which is inheritated from Class Painting.
# Override calculatePaintingCost.(Assume per Flats painting cost is 25000)
# Write method for 1.Flat 2.Building and then calculate the cost according to the type.

class Painting:
    
    painting_cost = 7500
    
    def __init__(self, noOfRooms=0):
        self.noOfRooms = noOfRooms
        
    def calculatePaintingCost(self):
        print(f"Painting cost will be {self.painting_cost*self.noOfRooms} Rs.")
    
class FlatPainting(Painting):
    painting_cost = 10000
    

    
class BulidingPainting(Painting):
    painting_cost = 25000
  
        
intake = int(input("Calculate Painting Cost for : \n 1. Flat \n 2. Building \n Enter your choice : "))

match intake:
    case 1:
        f1 = FlatPainting(int(input("Enter number of rooms : ")))
        f1.calculatePaintingCost()
    case 2:
        b1 = BulidingPainting(int(input("Enter number of flats : ")))
        b1.calculatePaintingCost()
    case _:
        print("Invalid Input")
