
"""## Exercise 8: Simple Search - 30 Marks

Write a program that searches for a specific string within a list of strings. The list is initialized with specific 
names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".

### Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input."""

# make a list and store the names or values u wangt
LIST = ["Jake", "Zac" , "Ian", "Ron", "Sam", "Dave"]

#write the name u want to search for
PERSON = "Sam"

#the code will display if the name u typed is present in the list or not
if PERSON in LIST :
    print("FOUND" , PERSON)
else :
    print("NOT FOUND", PERSON )