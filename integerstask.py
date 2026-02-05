temp = 56.8926
result = round(temp)
print(result)   # 57

temp = 56.8926
result = round(temp, 2)
print(result)   # 56.89

temp = 56.8926
result = round(temp, 3)
print(result)   # 56.893

temp = 56.8926
temp_str = str(temp)

# Slice parts
integer_part = temp_str[1]        # '8'
decimal_part = temp_str[3:6]      # '926'

# Concatenate
new_temp = integer_part + "." + decimal_part

# Convert back to float
result = float(new_temp)
print(result)   # 8.926

temp = 56.8926
result = round(temp / 10, 1)
print(result)
