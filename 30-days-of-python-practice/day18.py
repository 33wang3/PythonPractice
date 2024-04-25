import re
txt='I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words=re.findall(r'[^/. ]+',txt)
frequence=[]
for a in words:
    b= words.count(a)
    if (b,a) not in frequence:
        frequence.append((b,a))
sort_frequency= sorted(frequence,key=lambda item:item[0],reverse=True)
print(sort_frequency[0:3])



# 2.
txt='The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
print(re.findall('-?\d+',txt))

# 3.
def is_valid_variable(a):
    regular_pattern1=r'^[a-zA-Z]'
    regular_pattern2=r'[^a-zA-Z0-9_]'
    if len(re.findall(regular_pattern1,a))== 0 :
        print(False)
    else:
        if len(re.findall(regular_pattern2,a)) != 0:
            print(False)
        else: print(True)

is_valid_variable('1fisjdh')
is_valid_variable('_fdsd2_')



sentence ='%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'
# print(''.join(re.findall(r'[^%@$&#;]+',sentence)))
print(re.sub(r'[%@$&#;]+','',sentence))
