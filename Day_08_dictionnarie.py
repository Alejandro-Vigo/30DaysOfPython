#Day 8: 30 Days of python programming

empty_dict = dict()
print(empty_dict)
dog_dict = {'name':'cies','color':'white','breed':'cottom'}
print(dog_dict)
student_dict = {'first_name':'Alex','last_name':'BD','gender':'male',
                'marital':'married','status':'worker','skills':['Python','SAP'],
                'country':'Spain','city':'Madrid'}
print(student_dict)
print(len(student_dict))
print(student_dict['skills'])
print(type(student_dict['skills']))
student_dict['skills'].extend(['SQL','Tableau'])
print(student_dict)
print(student_dict.keys())
print(student_dict.values())
print(student_dict.items())
student_dict.pop('first_name')
print(student_dict)
del student_dict
print(student_dict)