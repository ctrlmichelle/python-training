name=" JOHn ." 
name=name.replace('.' , '')
name=name.strip()
name=name.lower()
print(name)

sentence_one="The Dog Breed Is German Shepherd"
print(sentence_one[7:24])

sentence_two="Defeats for the Clinton forces, this was her moment of triumph"
print(sentence_two[15:30])

text="The lazy dog; ran so fast; it hit the wall."
text=text.split(";")
print(text)
print(len(text))

first_name=" Joh.n"
last_name=" Do,e"
first_name=first_name.replace(".", "")
first_name=first_name.strip()
last_name=last_name.replace(",", "")
last_name=last_name.strip()
full_name=first_name + " " + last_name
print(full_name)

r ='["E", "W", "C"]'
r=r.replace('[', '')
r=r.replace(",", " ")
r=r.replace('"', '')
r=r.replace(']', '')
print(r)

r= r[2:11]
r=r.replace(",", " ")
r=r.replace('"', '')
print(r)
