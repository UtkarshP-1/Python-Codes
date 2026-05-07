# Write a Matrix class. Write Accept () and Print () functions. 
# Also provide Addition (), Subtraction () and Multiplication () function.

class Matrix():
  
  def accept(self,num1, num2):
    self.num1 = num1
    self.num2 = num2
    
  def print(self):
    print(f'Num1 = {self.num1} Num2 = {self.num2}')
    
  def addition(self):
    print(f'addition = {self.num1+self.num2}')
    
  def subtraction(self):
    print(f'subtraction = {self.num1-self.num2}')
  
  def multiplication(self):
    print(f'multiplication = {self.num1*self.num2}')
  
  def division(self):
    print(f'division = {self.num1/self.num2}')
    
    

mat = Matrix()
mat.accept(10,20)
mat.print()
mat.addition()
mat.subtraction()
mat.multiplication()
mat.division()
