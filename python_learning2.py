"""
Type Casting in python
     1. Implicit Type Casting (Coercion)
     2. Explicit Type Casting
"""
# Implicit Type Casting
a = 7
print(type(a))

b = 3.0
print(type(b))

c = a + b
print(c)
print(type(c))

d = a * b
print(d)
print(type(d))

# Explicit Type Casting
a = 2.5
b = int(a)
print(a,b,sep=" and ")

string1 = "5"
num1 = int(string1)
print("num1 : ",num1)

string2 = "kuldeep"
# num2 = int(string2)  # Will generate Error

a = 5
n = str(a)
print("n : ",n)
print(type(n))

a = "5.9"
# n = int(a) # Cannot Directly change string that contains float Value to the integer
n = int(float(a))
print(n)
print(type(n))

n1 = 51
s1 = str(n1)
print(s1)

print(round(0.12345+0.23456,4))
print("%.5f"%(0.1+0.2))

"""
Video for understanding Exception handling in Python
    https://www.youtube.com/watch?v=NIWwJbo-9_8
"""

# Exception handling
try:
    result = 10/20
except IOError as e:
    print('Input/Output Error !')
except ZeroDivisionError:
    print("Cannot Divide by Zero",ZeroDivisionError)
except Exception as e:
    print(e)
else:
    print("No Exception Occured ! So, else is Executed ")
finally:
    print("Finally Will Always Be Executed...")


