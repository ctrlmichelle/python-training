
myname="Ropy Kevin"
print(myname.upper())
myname = myname.upper()
print(myname)
myname=myname.lower()
print(myname)

x="   Python Programming  "
print(x)
x=x.strip()
print (x)

# clean Full_name="   rOpy KEvin  "  to "ropy kevin"
full_name="   rOpy KEvin  "
full_name=full_name.strip()
full_name=full_name.lower()
print(full_name)

# replace =>
myname = "Ropy Kevin"
print(myname)
myname=myname.replace('Kevin','Alex')
print(myname)

# Clean text = "PyTHon PROGraMming   " to "JAVA PROGRAMMING"
text="PyTHon PROGraMming   "
text=text.strip()
text=text.upper()
text=text.replace("PYTHON","JAVA")
print(text)

text="I am a python, student"
print(text.split(','))
print(text)

text="I am a python student"
print(text.count("I"))
print(len(text))




