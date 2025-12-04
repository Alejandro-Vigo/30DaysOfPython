#Day 14: 30 Days of python programming

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''map() → Transforms each element: Applies a function to each item in an iterable and returns a new iterable (map object).
filter() → Filters elements based on a condition. Applies a function that returns True or False to each item. Only elements that return True are included in the output.
reduce() → Reduces an iterable to a single value. Applies a function cumulatively to elements (must import from functools). Used for aggregations like sum, product, max, etc.'''

'''Higher-Order Function (HOF): A higher-order function is a function that either:
Takes another function as an argument.
Returns a function as its result.
Closure: A closure is a function that "remembers" the variables from its enclosing scope even after the outer function has finished executing.

Key difference from HOF: All closures are higher-order functions (they return a function), but not all higher-order functions are closures (they don’t always retain state).

Decorator: A decorator is a special type of higher-order function that wraps another function to modify or extend its behavior without changing its original code.'''

square = map(lambda x: x**2, numbers)
print(list(square))
odd = filter(lambda x: x%2 == 0, numbers)
print(list(odd))
import functools
product = functools.reduce(lambda x,y: x*y, numbers)
print(product)

for country in countries:
    print(country)
for name in names:
    print(name)
for num in numbers:
    print(num)

#Exercises 2
list_upper = list(map(lambda x: x.upper(), countries))
print(list_upper)

square_list = list(map(lambda x: x**2, numbers))
print(square_list)

list_names_upper = list(map(lambda x: x.upper(), names))
print(list_names_upper)

filter_land = filter(lambda x: 'land' in x, countries)
print(list(filter_land))

filter_six = filter(lambda x: len(x)==6, countries)
print(list(filter_six))

filter_six = filter(lambda x: len(x)>=6, countries)
print(list(filter_six))

starts_e = filter(lambda x: x.startswith('E'), countries)
print(list(starts_e))

square_product = functools.reduce(lambda x, y: x*y , map(lambda x: x**2, numbers))
print(square_product)

def get_string_lists(param_list):
    str_list = list(map(lambda x: str(x), param_list)) #alternative: [str(x) for x in param_list]
    return str_list
print(get_string_lists(numbers))

sum_numbers = functools.reduce(lambda x, y: x+y , numbers)
print(sum_numbers)

concat_list = functools.reduce(lambda x,y: x +', ' + y, countries)
print(concat_list)

from countries import countries
def categorize_countries(countries_list):
    patterns = ["land", "ia", "island", "stan"]
    pattern_list = list(filter(lambda country: any(pattern in country for pattern in patterns), countries_list))
    return pattern_list
print(categorize_countries(countries))

def list_to_dict(country_list):
    dicc = {}
    for countries in country_list:
        first_letter = countries[0]
        dicc[first_letter] = dicc.get(first_letter,0)+1
    return dicc
print(list_to_dict(countries))

def get_first_ten_countries(country_list):
    return country_list[0:10]
print(get_first_ten_countries(countries))

def get_last_ten_countries(country_list):
    length_list = len(country_list)
    return country_list[length_list-10:]
print(get_last_ten_countries(countries))

#Exercises 3
from countries_data import countries_all
'''def sort_countries (country_list):
    sorted_by_name = sorted(country_list, key= lambda x: x['name'], reverse=True)
    sorted_by_capital = sorted(country_list, key=lambda x: x['capital'], reverse=True)
    sorted_by_population = sorted(country_list, key=lambda x: x['population'], reverse=True)
    return {
        'by_name': sorted_by_name,
        'by_capital': sorted_by_capital,
        'by_population': sorted_by_population}
print(sort_countries(countries_all))'''

def get_ten_languages(country_list, top_n = 10):
    dic_lang = {}
    for country in country_list:
        for language in country['languages']:
            if language in dic_lang:
                dic_lang[language] += 1
            else: dic_lang[language] = 1
    sorted_lang = sorted(dic_lang.items(), key= lambda item: item[1], reverse=True)
    return sorted_lang[:top_n]
print(get_ten_languages(countries_all))

def get_ten_populated(country_list,top_n = 10):
    sorted_population = sorted(country_list,key=lambda x: x['population'], reverse=True)
    top_populated_countries = sorted_population[:top_n]
    return [country['name'] for country in top_populated_countries]
print(get_ten_populated(countries_all))