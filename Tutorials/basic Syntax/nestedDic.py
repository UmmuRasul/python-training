"""
Nested Dictionary
d = {'k1':{'nestk1':'nestval1','netk2':nestval2'}}
"""

cars = { 'bmw':{'model':'550i','year':2015}, 'benz':{'model':'657','year':2010}}
print(cars)

bnw_year = cars['bmw']['year']
print(bnw_year)

bnw_year = cars['bmw']['model']
print(bnw_year)

car = {'make':'bmw', 'model':'5501', 'year':'2019'}
print(car)

print(car.keys())
print(cars.keys())
print(car.values())
print(cars.values())


print(car.items())
print(cars.items())

car_copy = car.copy()
print(car_copy)
car.clear()
print(car)

print(cars.pop('model'))
print(cars)