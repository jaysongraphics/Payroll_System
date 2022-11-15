from tabulate import tabulate
from emoji import emojize

# Subtracted Taxes #
# Fed_Tax =  10%
# State_Tax =  6%  
# FICA(Federal Insurance Contributions Act) =  3% 

print(emojize('          :smiling_face_with_sunglasses: Welcome to the payroll system! :smiling_face_with_sunglasses:'))
print(emojize('''
              ,---------------------------,
              |  /---------------------\  |
              | |                       | |
              | |     Edward            | |
              | |           Arias       | |
              | |                       | |
              | |                       | |
              |  \_____________________/  |
              |___________________________|
            ,---\_____     []     _______/------,
          /         /______________\           /|
        /___________________________________ /  | ___
        |                                   |   |    )
        |  _ _ _                 [-------]  |   |   (
        |  o o o                 [-------]  |  /    _)_
        |__________________________________ |/     /  /
    /-------------------------------------/|      ( )/
  /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''))

Employee_Info = []
employee_number = 1

def User_Input_String(message):
  while True:
    try:
        userInput = str(input(message))
        if userInput.isalpha() == False:
          print(emojize(':stop_sign: Please enter an alphabetical name! Try again. :stop_sign:'))
          continue
        elif (len(userInput) < 2):
           print(emojize(':stop_sign: Name must be at lease two characters long! Try again. :stop_sign:'))
           continue
    except TypeError:
        continue
    else:
       return userInput 

def User_Input_Hours(message):
  while True:
    try:
       userInput = float(input(message))  
       if (userInput <= 0 or userInput >= 65):
          print(emojize(':stop_sign: Please enter a number between 1 and 65. Try again. :stop_sign:')) 
          continue   
    except ValueError:
       print(emojize(':stop_sign: Not a number! Try again. :stop_sign:'))
       continue
    else:
       return userInput   
     
def User_Input_Rate(message):
  while True:
    try:
       userInput = float(input(message))  
       if (userInput <= 14 or userInput >= 51):
          print(emojize(':stop_sign: Minimum $15 or Max $50 wage was not met, try again. :stop_sign:')) 
          continue  
    except ValueError:
       print(emojize(':stop_sign: Not a number! Try again. :stop_sign:'))
       continue
    else:
       return userInput   

while len(Employee_Info) < 2: 
    Employee_Name = User_Input_String(emojize(f':radio_button: Please enter your name employee #{employee_number}: '))
    Pay_Rate = User_Input_Rate(emojize(f':radio_button: Please enter your pay rate/hr employee #{employee_number}: '))
    Hours_Worked = User_Input_Hours(emojize(f':radio_button: Please enter how many hours you worked this week employee #{employee_number}: '))
    Overtime = Pay_Rate * 1.5 
    
    if (Hours_Worked >= 40 and Hours_Worked <= 65):
      Regular_Pay = Hours_Worked * Pay_Rate
      OT_Pay = Regular_Pay + Overtime 
      Gross_Pay = Regular_Pay + OT_Pay   
    else:   
      Regular_Pay = Hours_Worked * Pay_Rate
      Gross_Pay = Regular_Pay 
      OT_Pay = 0
        
    Fed_Tax = round(0.1 * Gross_Pay, 2)
    State_Tax = round(0.06 * Gross_Pay, 2)
    FICA = round(0.03 * Gross_Pay, 2)
    Taxes = Fed_Tax + State_Tax + FICA
    Net_Pay = round(Gross_Pay - Taxes, 2)
                  
    Employee_list = Employee_Name, Hours_Worked, Pay_Rate, Regular_Pay, OT_Pay, Gross_Pay, Fed_Tax, State_Tax, FICA, Net_Pay
    Employee_Info.append(Employee_list)
        
    employee_number = employee_number + 1

headers_table = 'Employee Name', 'Hours Worked', '$ Pay_Rate', '$ Regular Pay', '$ OT Pay', '$ Gross Pay', '$ Fed Tax', '$ State Tax', '$ FICA', '$ Net Pay'    
print(emojize(':money_bag: Please see this week payroll below: :money_bag:'))
print(tabulate(Employee_Info, headers=headers_table, tablefmt='fancy_grid'))