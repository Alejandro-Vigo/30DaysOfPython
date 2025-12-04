#Day 7: 30 Days of python programming

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.remove('Facebook')
print(it_companies)
it_companies.discard('Amazon')
print(it_companies)

#Exercises: level 2
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))
del A,B

#Exercises: level 3
print(set(age))
words ='I am a teacher and I love to inspire and teach people'.split()
print(set(words))
print(len(set(words)))