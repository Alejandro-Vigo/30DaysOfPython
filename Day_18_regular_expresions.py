#Day 18: 30 Days of python programming

#A regular expression or RegEx is a special text string that helps to find patterns in data.

import re
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

split_list = re.findall(r'\b\w+\b', paragraph)
count_dict = {}
for item in split_list:
    count_dict[item]= count_dict.get(item,0)+1
count_list=list(count_dict.items())
print(sorted(count_list,key=lambda x: x[1],reverse=True))

points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points=[]
for number in points:
    int_number=int(number)
    sorted_points.append(int_number)
print(sorted(sorted_points))
print(max(sorted_points)-min(sorted_points))
#another way: sorted_points = sorted(map(int, points))

#Exercises 2
def is_valid_variable(variable):
    regex_pattern = r'^[a-z_]\w*$'
    if re.match(regex_pattern, variable):
        return True
    else: return False
print(is_valid_variable('first_name'))
print(is_valid_variable('first-name'))
print(is_valid_variable('1first_name'))

#another way:
#variable.isidentifier()
#return bool(re.match(regex_pattern, variable))

#Exercises 3
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
subst = ['%', '@', '#', '&','$',';','!']
pattern = f"[{re.escape(''.join(subst))}]"
cleaned_sentence = re.sub(pattern, '', sentence)
print(cleaned_sentence)


def most_frequent_words(text):
    split_list = re.findall(r'\b\w+\b', text)
    count_dict = {}
    for item in split_list:
        count_dict[item] = count_dict.get(item, 0)+1
    count_list=list(count_dict.items())
    return (sorted(count_list,key=lambda x: x[1], reverse=True))
print(most_frequent_words(cleaned_sentence))