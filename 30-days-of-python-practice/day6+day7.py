# Q1 = tuple()
# Q2 = ('sansan','yituo')
# print(len(Q2))
# Q3 = ('wang','sun')
# Family_members = Q2 + Q3 
# print(Family_members)
# (siblings,parents,*other)= Family_members
# print(siblings)
# falimy_member_list = list(Family_members)
# print(falimy_member_list)
# del falimy_member_list
# del Family_members
# del siblings
# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# print('Estonia'in nordic_countries)
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()
print(removed_item)
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies_2 = {'Alibaba','Tencent'}
it_companies.update(it_companies_2)
print(it_companies)
Q1=it_companies.pop()
print(it_companies)
print(Q1)
it_companies.discard('Facebook')
print(it_companies)
A_B = A.union(B)
print(A_B)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))
age_set =set(age)
sentence = ['I', 'am' ,'a', 'teacher' ,'and', 'I', 'love', 'to', 'inspire', 'and' ,'teach' ,'people','.']
Q3 = set(sentence)
print(Q3)
print(len(Q3))
sentence1 = 'I am a teacher and I love to inspire and teach people.'
sentence1_split = sentence1.split()
print(sentence1_split)
sentence1_set = set(sentence1_split)
print(sentence1_set)