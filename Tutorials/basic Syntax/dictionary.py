student = {'name':'Mariam', 'age': 25,'course':['his','maths']}

#update value
#student.update({'name':'Maimuna','age':'67'})

#del student['age']

print(len(student))

print(student.items())
print(student.values())
print(student.keys())

for key in student:
    print(key)

for key,value in student.items():
    print(key,value)


#adding key and values to de dictionary
student['Phone'] = '0707088562'
student['name'] = 'Zainab'

#key and values
print(student)

print(student['name'])
print(student['age'])
print(student['course'])

#if key not exisist
print(student.get('Shoes', 'Not found'))





