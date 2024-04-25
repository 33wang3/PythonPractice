dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items())
dog = {}
dog['name','age','breed']='onepiece','4','mix'
print(dog)
student_dictionary ={'first_name':'one','last_name':'wang','gender':'male','age':'4','skills':['skating','running']}
print(len(student_dictionary))
print(student_dictionary.get('skills'))
skills_valule = student_dictionary.get('skills')
print(type(skills_valule))
student_dictionary['skills'].append('eating')
print(student_dictionary.items())
del student_dictionary['age']
student_dictionary.pop('skills')
print(student_dictionary)
