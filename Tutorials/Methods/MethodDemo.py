def add(n1, n2):
    """
    get sum of two parametre
    :param n1:
    :param n2:
    :return:
    """
    # print(n1 + n2)
    return n1+n2


sum1 = add(2, 8)
sum2 =  add(4, 8)

print(sum1)
print("*"*80)


l= [1,2,3,4,5]
l.append(6)
print(l)
print(len(l))

print("*" *30)
def ismetro(city):
    o = ['msa', 'Nai']

    if city in o:
        return True
    else:
        return False

x = ismetro('msa')
print(x)