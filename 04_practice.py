#Find the longest word in sentence.
sentence="Artificial intelligence changes everthing"
words=sentence.split()
longest_word=max(words,key=len)
print("The largest word is : ",longest_word)
#mask phone number.
def mask_phone_number(phone):
    phone=str(phone)
    return "*" * 6 + phone[-4:]
#Example
phone_number=8260595178
masked=mask_phone_number(phone_number)
print(masked)
#write function using f string
name="Rahul"
age=18
print(f"Hello {name},you are {age} years old")