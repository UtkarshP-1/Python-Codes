# 1. Use inheritance
# Write a class Course with name,fees.
# Provide following functionalities
# A. initializer
# B. Accept data
# C. Print Data .
# Write a Class Computer with subjectList.
# Provide following functionalities
# A. initializer
# B. Accept data
# C. Print Data .
# Write a Class Electonics with subjectList.
# Provide following functionalities
# A. initializer
# B. Accept data
# C. Print Data .
# Write menu driven program to test above functionalities.
# OutPut
# ‘1st year Comp’ 90000 [‘sub1’,’sub2’....]

class Course:
    
    def __init__(self,name=None,fees=None):
        self.name = name
        self.fees = fees
        
    def accept_data(self, name, fees):
        self.name = name
        self.fees = fees
    
    def print_data(self):
        print(f"Course Name: {self.name}, Fees: {self.fees}", end='\t')
        

class Computer(Course):
    def __init__(self, name=None, fees=None, subjectList=None):
        super().__init__(name,fees)
        self.subjectList = subjectList
        
    def accept_data(self,name,fees, subjectList):
        super().accept_data(name, fees)
        self.subjectList = subjectList 
        
    def print_data(self):
        super().print_data()
        print(f"Subject List: {self.subjectList}")
        

class Electronics(Course):
    def __init__(self,name=None,fees=None, subjectList=None):
        super().__init__(name,fees)
        self.subjectList = subjectList
        
    def accept_data(self,name,fees, subjectList):
        super().accept_data()
        subjectList = self.subjectList
        
    def print_data(self):
        super().print_data()
        print(f"Subject List: {self.subjectList}")
        
        
computer_sub_list = ["C Programming", "OOP", "Java", "Python", "R"]
electronics_sub_list = ["Digital Systems", "Control Systems", "Power Electronics", "IC Technology", "VLSI Design"]

intake = int(input("Choose your Course: \n 1. Computer \n 2. Electronics \n 3. Custom Course \n Enter your input: "))

match intake:
    case 1:
        c1 = Computer()
        c1.accept_data('1st year Comp', 90000, computer_sub_list)
        c1.print_data()  
    case 2:
        c2 = Electronics('EXTC',75000, electronics_sub_list)
        c2.print_data()
    case 3:
        c3 = Course(input("Enter Course Name : "), input("Enter Course Fees : "))
        c3.print_data()
    case _:
        print("Invalid Input")
