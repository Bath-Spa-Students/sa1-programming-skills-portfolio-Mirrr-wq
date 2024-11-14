
"""### Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis"
should all be considered correct).Multiple Questions: Extend the program into a quiz that asks for 
the capitals of 10 European countries. Provide feedback for each question."""


# store the 10 countries and their capitals as per the question
country_caps = [
    ("France" , "paris"),
    ("Germany" , "berlin"),
    ("Italy" , "rome"),
    ("Spain" , "madrid"),
    ("Portugal" , "lisbon"),
    ("Nertherlands" , "amsterdam"),
    ("Belgium" , "brussels"),
    ("Sweden" , "stockholm"),
    ("Norway" , "oslo"),
    ("Finland" , "helsinki"),
]

# this code will ask you the capitals and if u anwer correct it will display the other question..
for country , capital in country_caps :
    answer = input (f"WHAT IS THE CAPITAL OF {country}? : ").strip()
    
    if answer.lower() == capital.lower():
        print ("GENIUS.")
    else:
        print(f"INCOREECT THE capital of {country} is {capital}")
