#Day 6: 30 Days of python programming

empty_tuple = tuple()
bro_tuple = ('Jorge','Carlos')
sis_tuple = ('Mati','Patricia')
siblings = bro_tuple + sis_tuple
print(siblings)
print(len(siblings))
family_members = siblings + ('Marta','Juan')
print(family_members)

#Exercises: Level 2
*siblings_unpack, parents = family_members[:-2], family_members[-2:]
print(siblings_unpack, parents)
fruits = ('apple','banana')
vegetables = ('tomato', 'avocado')
animals = ('horse','bull')
food_stuff_tp= fruits + vegetables + animals
print(food_stuff_tp)
print(list(food_stuff_tp))
print(food_stuff_tp[2:4])
print(food_stuff_tp[0:3], food_stuff_tp[3:6])
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)