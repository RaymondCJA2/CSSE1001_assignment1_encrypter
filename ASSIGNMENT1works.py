#!/usr/bin/env python3
"""
Assignment 1
CSSE1001/7030
Semester 2, 2018
"""

from a1_support import is_word_english

__author__ = "Raymond Chan, 45574511"

# Write your functions here
# FOR E AND D I MIGHT WANA MAKE IT SEPARATE FUNCTIONS SO I DONT HAVE TO TYPE EVERYTHING TWICE BUT IDK
def function_e():
    sentence = input("Enter sentence to be encrypted: ")  #they want you to enter both the string to be encrypted and offset in the same function i think + they want you to use the exact same prompts they have used
    encryption_offset_e = int(input("Enter offset: "))
    alphabet = ("abcdefghijklmnopqrstuvwxyz")
    deciphered_text = ""

    #placeholder can be seen as a char I THINK
    for placeholder in sentence:         #for each char in sentence
        if placeholder in alphabet:      #if that char is in the alphabet, 
            deciphered_text += alphabet[(alphabet.index(placeholder) + encryption_offset_e) % (len(alphabet))] #find the index/position of the particular char relative to alphabet. THEN add the offset to it. THEN mod it by 26
        else:
            deciphered_text += placeholder

    print("your encrypted message is: " + deciphered_text)


def function_d():
    sentence = input("Enter sentence to be encrypted: ")  #they want you to enter both the string to be encrypted and offset in the same function i think + they want you to use the exact same prompts they have used
    encryption_offset_e = int(input("Enter offset: "))
    alphabet = ("abcdefghijklmnopqrstuvwxyz")
    deciphered_text = ""

    
    for placeholder in sentence:         
        if placeholder in alphabet:      
            deciphered_text += alphabet[(alphabet.index(placeholder) - encryption_offset_e) % (len(alphabet))]  #indexed pos + offset = current ans,  you have current ans and want to get index   
        else:
            deciphered_text += placeholder

    print("your decrypted message is: " + deciphered_text)


def function_a(): #this will be tough # ASK IF THIS NEEDS TO IDENTIFY 
    sentence = input("Enter some encrypted text: ")
    #encryption_offset_e = int(input("Enter offset: "))
    alphabet = ("abcdefghijklmnopqrstuvwxyz")
    #deciphered_text = ""
    #think whether i can use a list as well for the below function
    DT_list = [0] #DT == deciphered_text, might wana add a placeholder in here for indexing to start from 1
    
    


    for encryption_offset_e in range(1, 26): # use a dictionary for this #replace "placeholder" with "non_alphabet"
        deciphered_text = "" #TRY PUTTING THIS BACK AT THE TOP
        for placeholder in sentence:
            if placeholder in alphabet:      
                deciphered_text += alphabet[(alphabet.index(placeholder) + encryption_offset_e) % (len(alphabet))]

            else:
                deciphered_text += placeholder#char
                
        DT_list += [deciphered_text]

    print(DT_list)

def function_q():
    print("you picked method q")


Encryption_dictionary = {
    "e": function_e,
    "d": function_d,
    "a": function_a,
    "q": function_q
    }
    

def main():
    # Add your main code here

    Encryption_tool_choice = input("Please choose an option [e/d/a/q]: \n"  #add an error in not edaq is entered
      "e) Encrypt some text \n"
      "d) Decrypt some text \n"
      "a) Automatically decrypt English text \n"
      "q) Quit\n")


    if Encryption_tool_choice in Encryption_dictionary:
        Encryption_dictionary[Encryption_tool_choice]()
    else:
        print("You entered an invalid choice, please try again")
        #put smth here that makes them go thru main again

    

##################################################
# !! Do not change (or add to) the code below !! #
#
# This code will run the main function if you use
# Run -> Run Module  (F5)
# Because of this, a "stub" definition has been
# supplied for main above so that you won't get a
# NameError when you are writing and testing your
# other functions. When you are ready please
# change the definition of main above.
###################################################

if __name__ == '__main__':
    main()
