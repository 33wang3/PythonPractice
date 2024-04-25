from re import A, I
from tkinter import N


numbers =[-4,-3,-2,-1,0,2,4,6]
numbers_filtered = [i for i in numbers if i >0 ]
print(numbers_filtered)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_list =[i for n in list_of_lists for m in n for i in m]
print(flatten_list)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
Q4 = [i for n in countries for m in n for i in m]
print(Q4)

Q5 = [{'countries': i,'city':n} for [(i,n)] in countries]
print(Q5)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
Q6 = [i+' '+m for n in names for (i,m) in n ] 
print(Q6)

Q3 = [(n,n**0,n**1,n**2,n**3,n**4,n**5) for n in range(11)]
print(Q3)