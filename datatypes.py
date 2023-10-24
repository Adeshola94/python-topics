import math, random
'''Datatype is an object collection also known as object type'''
'''String Data type'''
'''String is a collection of characters'''
'''String is an list of characters'''
'''String is immutable'''
country1 = 'Nigeria'
print('I ' + 'live ' + 'in ' + country1) # string concatenation
print('I' + ' ' + 'live'+ ' ' + 'in' + ' '+ country1) # string concatenation
print('I live in', country1) 
print(f'{country1} is in Africa')
print(country1[0:3])
print(country1[6])
print(country1[-1])
print(country1[3:6])
print(country1[2:6])
print(country1[2:])
continent = 'Africa\n'
print(continent*5)
country2 = "India"
print('I live in', country2)

print(f'{country2} is in Asia') #f => formatting
print(country2, 'is in Asia')

print(f'{country1} is the most populated in Africa. {country2} is second most populated in Asia')
print(country1, 'is the most populated in Africa.', country2, 'is the second most populated in Asia.')
print(country1, country2, "is the")
# word = "Spam"
# word[0] = 'B'
# print(word)

fruit = "Orange"
print(list(fruit))

word = "Triangle"
print(word.find('angle'))
print(word.replace('Tri', 'Rect'))
word1 = 'banananana'
print(word1.replace('na', 'da'))

line = 'a, b, c, d'
print(line.split(','))
# line1 = 'a', 'b'
# print(line1.join(' '))
# 
''''
Numeric Datatypes
Integers, Floating Point, Complex Number
'''
# swapping algorithm
a = 4
b = 5
a, b = b, a
print(a)
print (b)

c = 9.9999999999
d = 9.9999999999
print(f'{c + d}')

pi = 3.14159265359
print(format(pi, ".3g")) #3 significant digit
print(repr(math.pi))
print(math.sqrt(100))

'''
Boolean Data Types
'''

s = True
y = False
z = True


'''Logical Operator are and, not, or'''
print(s and y) #false
print(s or y) #True
print(s and z) # true
print(s and y or z) # true
print(s or z and y) #true
'''and has a higher precedence before or then not'''
print(not y or s) #true
#print(s or y not z) # joining or with not gives an error

a = 30
b = 30
c = 30
result = (a + b + c)
print(result//5)
res = (a + b + c) // 5
print(res)

s = 25
y = 25
result = (s * y) + 10
print(result)

print(type(3+2j))
print(type('opeyemi'))
print(type(3.5))
print(type(3))
print(2**3)
print(10**2)
print(len(str(2**10000)))
print(random.random()*100)

'''
List DataType
List is a sequence of unordered collection
List can be mutable
'''
l = ['Malware', 'Analysis', 'is', 'good', 'to' , 'learn']
print(len(l))

print('First Element in the list is ', l[0])
print(l[0:-1:2])
l[5] = 'learnn'
print(l)

l1 = ['bread', 'pap']
l2 = l1 + ['tea']
print(l2)
print(l2[::-1])

print('bread' in l1)
'''multidimensional list'''
multilist = [[2, 3], [3, 4], [5, 6]]
print(multilist[2][0])

multilist1 = [['ade', 'bola'], ['timi', 'folake', 'john'], ['peter'], ['jimi', 'jegede', 'timperi']]
print(multilist1[3][2].capitalize() + ' is a boy')
print(multilist1[1][2].capitalize()+ ' is a pastor')

#print out 'Timperi is a boy' and 'john is a pastor'
word = "decagon"
print(word.replace('decagon', 'polygon'))

fruit = 'pineapple'
print(list(fruit))

word5 = 'implementation'
print(word5[5:])

'''Dictionary Data Type
Dictionary uses a key value pairing
Dictionary is mutable
'''
dictt = {
    'A':'America', 
    'B':'Britain',
    'C':'Canada',
}

print(dictt['A'])
print(dictt['B'] + ' is in Europe')

dictt['G'] = 'Ghana'
print(dictt)

dictt['U'] = 'Ukraine'
dictt['R'] = 'Russia'
print(dictt)
dictt.pop('U')
print(dictt)

'''
Tuples Data Type

Tuples are like list, except they are immutable and they are represented with ()
'''
tuples = (18, "True", 'Bola', 18)
print(tuples[::-1]) #reverse the tuple
print(tuples[-1]) #get last element
print(tuples.count(18))


multilist2 = [[1,2,3],[4,5,6],[7,8,9]]
for x in range(0,3):
    for y in range(0,3):
        print(multilist2[x],[y])
multilist3 = [[1,2],[3,4],[5,6],[7,8],[9,10]]
for x in range(0,5):
    for y in range(0,5):
        print(multilist3[x],[y])

print(dir(__builtins__))