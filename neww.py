def square_number(num):
    square = num **2
    return square

x=square_number(4)
print(x)
y=square_number(23)
print(y)

def cube_number(num):
    cube = num **3
    return cube

m=cube_number(3)
print(m)
n=cube_number(34)
print(n)

# def add_numbers(a, b):
#     sum = a + b
#     print(sum)

# add_numbers(10, 20)

def check_password(password):
    if password == "secret123":
       result= "Access granted"
    else:
        result="Access denied"
    return result


d=check_password("secret123")
print(d)
r=check_password("jambo")
print(r)

