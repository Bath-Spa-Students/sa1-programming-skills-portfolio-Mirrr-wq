
"""### Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year
and adjust the number of days accordingly."""

# store the data of days and months 
days = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
}
# code will ask the user to input the number of the month
days = (int(input("enter the months number (1-5): ")))
# if the user asks for 2nd month itll ask the user if its a leap year or not
if days == 2 :
    leap = input (" is this leap year ? (yes/no) : ")
#if its a leap year it will display 29 days or else it will say 28 days
    if leap == "yes":
       print("there are 29 days in leap year")
    elif leap ==  "no":   
       print("there are 28 days")
    else:
        print("invalid input")