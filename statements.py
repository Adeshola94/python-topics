import sys
from functools import reduce
# Statement are things you write to tell python what to do



password = 'python3'
checker = input('Enter the password ')
if checker == password:
    print('Password successful')
    # if the first condition is not true, it defaults to else
else:
    print('Wrong password')





age = int(input("Enter your current age: "))
if age > 21:
    print('You can drive a Tractor')
elif age >= 16:
    print('You can drive a car')
else:
    print("You can\'t drive")

m_age = int(input("Enter your current age : "))
if m_age < 5:
    print('You cant start school')
elif m_age >= 5 and m_age <= 6:
    print('Go to Kindergaten')
elif m_age > 6 and m_age <= 18:
    print('You should be in Grade', m_age-5)
else:
    print('Go to College')



# Tenary Operator
# Tenary Operator is a short form of writing if else statements


canVote = 30
voting= True if canVote>=18 else False
print(voting)


canRead = 2
read = 'Yes you can read' if canRead >=5 else 'You cant read'
print(read)



#Looping 

'''
variable
while variable is true
do this
increment
'''
num = 1
while num <= 10:
    print(num)
    num += 1


num1 = 1
while num1 <= 20:
    if num1 % 2 == 0: # checking out if a particular number is even
        print(num1)
    num1 += 1


# Assignment 
# 1. Find the differences between json and dictionary
# a while loop that displays odd numbers 

g_even = 1
while(g_even <= 20):
    if g_even % 2 == 0:
        print('Even Number: ', g_even)
    elif g_even == 15:
        break
    else: 
        g_even += 1
        continue
    g_even += 1


# For Loop
# for variable in range():


for i in range(3):
    print('Howdy')

list1 = ['MRE', 'Palo Alto', 115000, 'Norway']
for i in list1:
    print(i, '', end='')
print()

multilist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for x in range(0, 3):
    for y in range(0, 3):
        print(multilist[x], [y])

multilist2 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
for x in range(0, 5):
    for y in range(0, 2):
        print(multilist2[x], [y])

for i in range(0,10,2):
    pass 