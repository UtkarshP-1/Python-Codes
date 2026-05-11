# Write a class Date with day,month,year.
# Provide following functionalities
# A. initializer
# B. Accept date(19/02/2018)
# C. validate date (If not then throw exception InvalidDate ).
# D. Print Date in format of '19 Feb 2018'.


class Date:
  def __init__(self,date=1, month=1, year=1990):
    self.date = date
    self.month = month
    self.year = year
    
  
  def accept_date(self,date, month, year):
    self.date = date
    self.month = month
    self.year = year
    
  def validate_date(self):
    try:
      date = int(self.date)
      month = int(self.month)
      year = int(self.year)
    except ValueError as e:
      print(f"Invalid Date \t {e}")
    else:
      print('Date is Valid')
    finally:
      print('Date validated')
  
  def print_date(self):
    month_dict = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec"
    }
    print(f'{self.date} {month_dict.get(int(self.month))} {self.year}') 
    

dt = Date()
dt.accept_date(*'19/two/2018'.split('/'))
dt.validate_date()
dt.print_date()
