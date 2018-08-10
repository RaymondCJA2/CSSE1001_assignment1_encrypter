#!/usr/bin/env python3
"""
Assignment 1
CSSE1001/7030
Semester 2, 2018
"""

from a1_support import is_word_english

__author__ = "Your name & student number here"

# Write your functions here
def function_e():
    print("you picked method e")


def function_d():
    print("you picked method d")


def function_a():
    print("you picked method a")


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
