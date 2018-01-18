# Module 5 exercises

# 1. Based on Textbook R6.3
# write a loop to copy a list
'''
L1 = [1,3,5,7,8,6,4,3,0]
L1copy = []

for elem in L1:
    L1copy.append(elem)

L1copy = [ ]

for i,elem in enumerate(L1):
    L1copy[i] = elem
    

# List 5 ways to copy a list, without using a loop
L1copy = list(L1) # Easy way to copy list 
L1copy = L1[:]
L1copy = L1 + [] #not reccomened
L1copy = L1 * 1 # not advised 
L1copy = [elem for elem in L1] #list compehension 

'''

#2 Based on Textbook R6.18
# Write code to remove all negative values from a list
'''
myList = [2, -8, 12, -3, 24, -9, 29, -3, -10, 94]

value = 0
for i,elem in enumerate(myList):
    value = int(myList[i])
    if(value < 0):
        myList.remove(myList[i])        
print(myList)

'''
#Walk the list backward to pop negative values from the end to the front. The fact that elements on the right of the pop will shift left is not a problem because they are all positive.
'''
for i in range(len(myList)-1, -1, -1) :    
    if(myList[i] < 0):
        myList.pop(i)
        
#EC problem 
'''
'''
# 3. Based on Textbook R6.28
# Create a table of m rows and n cols and initialize with 0
m = 3 #rows
n = 4 #colums
table = []
for i in range(m) :
    m = [0] * n    
    table.append(m)


table = [  [0] * n for i in range(m) ]

# write a function to print the table, then call it
def printTable(t):
    for r in range(len(t)):
        for c in range(len(t[0])):
            print("%4d" %t[r][c], end= " ")
        print()
    


printTable(table)
'''
'''




# fill table with 1's
for r in range(len(table)):
    for c in range(len(table[0])):
        table[r][c] = 1
    print()
print()
printTable(table)

for r in range(len(table)):
    for c in range(len(table[0])):
        if (c + r) % 2: 
            table[r][c] = 0
            
'''          
'''
# fill table with 1's and 0's to create checkerboard pattern
for r in range(len(table)):
    for c in range(len(table[0])):
        if c % 2: # if odd
            table[r][c] = 0
    print()
print()
printTable(table)



# copy table to table2
table2 = []

for i in range (len(table)):#walk each row 0, 1, 2, 3, 4
    table2.append(list(table[i]))
                
                
table2 = [ (list(table[i]) for i in range (len(table) ]    

printTable(table2)
print()


# fill elements of top and bottom rows with 1's


table2[0] = [1] * len(table[0])
table2[-1] = [1] * len(table[0])


print()
printTable(table2)
print()

# recreate table by copying table2 to table
print()



table2[0] = list(table[0])
table2[-1] = table[-1][:]


print()
printTable(table2)

# fill elements of left and rigth cols with 1's
print()

for r in range (len(table)):
    table[r][0] = 1
    table[r][-1] = 1




printTable(table)
'''

        # right here you can change the obeject 
#myList = [elem   for elem in myList    if elem >= 0  ]
#does data change ||condition      || filter
#print(myList)
        
        
        
# Textbook P7.9
# Write a program that loops to:
# read in lines of an input file from the user,
# reverse the lines and characters in the lines, 
# store the resulting lines in an output file,
# print the number of lines and number of characters reversed.
# and print the output file
# The loop ends when the user enters no input filename

filename = input("Enter file: ")
while(filename != ""):
        with open("mod5exInput.txt") as infile :
                with open("mod5exOutput.txt", "w") as outfile:
                        lines = []
                        total = 0
                        for line in infile :
                                #print(line)
                                line = line.rstrip()[::-1]
                                lines.append(line)
                        '''        
                        for i in range(-1,len(lines)-1,-1): # -1,-2,-3, -4
                                print(lines[i])
                                outfile.write(lines[i] + "\n")
                        '''
                        total += len(line)
                        outfile.reverse()
                        for line in lines:
                                outfile.write(line + "\n")
                        print("Reversed" , numChars, "chars in", len(lines), "lines")

        
# Add exception handling for when file is not found
# Add exception handling for when file is empty


excpet 