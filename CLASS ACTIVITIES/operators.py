names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Allow the user to input the search term
search_name = input("Enter the name you want to search for: ")

# Check if the name is in the list
if search_name in names:
    print("Found:", search_name)
else:
    print("Not found:", search_name)