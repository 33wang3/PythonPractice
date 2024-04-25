import numpy
numpy.version.version
lst = [1, 2, 3,4, 5]
np_arr = numpy.array(lst)
np_arr
len(np_arr)

import requests
url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
response = requests.get(url)
print(response.headers)

class Person:
  pass
print(Person)

class person_account:
    pass

import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'
response = requests.get(url)
status = response.status_code
print(status)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.body)

url='https://archive.ics.uci.edu/ml/datasets.php'
response=requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
