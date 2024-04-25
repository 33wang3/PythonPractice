# from re import X


# def print_fullname(firstname, lastname):
#     space = ' '
#     full_name = firstname  + space + lastname
#     print(full_name)
#     return full_name
# print(print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh'))

# def is_even (n):
#     if n % 2 == 0:
#         return True    # return stops further execution of the function, similar to break 
#     return False
# print(is_even(10)) # True

# def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
#     space = ' '
#     full_name = first_name + space + last_name
#     return full_name

# print(generate_full_name())
# print(generate_full_name('David','Smith'))

# def generate_groups (team,*args):
#     print(team)
#     for i in args:
#         print(i)
# print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))

# def square_number (n):
#     return n * n
# def do_something(f, x):
#     return f(x)
# print(do_something(square_number, 3))

#Q1 
from audioop import reverse
from unittest import result


def add_two_numbers(a,b):
    return a+b
print(add_two_numbers(3,4))

#Q2
def area_of_circle(r):
    print('area_of_circle:',r)
    return 3.14*r*r
print(area_of_circle(3))

def convert_celsius_to_farenheit(C):
    return (C*9/5)+32
print('F=',convert_celsius_to_farenheit(32))

def check_season(month):
    if month in [11,12,1,2]:
        month = 'winter'
    elif month in [3,4,5]:
        month = 'spring'
    elif month in [6,7,8]:
        month = 'summer'
    elif month in [9,10]:
        month = 'autumn'
    return month
print((check_season(5)))


def print_list(list):
    for n in list:
        print(n) 
print_list(['onepiece','onebing'])

list_2 = []
def reverse_list(list_2):
    list_2.reverse()
    return list_2
print(reverse_list([3,5,7]))



def capitalize_list_items(list):
    list_6 = []
    for n in list:
        n = n.capitalize()
        list_6.append(n)
    return list_6

list1 = ["Hello", "how", "are", "you"]
print(capitalize_list_items(list1))


def add_item(list_4,item):
     list_5 = list_4.append(item)
     return list_4 
number = [2,3,7]
print(add_item(number,5))

def sum_of_odds(n):
    result=0
    for i in range(n):
        if i % 2 == 0:
            result = result+i
    return result
print(sum_of_odds(9))


def evens_and_odds(n):
    if n<=0 or isinstance(n,int) == False:
        print('Wrong parameter')
    else:
        even_list = []
        odd_list =[]
        for i in range(1, n+1):
           if i%2 == 0:
                even_list.append(i)
           else:
                odd_list.append(i)
        print('The number of evens are',len(even_list))
        print('The number of odds are',len(odd_list))

evens_and_odds(50)

def is_empty(item):
    if len(item)== 0:
        print ('is_empty')
    else:
        print('not_empty')

def check_unique(list):
    if list == set(list):
        print ('all unique')
    else:
        print('not unique')
check_unique([5,7,7])

def check_datatype(list):
    for i in range(len(list)-1):
        if not(type(list[i])==type(list[i+1])) :
            return ('not the same type')
    return ('same type')
print(check_datatype([3,5,'string']))


type_list = []
def check_datatype(list):
    for i in list:
        type_list.append(type(i))
    if len(set(type_list)) == 1:
        print('same type')
    else: 
        print('not same type')

check_datatype([3,5,'58'])

import random
def random_unique_array():
    random_list = []
    while len(random_list) < 7:
        a=random.randint(0,9)
        while not(a in random_list):
            random_list.append(a)
    random_list.sort()
    return random_list

print(random_unique_array())
    

        

