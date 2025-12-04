#Day 10: 30 Days of python programming

for number in range(11):
    print(number)

i = 0
while i <11:
    print(i)
    i+= 1

for number in range(10,-1,-1):
    print(number)

i = 10
while i >-1 :
    print(i)
    i -= 1

for i in range(1,8):
    print('#'*i)

for x in range(8):
    for t in range(8):
        print('#',end='')
    print()
#another way without end
for x in range(8):
    row = "" 
    for t in range(8):
        row += "#" 
    print(row) 

a = 0
for x in range(11):
    for t in range(1):
        print(f"{a} x {a} = {a*a}",end='')
        a +=1
    print()
#another way
for i in range(11):
    print(f"{i} x {i} = {i * i}")

code_list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for x in code_list:
    print(x)

for x in range(0,101,2):
    print(x)

for x in range(1,101,2):
    print(x)
#another way
for x in range(101):
    if x % 2 != 0:
        print(x)

#Exercises 2
total_sum = 0
for x in range(101):
    total_sum +=x
print('The sum of all numbers is ',total_sum)

total_even = 0
total_odd = 0
for x in range(101):
    if x % 2 == 0:
        total_even +=x
    else: total_odd +=x
print(f"The sum of all evens is {total_even}. And the sum of all odds is {total_odd}.")

#Excercises 3
from countries import countries
for x in countries:
    if 'land' in x:
     print(x)

fruit = ['banana', 'orange', 'mango', 'lemon']
fruit_inv = []
for x in fruit[::-1]:
    fruit_inv.append(x)
print(fruit_inv)

from countries_data import countries_all
total_languages = 0
for language in countries_all:
    total_languages += len(language['languages'])
print(total_languages)

from countries_data import countries_all
dict_lang = {}
for country in countries_all:
    for language in country['languages']:
        if language in dict_lang:
            dict_lang[language]+=1
        else: dict_lang[language]=1
sorted_lang =sorted(dict_lang.items(), key=lambda item: item[1], reverse=True)
for lang, count in sorted_lang[:10]:
    print(f"{lang}: {count}")

from countries_data import countries_all
populated_count = {}
for country in countries_all:
    populated_count[country['name']]=country['population']
sorted_population = sorted(populated_count.items(),key=lambda item: item[1], reverse=True)
for country, popul in sorted_population[:10]:
    print(f"{country}: {popul}")