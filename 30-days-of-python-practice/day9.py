# age = input('Enter your age:')
# if int(age) >= 18:
#     print('You are old enough to learn to drive')
# else:
#     years = 18-int(age)
#     print('You need',years, 'more years to learn to drive.')80


# age1 = int(input('Enter first age:'))
# age2 = int(input('Enter second age:'))
# age_difference = age1-age2
# if age_difference > 0:
#     print('You are ', age_difference,'older than me.')
# elif age_difference == 0:
#     print('We are the same age.')
# else:
#     print('You are',abs(age_difference),'younger than me.')

# grade = float(input('grade of the student:'))
# if grade<= 49:
#     print('F')
# elif grade<= 59:
#     print('D')
# elif grade<= 69:
#     print('C')
# elif grade<= 89:
#     print('B')
# else: print('A')

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {'street': 'Space street','zipcode': '02210'} }

if 'skills' in person:
    if 'Python' in 'skills':
        print ('yes')
    else: print('no')

if 'skills' in person:
    skills_list = person['skills']
    len_1 = len(skills_list)
    if len_1%2 == 0:
        print(skills_list[int(len_1/2)],skills_list[int((len_1/2)+1)])
    if len_1%2 != 0:
        print(skills_list[int((len_1+1)/2)])
else: print ('no')


