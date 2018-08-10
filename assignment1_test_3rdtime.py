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
#SET INSTEAD OF LIST for function A
#ask if i need to have both: what I already have AND separate decrpyt, encrypt and find_encryption_offsets functions or do i just need what i already have
#fix number AND ordering of func_e
#special symbols dont work for func_a

import urllib.request
import re

def getText():
    """ Return the text in the file, 'staff.html'

    Parameters:
        No parameters

    Return:
        str: text in 'staff.html'
    """
    fd = open("words.txt") # what do the parameters for this function even mean
    text = fd.read()
    fd.close()
    return text


def function_e():
    sentence = input("Enter sentence to be encrypted: ")  #they want you to enter both the string to be encrypted and offset in the same function i think + they want you to use the exact same prompts they have used
    encryption_offset_e = int(input("Enter offset: "))
    alphabet = ("abcdefghijklmnopqrstuvwxyz")
    deciphered_text = ""


    #EXTENSION HERE
    DT_list = []
    if encryption_offset_e == 0:
        print("The encrypted text is: \n")
        for encryption_offset_e in range(1, 26): # use a dictionary for this #replace "placeholder" with "non_alphabet"
            deciphered_text = ""
            for placeholder in sentence:
                if placeholder in alphabet:      
                    deciphered_text += alphabet[(alphabet.index(placeholder) - encryption_offset_e) % (len(alphabet))]

                else:
                    deciphered_text += placeholder#char
                
            DT_list += [deciphered_text]

        for item in DT_list:
            print(str(DT_list.index(item)) + ": " + item)
    else:###        
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

def function_a():# ASK IF THIS NEEDS TO IDENTIFY #CHANGE IT TO TAKE SETS INSTEAD OF LIST ####cant handle aporsphties
    sentence = input("Enter some encrypted text: ")
    alphabet = ("abcdefghijklmnopqrstuvwxyz")
    DT_list = [0]
    
    
    for encryption_offset_e in range(1, 26): # use a dictionary for this #replace "placeholder" with "non_alphabet"
        deciphered_text = ""
        for placeholder in sentence:
            if placeholder in alphabet:      
                deciphered_text += alphabet[(alphabet.index(placeholder) - encryption_offset_e) % (len(alphabet))]

            else:
                deciphered_text += placeholder#char
                
        DT_list += [deciphered_text]

    
    text = getText()
    words_list = text.split()
    aa_holder = []
    DT_listb = [0]
    

    for aa in range(1,26):
        DT_listb.append(re.sub("[^0-9a-zA-Z]+", " ", DT_list[aa]))
        keywords_to_look_for = DT_listb[aa].split() ## can be fixed if i ask the program to look at all non-alphabets as spaces
        numbers_of_elements_to_loop_thru = len(keywords_to_look_for)

        pCounter = 0
        
        for string_ORSOMETHING in keywords_to_look_for: 
            if string_ORSOMETHING in words_list:
                pCounter += 1
                if pCounter < numbers_of_elements_to_loop_thru:
                    continue 
            
                else:
                    aa_holder.append(aa)
                    break
            else:
                break

    if len(aa_holder) == 1:
        print("Encryption offset: " + str(aa_holder[0]))
        print("Decrypted message: " + DT_list[(26 - (aa_holder[0]*aa)) % 26]) ##this i dont exactly understand but hey, it works LOL
    elif len(aa_holder) > 1:
        print("Multiple encryption offsets: ")
        for item in aa_holder:
          print(str(item))
    else:
        print("No valid encryption offset")


def function_q():
    print("Bye!")
    #code to end program or smth


Encryption_dictionary = {
    "e": function_e,
    "d": function_d,
    "a": function_a,
    "q": function_q
    }
    

def main():
    # Add your main code here
    while True:
        print("")# makes the program more readable with a newline 
        Encryption_tool_choice = input("Please choose an option [e/d/a/q]: \n"  
          "e) Encrypt some text \n"
          "d) Decrypt some text \n"
          "a) Automatically decrypt English text \n"
          "q) Quit\n")


        if Encryption_tool_choice in Encryption_dictionary:
            if (Encryption_tool_choice == "e" or Encryption_tool_choice == "d" or Encryption_tool_choice == "a"):
                Encryption_dictionary[Encryption_tool_choice]()
            else:
                Encryption_dictionary[Encryption_tool_choice]()
                break
        else:
            print("You entered an invalid choice, please try again")
            

    

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



