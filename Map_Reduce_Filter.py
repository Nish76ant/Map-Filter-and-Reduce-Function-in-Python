#Map Filter and Reduce

#Map Function

"""
numbers = ['3','34','64']
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

numbers[2] = numbers[2]+1
print(numbers[2])
"""
# #Map Function
# numbers = ['3','34','64']
# numbers = list(map(int,numbers))
# print(numbers)

# #In Map function we at wirst we give function 
# def sq(a):
#     return a*a
# num = [2,3,5,6,76,3,3,2]
# sqare = list(map(sq,num ))
# print(sqare)


# #In Map function using lambda function
# num = [2,3,5,6,76,3,3,2]
# square = list(map(lambda x: x*x,num))
# print(sqare)
"""
def sqare(a):
    return a*a

def cube(a):
    return a*a*a

func = [sqare,cube]

num = [2,3,5,6,76,3,3,2]
for i in range(5):
    val = list(map(lambda x :x(i),func))
    print(val)
"""

#Filter Function

list1 = [1,2,3,4,5,6,7,8,9]

def is_greater_5(num):
    return num>5

gr_than_5 = list(filter(is_greater_5,list1))
print(gr_than_5)


#Reduce Function
from functools import reduce
list1 = [1,2,3,4]
num  = reduce(lambda x,y:x+y,list1)
print(num)

"""

list1 = [1,2,3,4]
num = 0
for i in list1:
    num = num+i
print(num)
"""
