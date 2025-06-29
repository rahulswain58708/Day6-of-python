# single quote string 
a='Hello Rahul'
#Double quote string
b="Hello Rahul"
# Triple quote string ("multiline string")
c='''This is 
multiline 
       string'''
# String Indexing
text="python"
print(text[0])#output:-p
print(text[1])#output:-y
print(text[2])#output:-t
print(text[3])#output:-h
print(text[4])#output:-o
print(text[5])#output:-n
# string slicing
text="Hello, python"
print(text[0:5])#output:-Hello
print(text[7: ])#output:-python
print(text[::2])#output:-Hlo yhn
# string method:-
text="hello rahul"
#changing case
print(text.upper())#output:- HELLO RAHUL
print(text.lower())#output:-hello rahul
print(text.title())#output:- Hello Rahul
print(text.capitalize())#output:- Hello rahul
#removing whitespace
print(text.strip())
print(text.lstrip())
print(text.rstrip())
#finding and replace
print(text.find('r'))
print(text.replace("rahul","python"))
#spliting and joining
text="apple,banana,orange" 
fruties=text.split(",")
print(fruties)
#joining
new_text="-".join(fruties)
print(new_text)
#checking string properties:-
text="python123"
print(text.isalpha())#false
print(text.isdigit())#false
print(text.isalnum())#True
print(text.isspace())#false
# Built in string function
print(len(text))
#format and f-string:-
name="Rahul"
age=18
print("my name is {} and i am {} years old.".format(name,age))
print(f"my name is {name} and i am {age} years old.")
x=10
y=90
print(f"The sum of {x} and {y} is {x+y}")