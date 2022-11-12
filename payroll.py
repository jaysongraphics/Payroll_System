from tabulate import tabulate

# Subtracted Taxes #
# Fed_Tax =  10%
# State_Tax =  6%  
# FICA(Federal Insurance Contributions Act) =  3% 

print('Welcome to the payroll system!')
Employee_Info = []
employee_number = 1

while len(Employee_Info) < 11: 
  
  Employee_Name = input(f'Please enter your name employee #{employee_number}: ');
  Pay_Rate = float(input(f'Please enter your pay rate/hr employee #{employee_number}: '));
  Hours_Worked = float(input(f'Please enter how many hours you worked employee this week #{employee_number}: '));
  Overtime = Pay_Rate * 1.5 
  
  if (Hours_Worked > 40):
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
print('Please see below this week payload!')
print(tabulate(Employee_Info, headers=headers_table, tablefmt='fancy_grid'))

