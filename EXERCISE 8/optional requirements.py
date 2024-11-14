
"""### Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input."""

#store the names in the list
NAMES =["Jake", "Zac" , "Ian", "Ron", "Sam", "Dave"]

#write the code u want to search the name for 
SEARCHFOR =input("ENTER THE NAME YOU WANT TO SEARCH : ")

#the code will display if the name is found or not found
if SEARCHFOR in NAMES:
    print("NAME FOUND:", SEARCHFOR)
else:
    print("NAME NOT FOUND:", SEARCHFOR)
