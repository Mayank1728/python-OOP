from random import choice
print("Welcome To Employee Wage Computation")

class Employee:
 """
 Calculates the wage of an employee
 """
 wph = 20 # wage per hour
 ft_hours = 8 # full time hours
 pt_hours = 4 # part time hours
 twd = 20 # total working days

 def __init__(self):
  self.worked_hours = 0
  self.days_worked = 0
  self.total_wage = 0

 def is_present(self)->str:
  return choice(['Present', 'Absent'])
 
 def daily_wage(self)->int:
  # wage = 0
  if self.is_present() == 'Absent':
   self.total_wage += 0
   return
  self.is_part_time = choice([True, False])
  if self.is_part_time:
   self.total_wage += Employee.pt_hours * Employee.wph
   self.worked_hours += Employee.pt_hours
  else: 
   self.total_wage += Employee.ft_hours * Employee.wph
   self.worked_hours += Employee.ft_hours
  self.days_worked += 1
  # self.total_wage += wage
  # return wage
 
 # def monthly_wage(self)->int:
 #  monthly_wage = self.daily_wage() * Employee.twd
 #  return monthly_wage 
 
 def cal_wages_till(self)->int:
  while self.worked_hours < 130 and self.days_worked < 20:
   self.daily_wage()
  # return self.total_wage

goku = Employee()
print("Is Employee present today: ", goku.cal_wages_till())
# print("Daily wage: ", goku.daily_wage())
# print("Monthly wage: ", goku.monthly_wage())
print("Total wages till: ", goku.total_wage)
