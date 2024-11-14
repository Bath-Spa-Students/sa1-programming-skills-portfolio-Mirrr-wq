
'''Write a program that tells a user how many days there are in a specific month. Use a dictionary to map 
the month numbers (1-12) to the number of days in each month.

### Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.

### Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year
and adjust the number of days accordingly.'''

#code is asking the user to input the number of the month to display the days
num_month = (int(input("write the month number (1-12): ") ))
# this code is basically used to store the days of the perticular months
if num_month == 1 :
    days = 31
elif num_month == 2 :
    days = 28
elif num_month == 3 :
    days = 31
elif num_month == 4 :
    days = 30
elif num_month == 5 :
    days = 31
elif num_month == 6 :
    days = 30
elif num_month == 7 :
    days = 31
elif num_month == 8 :
    days = 31
elif num_month == 9 :
    days = 30
elif num_month == 10 :
    days = 31
elif num_month == 11 :
    days = 30
elif num_month == 12 :
    days = 31
else :
    days = None

#this code will print the the days of the month the user is asking for
if days is not None :
    print(f" there are {days} days in {num_month} .")
else :
    print("Pls enter valid month number")



