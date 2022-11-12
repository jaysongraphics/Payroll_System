from tabulate import tabulate
from emoji import emojize

# Subtracted Taxes #
# Fed_Tax =  10%
# State_Tax =  6%  
# FICA(Federal Insurance Contributions Act) =  3% 

print(emojize(':smiling_face_with_sunglasses: Welcome to the payroll system! :smiling_face_with_sunglasses:'))

Employee_Info = []
employee_number = 1

def User_Input(message):
  while True:
    try:
       userInput = float(input(message))       
    except ValueError:
       print(emojize(':stop_sign: Not an integer! Try again. :stop_sign:'))
       continue
    else:
       return userInput      
          
def User_Input_string(message):
  while True:
    userInput = input(message)
    if(len(userInput) < 3):
      print(emojize(':stop_sign: Name must be three characters long! Try again. :stop_sign:'))
      continue
    else:
      return userInput 

while len(Employee_Info) < 11: 
  Employee_Name = User_Input_string(emojize(f':radio_button: Please enter your name employee #{employee_number}: '))
  Pay_Rate = User_Input(emojize(f':radio_button: Please enter your pay rate/hr employee #{employee_number}: '))
  Hours_Worked = User_Input(emojize(f':radio_button: Please enter how many hours you worked employee this week #{employee_number}: '))
  Overtime = Pay_Rate * 1.5 
  
  if (Hours_Worked > 40):
    Regular_Pay = Hours_Worked * Pay_Rate
    OT_Pay = Regular_Pay + Overtime 
    Gross_Pay = Regular_Pay + OT_Pay
  elif(Hours_Worked <= 0 or Hours_Worked >= 100):
    print('Please enter a number between 1 and 100')
    break
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
print(emojize(':money_bag: Please see below this week payroll! :money_bag:'))
print(tabulate(Employee_Info, headers=headers_table, tablefmt='fancy_grid'))