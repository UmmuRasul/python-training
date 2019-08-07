# a = 10
# #global variable
#
# def test_method(a):
#     print('value of local a is  ' + str(a))
#     a = 2
#     print("new value of loccal a " + str(a))
#
# print("value of global a " + str(a))
# test_method(a)
# print("value of global a change? " + str(a))



#accessing variable fr inside the method
a = 23
#global variable

def test_method():
    global a
    print('value of local a is inside de method  ' + str(a))
    a = 2
    print("new value of local a inside de method " + str(a))

print("value of global a " + str(a))
test_method()
print("value of global a change? " + str(a))
