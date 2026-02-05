num1 = (input)("Enter first number: ")
num1 = int(num1)
num2 = (input)("Enter second number: ")
num2 = int(num2)
num3 = (input)("Enter third number: ")
num3 = int(num3)
num4 = (input)("Enter fourth number: ")
num4 = int(num4)

if num1 > num2 and num1 > num3 and num1 > num4:
    print("The largest number is:", num1)

elif num2 > num1 and num2 > num3 and num2 > num4:
    print("The largest number is:", num2)

elif num3 > num1 and num3 > num2 and num3 > num4:
    print("The largest number is:", num3)

else:
    print("The largest number is:", num4)
