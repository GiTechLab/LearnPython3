__author__ = 'YS1003'

print(' Boolean & Integer ')
boolData = True
print(boolData)
# Boolean sometimes is same as int
intData = 10
print(type(boolData))
print(boolData + intData)
print(boolData + boolData)


def is_it_true(anything):
    if anything:
        print('Yes, it is true. ' + str(anything) )
    else:
        print('No, it is false. ' + str(anything))

is_it_true(boolData)
is_it_true(intData)
is_it_true(-2 * intData)
is_it_true(0.002 * intData)
is_it_true(0.00 * intData)
is_it_true(0 * intData)


print(' Float & Integer ')
intV = 2
floatV = 4.5
print(type(intV))
print(type(floatV))
print(intV)
print(floatV)
print(intV + floatV)
print(intV * floatV)
# NOTICE: data type conversion may lose data
print(intV + int(floatV))
print(int(intV * floatV))
# NOTICE: Divide returns float even if the input/output are integers
print(4 / intV)

# NOTICE: Strange divide
# If inputs are all integers, it get integer part as result, it depends on the digit dot and if it is minor value
print(12 // intV)
print(11 // intV)
print(-11 // intV)
# If inputs are not integers, it returns float as result, it depends on the digit dot and if it is minor value
print(10.3 // intV)
print(-10.3 // intV)

print(intV ** 2)
print(intV ** 3)
print(intV ** 4)
# 1 / (intV ** 2)
print(intV ** -2)
# root intV (radical)
print(intV ** 0.5)
# 1 / (intV ** 0.5)
print(1 / (intV ** 0.5))
print(intV ** -0.5)

print(4 % intV)
print(5 % intV)

# Fraction 分数
print('Fraction')
import fractions
print(fractions.Fraction(intV, 4))
print(fractions.Fraction(intV * 3, 4))
print(fractions.Fraction(6, 4))
print(intV ** fractions.Fraction(intV, 4))

# Trigonometric Function
print('Trigonometric Function')
import math
# mapping half circle
print(math.pi)
print(math.sin(math.pi / 2))
# this
print(math.tan(math.pi / 4))
