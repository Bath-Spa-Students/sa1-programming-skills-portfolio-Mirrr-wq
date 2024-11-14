
"""### Optional Requirements:

Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining
 attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted."""

#make a pass and store it 
right_pass = "2233"

full_attempts = 5

tries = 0
#this code will display if the user enetered the right code or wrong, and will let the user know about the tries as well
while tries < full_attempts:
    answer = input("ENTER THE PASS : ")
      
      
    if answer == right_pass :
        print ("ACCESS GRANTED, HAVE FUN")
    else:
        tries += 1
        print (f"INCOREECT PASSWORD, ATTEMPTS {full_attempts - tries}")

#if the user exceeds the maximum limit of the  trie this message will be displayed
if tries == full_attempts:
    print ("MAXIMUM ATTEMPTS REACHED")


