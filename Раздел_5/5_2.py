car_1 = 'honda'
car_2 = 'ferrari'
print(car_2 == 'honda')
print(car_1 == 'ferrari')
print(car_1 == car_2)
print()

car = 'Audi'
print(car.lower() == 'audi')
print(car.title() == 'Audi')
print(car.upper() == 'AUDI')
print()

a,b,c,d = 1,2,3,4
print(a+b == c)
print(a-d/c == d)
print(d/b == b)
print(b**b == d)
print(a>d)
print(d<a+b+c)
print(b<=a+a)
print(b>=a+a+a)
print()

age_1 = 16
age_2 = 18
print(age_1>=17 and age_2>=17)
print(age_1>=17 or age_2>=17)
print()

cars = ['audi', 'bmw', 'subaru', 'ifinity']
print('honda' in cars)
print('bmw' not in cars)
print('honda' not in cars)
print('bmw' in cars)