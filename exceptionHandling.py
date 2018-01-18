
'''
How to read/write a file and handle exception

A. Using if else
ask for filename
while user enters a name 
   call OS methods to search for filename in the current directory
   if not found
       print error message
   else
       open file
       process file
   ask for filename


B. Using try except
ask for filename
while user enters a name
   try
       open file
       process file
   except
       print error message
   ask for filename
'''


# How to read a number for the user and handle exception
#num = int(input("Enter an integer: "))
#print(num)

# without exception handeling 
   
num = input("Enter an integer: ")

if (num.isdigit()):
    print(int(num))
else:
    print("Error")
    
    
try:
    num = int(input("Enter an integer: "))
    print(num)   
except:
    print("Error")