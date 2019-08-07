bool_output = True or not False and False
print(bool_output)

# not is evaluated first the and last or


d = 10 == 10 or not 10 > 10 and 10 > 10
print(d)

d1 = (10 == 10 or not 10 > 10) and 10 > 10
print(d1)

#() changes the order dat y false