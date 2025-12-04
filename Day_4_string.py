#Day 4: 30 Days of python programming

phrase = 'Thirty'+ ' ' +'Days'+ ' ' +'Of'+ ' ' +'Python'
print(phrase)

coding ='Coding'+ ' ' +'For'+ ' ' +'All'
print(coding)

company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[7:])
print(company.find('Coding'))
print(company.replace('Coding','OK'))
print('Python for Everyone'.replace('for Everyone','for All'))
print(company.split())
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))
print(company[0])
print(company[-1])
print(company[10])

python = 'Python For Everyone'
acronym = "".join(word[0].upper() for word in python.split())
print(acronym)
print("".join(word[0].upper() for word in company.split()))

print(company.index('C'))
print(company.index('F'))
print(company.rindex('l'))
long_phrase = 'You cannot end a sentence with because because because is a conjunction'
print(long_phrase.index('because'))
print(long_phrase.rindex('because'))
print(long_phrase[31:54])
print(long_phrase.find('because'))
print(company.startswith('Coding'))
print(company.endswith('coding'))
print('   Coding For All      '.strip())
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())
print(' # '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))
print('I am enjoying this challenge. \nI just wonder what is next.')
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

radius = 10
area = 3.14 * (radius **2)
print('The area of circle with a radius %d is %d.' %(radius,area))

a = 8
b = 6
print('%d + %d = %d' % (a, b, a + b))
print('{} + {} = {}'.format(a, b, a + b))
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')