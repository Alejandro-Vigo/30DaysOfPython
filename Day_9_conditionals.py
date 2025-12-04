#Day 9: 30 Days of python programming

age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to learn to drive.')
else:
    print('You need 3 more years to learn to drive.')

my_age = 30
your_age = 35
difference = my_age - your_age

if difference == 1:
    print("I am 1 year older.")
elif difference > 1:
    print(f"I am {difference} years older.")
elif difference == -1:
    print("You are 1 year older.")
elif difference < -1:
    print(f"You are {-difference} years older.")
else:
    print("We are the same age.")

number_a = int(input('Number a: '))
number_b = int(input('Number b: '))
diff = number_a - number_b

if diff > 0:
    print('A greater')
elif diff < 0:
    print('A smaller')
else: print('Equals')

#Exercises 2
scores = 65
if scores >=80:
    print('A')
elif scores >=70 and scores <80:
    print('B')
elif 60 <= scores <70:
    print('C')
elif 50 <= scores <60:
    print('D')
else: print('F')

month = input('Enter the month: ')
if month in ['September', 'October','November']:
    print('Autumn')
elif month in ['December', 'January','February']:
    print('Winter')
elif month in ['June', 'July','August']:
    print('Summer')
elif month in ['March', 'April', 'May']:
    print('Spring')
else: print('Invalid month')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = 'blueberry'
if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print(fruits)

#Exercises 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person and person['skills']:
    skills = person['skills']
    middle_index = len(skills) // 2
    print(f"Middle skill: {skills[middle_index]}") 

if 'skills' in person:
    if 'Python' in person['skills']:
        print('You have Python')
else: print('You do not')

if 'JavaScript' in person['skills'] and 'React' in person['skills'] and len(person['skills']) ==2:
    print('He is a front end developer')
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills'] and len(person['skills']) >= 3:
    print('He is a back-end developer')
elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills'] and len(person['skills']) >= 3:
    print('He is a full-stack developer')
else:
    print('Unknown title')
 
if person['is_married'] == True:
    if person['country'] == 'Finland':
        print('%s %s lives in %s. He is married' %(person['first_name'],person['last_name'],person['country']))