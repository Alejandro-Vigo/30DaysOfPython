#Day 13: 30 Days of python programming

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print([num for num in numbers if num <=0])

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_list = [num for sublist in list_of_lists for row in sublist for num in row]
print(flatten_list)

list_of_tuples = [(num, 1, num, num**2, num**3, num**4, num**5, num**6) for num in range(11)]
print(list_of_tuples)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_list = [(country.upper(), country[:3].upper(),capital.upper()) for sublist in countries for capital, country in sublist]
print(new_list)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_dicc = [({'country': country.upper(), 'city': city}) for sublist in countries for country, city in sublist]
print(new_dicc)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
new_list = [(name + ' ' + surname) for sublist in names for name,surname in sublist]
print(new_list)

slope = lambda x1, y1, x2, y2: (y2-y1)/(x2-x1)
y_intercept = lambda x1,y1,x2, y2: y1 - slope(x1,y1,x2,y2) * x1
print(slope(1,2,2,2))
print(y_intercept(1,1,1,1))