'''
It takes user integer input, makes sure that the input is greater than 20. 
When input is greater than 20, it find the power raised to 2.
Break
'''
'''

while True:
    reply = input('Enter your integer input: ')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad' * 8)
    else:
        num = int(reply)
        if num < 20:
            print('low! Enter an higher value of 20 or greater')
        else:
            print(f'{num} multiplied by itself is: ', num ** 2)
            break
print('Bye!!')
'''

'''
for:
else:

while:
else:
'''
items = ['aaa', 111, (4, 5), 2.01]
test = [(4,5), 3.14]

for i in test:
    for x in items:
        if x == i:
            print(i, ' was found')
            break
    else:
        print(i, ' was not found')

# Refactor this code
items1 = ['bola', 232, (8, 5), 2.01]
test1 = [(4,9), 2.14]

for a in test1:
    for u in items1:
        if u == a:
            print(u, ' was found')
            break
    else:
        print(a, ' was not found')
while True:
    reply = input('Enter your integer input: ')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad' * 5)
    else:
        num = int(reply)
        if num < 20:
            print('low! Enter an higher value of 20 or greater')
        else:
            print(f'{num} multiplied by itself is: ', num ** 3)
            break
print('Bye!!')

