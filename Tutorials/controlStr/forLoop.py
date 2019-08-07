my_string = 'abcabc'

print("-"*20 +"strings for loop" + "-"*20)
# for c in my_string:
#     print(c)
#     print(c, end=" ")


for c in my_string:
    if c =='a':
        print('A', end=" ")
    else:
        print(c, end=" " )


print("f"*100)
print("-"*20 +"list for loop" + "-"*20)
cars = ['bmw', 'masedez', 'benz']

for cars in cars:
    print(cars)

nums = [1, 2, 3, 4, 5]
for n in nums:
    print(n * 10)



print("*" *30)
print("-"*20 +"dictionaries for loop" + "-"*20)
d = {'one': '1', 'two': '2', 'three': '3'}
for k in d:
    print(k)
    print(k + " " + str(d[k]))


print("*" *90)
for k, v in d.items():
    print(k,v)
    print(k)
    print(v)
