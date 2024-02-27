print("Program to find leap year")

year = 2300
total_digits = 0
year_copy = year
while year_copy: 
 total_digits += 1
 year_copy = year_copy // 10

if total_digits > 4:
 print("Invalid Input")
else:
 if (year % 4 == 0 and year % 100 == 0 and year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
  print(year, 'is a Leap year')
 else: 
  print(year, 'is NOT a leap year')
