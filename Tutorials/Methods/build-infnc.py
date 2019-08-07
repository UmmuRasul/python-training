def largest(*args):
    print(max(args))

largest(-20, -9, 0, 6, 19)


def largest(*args):
    print(max(args))
    return(max(args))

x = largest(-20, -9, 0, 6, 19)


def small(*args):
    print(min(args))

small(-20, -9, 0, 6, 19)

def small(*args):
    print(min(args))
    return(min(args))

x = small(-20, -9, 0, 6, 19)

def abs_fnc(a):
    print(abs(a))

abs_fnc(6)
abs_fnc(-9)

print(type(99))
print(type(99.9))
print(type('999'))

l =  [2, 1, 4]
print(type(l))

t = (6, 7)
print(type(t))

d = {'key':'val'}
print(type(d))
