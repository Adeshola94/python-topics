from functools import reduce

def test(a:int,b:int):
    return a*b
print(test(2,4))

def multiargs(*args):
    sum = 1
    for i in args:
        sum+=i
    return sum
print(multiargs(1,2,3,4,5))

def nextNum(num):
    return(num+1, num+2, num+3, num+4, num+5, num+6, num+7, num+8, num+9, num+10)
i1, i2, i3, i4, i5, i6, i7, i8, i9, i0 = nextNum(5)
print('Next number after 5 are ', nextNum(5))
print('Next number after 5 are ', i1, i2, i3, i4, i5, i6, i7, i8, i9, i0)

#Lambda function ia an anonymous function
add5 = lambda x:x+5
print(add5(6))

addandmltp = lambda x:x+5*3
print(addandmltp(1))

def anything1(num):
    return lambda x:x*num
print(anything1(9)(4))

def anything(num):
    return lambda x:x+num
print(anything(9)(4))
oneToTwelve = range(1,13)
mult_by_2 = lambda x:x*2
print(list(map(mult_by_2, oneToTwelve)))

oneToTwelve = range(1,13)
mult_by_2 = lambda x:x*3
print(list(map(mult_by_2, oneToTwelve)))

#Filter with Lambda
#print out only even numbers from a range to infinity
print(list(filter((lambda x:x%2 == 0), range(1,10))))
print(list(filter((lambda x:x%3 == 0), range(1,100))))
print(list(filter((lambda x:x*3), range(1,100))))

# Reduce
print(reduce((lambda num1, next_num: num1+next_num), range(1,11)))
print(reduce((lambda num1, next_num: num1*next_num), range(1,6)))
'''
i = 1
while(i<101):
    if(i%2==0):
        print(i, "is even")
    else:
        print(i, 'is odd')

'''
# Variable/Function Lookup hierarchy
# Python uses the LEGB Rule for variable/function lookup hierarchy
# L => Local, E => Enclosing, G => Global, B => Builtin
# r = 3
# def test(arg):
#   t = 4    
#   def test(args):
#       y = 3

X = 88
def tet():
    X = 99
tet()
print(X)

# global allows us to change names that lives outside a def at the top level of a 
# module file 

X = 88
def tet():
   global X 
   X = 99
tet()
print(X)