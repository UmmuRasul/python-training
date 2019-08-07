"""
and
true and true --->true
true and false --->false
false and false ---> false

****************************

or
true or true --->true
true or false ---> true
false or false -->false
*****************************
not
not false --> true
not true --> false

"""
print(" ---------------------------  a      n       d     -------------------------")
c1 =(10 == 10) and (10 > 9)
c2 =(10 == 10) and (10 < 9)
c3 =(10 != 10) and (10 < 9)
print(c1)
print(c2)
print(c3)

print("--------------   o        r       -------------------------")
d1 =(10 == 10) or (10 > 9)
d2 =(10 == 10) or (10 < 9)
d3 =(10 != 10) or (10 < 9)
print(d1)
print(d2)
print(d3)


print("---------------    n        o           t    -------------")
s1 = not (10==10)
s2 = not (10!=10)
print(s1)
print(s2)



