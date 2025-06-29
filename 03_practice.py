           # Hard level
#Q1.check if a string is a palindrone.
s=input("Enter a string : ")
cleaned=s.replace(" ","").lower()
if cleaned==cleaned[::-1]:
    print("yes,it's a palindrome")
else:
    print("No,it's a not palindrome")
# Q2.Remove all vowels from a string
s=input("Enter a string : ").lower()
vowel="a,e,i,o,u"
no_vowels=' '.join([char for char in s if char not in vowel])
print("string After removing vowels : ",no_vowels )