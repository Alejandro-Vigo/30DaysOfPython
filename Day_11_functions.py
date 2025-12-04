# Day 11: 30 Days of python programming

def add_two_numbers(one, two):
    return one + two
print(add_two_numbers(1,1))

def area_circle(radius):
    pi=3.14
    return print('Area: ', pi*radius*radius)
area_circle(2)

def add_all_nums(*nums):
    sum_num = 0
    for num in nums:
         if type(num) != int:
            return('Not a number')
         sum_num += num
    return sum_num
print(add_all_nums(1,'tres',3))

def convert_celsius_to_fahrenheit(celsius):
    return (celsius*(9/5))+32
print(convert_celsius_to_fahrenheit(15))

def check_season(month):
    if month in ('June','July','August'):
       return ('Summer')
    elif month in ('September','October','November'):
        return ('Autumn')
    elif month in ('December','January','February'):
        return ('Winter')
    elif month in ('March','April','May'):
        return ('Spring')
    else: return ('Not a month')
print(check_season('July'))

def calculate_slope(equation):
    equation = equation.replace(" ",'')
    if equation.startswith('y='):
        equation= equation[2:]
    if 'x' in equation:
        slope_part = equation.split('x')[0]
        return float(slope_part)
    else: return 'No valid x found'
print(calculate_slope('y=3x+1'))

import math
import cmath
def solve_quadratic_eqn(a,b,c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b+math.sqrt(discriminant))/(2*a)
        x2 = (-b-math.sqrt(discriminant))/(2*a)
    else: 
        x1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        x2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    return (x1,x2)
print(solve_quadratic_eqn(1,1,1))

car_list = ['Porsche','Ferrari','Bentley']
def print_list(param_list):
    elements = []
    for x in param_list:
     elements.append(x)
    return elements
print(print_list(car_list))

def reverse_list(array):
    new_list = []
    for x in range(len(array)-1,-1,-1):
        new_list.append(array[x])
    return new_list
print(reverse_list([1,2,3]))

def capitalize_list_items(items):
    capitalized_list = []
    for item in items:
        capitalized_list.append(item.capitalize())
    return capitalized_list
print(capitalize_list_items(["apple", "banana", "cherry"]))  

def add_item(items_list, *items):
    for item in items:
        items_list.append(item)
    return items_list
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat')) 

def add_item(items_list, *items):
    for item in items:
        items_list.remove(item)
    return items_list
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Mango')) 

def sum_of_numbers(number):
    sum_number= 0
    for x in range(number+1):
        sum_number+=x
    return sum_number
print(sum_of_numbers(5))

def sum_of_odds(number):
    sum_odds = 0
    for x in range(number+1):
        if x % 2 != 0:
            sum_odds+=x
    return sum_odds
print(sum_of_odds(5))

def sum_of_even(number):
    sum_even = 0
    for x in range(number+1):
        if x % 2 == 0:
            sum_even+=x
    return sum_even
print(sum_of_even(5))

#Exercises 2
def evens_and_odds(integer):
    sum_odds = 0
    sum_evens = 0
    for x in range(integer+1):
        if x % 2 == 0:
            sum_evens+=1
        else: sum_odds+=1
    return (sum_odds,sum_evens)
print(evens_and_odds(5))
#another easy way
def evens_and_odds(n):
    evens = (n // 2) + 1
    odds = n // 2
    return (odds, evens)

def factorial(number):
    mul_number = 1
    for x in range(1,number+1):
        mul_number *= x
    return mul_number
print(factorial(5))

def is_empty(value):
    return not bool(value)
print(is_empty(''))

def calculate_mean(lists):
    sum_list = 0
    for item in lists:
        sum_list +=item
    mean = sum_list/len(lists)
    return mean
print(calculate_mean([1,2,3]))
#another easy way
def calculate_mean_two(lists):
    return sum(lists)/len(lists)
print(calculate_mean_two([1,2,3]))

def calculate_median(lists):
    sorted_list = sorted(lists)
    mid = len(sorted_list) //2
    if len(sorted_list)%2 ==0:
        median = (sorted_list[mid -1] + sorted_list[mid])/2
    else: median =sorted_list[mid]
    return median
print(calculate_median([2,1,3,4]))

def calculate_mode(number_list):
    frequency = {}
    for num in number_list:
        if num in frequency:
            frequency[num] +=1
        else: frequency[num] = 1
    max_count = max(frequency.values())
    mode = []
    for key, value in frequency.items():
        if value == max_count:
            mode.append(key)
    return mode
print(calculate_mode([1,1,6,2,3,6,6,1,6,7]))

def calculate_range(range_list):
    if not range_list:
        return None
    return max(range_list) - min(range_list)
print(calculate_range([2,3,5,1,9,7]))

def calculate_variance(data):
    n = len(data)
    if n < 2:
        return None
    mean = sum(data)/n
    squared_diff = sum((x - mean) ** 2 for x in data)
    variance = squared_diff / (n - 1)
    return variance
print(calculate_variance([2,3,5,6,8,4]))

def calculate_std(data):
    variance = calculate_variance(data)
    std_deviation = math.sqrt(variance)
    return std_deviation
print(calculate_std([2, 3, 5, 1, 9, 7]))

#Exercises Level 3
def is_prime(number):
    if number <=1:
        return False
    elif number ==2:
        return True
    elif number % 2 == 0:
        return False
    else: 
        for i in range(3,int(math.sqrt(number))+1,2):
            if number % i == 0:
                return False
        return True
print(is_prime(4))

def is_unique(unique_list):
    frequency = {}
    for num in unique_list:
        if num in frequency:
            frequency[num] +=1
        else: frequency[num] = 1
    max_count = max(frequency.values())
    if max_count >1:
        return False
    else: return True 
print(is_unique([3,5,1,5,'Apple']))
#another easy way -> set doesn't allow duplicate values
def is_unique(unique_list):
    return len(unique_list) == len(set(unique_list))

def same_data(data_list):
    type_str,type_int,type_float = 0,0,0
    for item in data_list:
        if type(item) == int:
            type_int +=1
        elif type(item) == str:
            type_str +=1
        elif type(item) == float:
            type_float +=1
    if type_float == type_int ==type_str:
        return True
    else: return False
print(same_data([3,5,1,5,'Apple']))
#another way only comparing the first element
def are_all_same_type(data_list):
    first_item_type = type(data_list[0]) 
    for item in data_list:
        if type(item) != first_item_type:
            return False
    return True

import keyword
def is_valid_variable(variable):
    return variable.isidentifier() and not keyword.iskeyword(variable)
print(is_valid_variable("my-var"))

from countries_data import countries_all
def most_spoken_languages(list_countries, top_n=10):
    language_count = {}
    for country in list_countries:
        for language in country['languages']:
            if language in language_count:
                language_count[language] +=1
            else: language_count[language] = 1
    sorted_languages = sorted(language_count.items(),key=lambda item: item[1], reverse=True)
    top_languages = sorted_languages[:top_n]
    return top_languages
print(most_spoken_languages(countries_all))

def most_populated_countries(list_countries, top_n=10):
    populated_count = {}
    for country in list_countries:
        populated_count[country['name']]=country['population']
    sorted_population = sorted(populated_count.items(),key=lambda item: item[1], reverse=True)
    top_population = sorted_population[:top_n]
    return top_population
print(most_populated_countries(countries_all))