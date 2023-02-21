# Area of a Triangle
a = float(input('Enter the first side: '))
b = float(input('Enter the second side: '))
c = float(input('Enter the third side: '))
if (a+b) > c and (a+c) > b and (b+c) > a :
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c)) ** 0.5
    print('Area = %0.2f' %area)
else:
    print('This values can not form a triangle')