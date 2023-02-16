# Square root of real or complex numbers like 1+2j
import cmath
num = eval(input("Enter Complex number: "))
sqrt = cmath.sqrt(num)
print("The square root of {0} is {1:0.3f}+{2:0.3f}j".format(num, sqrt.real, sqrt.imag))