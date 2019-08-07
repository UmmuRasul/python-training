#help execute document repeatedly 'Loops'
x = 0
while x < 10:
    print("value of x is  :" + str(x))
    x= x + 1

print("-"*100)
print("appending numbers to the list below")
l = []
y = 0
while y < 10:
    l.append(y)
    y +=1
    print("value of y is " + str(y))
print(l)