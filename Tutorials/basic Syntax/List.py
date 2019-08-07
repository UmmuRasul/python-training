courses = ['bios','his','eng','kisw','soc']
courses2 = ['geo','comp']
num = [1 , 2 , 5 , 9 , 7 , 0 , 6]

courses.append('Tech')

courses.insert(0 , 'phy')
print(courses)

courses.insert(0 , courses2)

courses.extend(courses2)

courses.remove('bios')

courses.pop()
popped = courses.pop()

print(popped)


for item in courses:
    print(item)

print("KKKKKKKKKKKKKKKKKK")
courses2.reverse()

courses2.sort()

num.sort()
print(courses[0])
print(courses[3])
print(courses[-1])

print(courses[-2])
print(courses[0:2])
print(courses[:2])
print(courses[2:])


