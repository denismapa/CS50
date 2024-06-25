# 2024 CS50 Python
# Created by Denis Mapa

#Initial Python Script

# Steps
# 1. Get Input
# 2. Make everything lowercase


# January 4 2023

# Function and print to get username
getusername = input ("What is your name? ").strip().title()

# Split the username
first, last = getusername.split(" ")

# Function and print to get the user's Text Input to change to lowercase
getusertext = input ("Hello " + getusername + ". Enter your text: ").strip()

# Print the function, variable and change everything to the lowercase
print ("Here is your lowerecase text:\n\n\n" + getusertext.lower() +'\n\n\n\n')

# Print the result to be lowercase
print ("Thank You, " + getusername + ". \nYour text has been changed to lowercase \n\n")

# Print output of first and last name
print(first + " " + last)