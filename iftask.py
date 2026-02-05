num1=(input)('enter number one:')
num1=int(num1)
num2=(input)('enter number two:')
num2=int(num2)
num3=(input)('enter number three:')
num3=int(num3)

if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print (num2)
else:
    print (num3)

temperature=(input)('enter the temperature:')
temperature = int(temperature)

if temperature > 30:
    print("The temperature is too high")
elif temperature > 15:
    print("Normal temperature")
else:
    print("Cold temperature")

x=(input)('enter value of x:')
x = int(x)

y=(input)('eneter value of y:')
y = int(y)

if 10 <= x <= 20 and y > 100:
    print("Conditions met")
else:
    print("Conditions not met")

password = input("Enter password: ")

if password == "secret123":
    print("Access granted")
else:
    print("Access denied")

student_score=(input)('enter student score:')
student_score = int(student_score)

attendance=(input)('enter attendance percentage')
attendance = int(attendance)

if student_score > 90:
elif attendance > 80:
    print("Excellent student")
else:
        print("Good score, but attendance needs improvement")

