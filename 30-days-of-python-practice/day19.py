#what is os module
#how to find a path of a file
# why use this word?(indent)
# r只读，r+读写，不创建
# w新建只写，w+新建读写，二者都会将文件内容清零


#highlight: ensure_ascii=False line_count

# import json
# # python dictionary
# person = {
#     "name": "Asabeneh",
#     "country": "Finland",
#     "city": "Helsinki",
#     "skills": ["JavaScrip", "React", "Python"]
# }
# with open('./files/json_example.json', 'w', encoding='utf-8') as f:
#     json.dump(person, f, ensure_ascii=False, indent=4)


# import csv
# with open('./csv.csv') as f:
#     csv_reader = csv.reader(f, delimiter=',')
#     for row in csv_reader:  
#         print(f'Column names are :{", ".join(row)}')

from cgitb import text

# Q1
def read_count(path):
    with open(path) as f:
        lines = f.readlines()
        words = f.read().split()
        print(len(lines))
        print(len(words))

read_count('/Users/3w3/Desktop/30daysofPython/30-Days-Of-Python-master/data/obama_speech.txt')

#Q2
def most_spoken_language(path):
    import json
    with open(path) as f:
        countries_data_dic=json.loads(f.read())
        print(type(countries_data_dic))
    language=[]
    for i in range(len(countries_data_dic)):
            language.append(countries_data_dic[i]["languages"])
    language_list= [m for n in language for m in n]

    from collections import Counter
    language_count=Counter(language_list)
    print(language_count.most_common(10))

most_spoken_language('/Users/3w3/Desktop/30daysofPython/30-Days-Of-Python-master/data/countries_data.json')





         


