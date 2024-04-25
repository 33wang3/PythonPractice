import random
import string
def random_user_id(n,m):
    for i in range(m):
        print(''.join(random.choice(string.ascii_uppercase + string.digits+string.ascii_lowercase) for _ in range(n)))

random_user_id(5,8)


def rgb_color_gen():
    return (random.randint(0,256),random.randint(0,256),random.randint(0,256))
print(rgb_color_gen())

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)

print(mylist)

def shuffle_list(a):
    random.shuffle(a)
    return a
print(shuffle_list([3,9,8,6,5]))

count = 0
while count < 5:
    print(count)
    count = count + 1

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
    


