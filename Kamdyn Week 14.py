#Name: Section19.6problem1
#Purpose:  Exceptions
#Author: KamdynHagerty
#Created: 4/28/26




def readposint():
   while True:
       user_input = input("Please enter a positive integer: ")
       if user_input.isdigit():
           user_int = int(user_input)
           if user_int > 0:
               return user_int
       print("Invalid input. Try again.")
