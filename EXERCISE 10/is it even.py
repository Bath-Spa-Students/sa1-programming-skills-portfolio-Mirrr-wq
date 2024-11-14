

"""### Instructions:
* The program should ask the user for a number from within the main function.
* The entered number should be passed to a function that determines if the value is even or odd.
* The function should return a message indicating whether the number is even or odd.
* The message returned by the function should be printed from within the main function."""


# Ask the user for a number
value = int(input("Please enter a number: "))

# Check if the number is even or odd and print the result
if value % 2 == 0:
    print(f"The number {value} is even.")
else:
    print(f"The number {value} is odd.")