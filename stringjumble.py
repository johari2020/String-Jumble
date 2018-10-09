"""
stringjumble.py
Author: johari
Credit: megsnyder, https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
https://stackoverflow.com/questions/529424/traverse-a-list-in-reverse-order-in-python
https://stackoverflow.com/questions/4481724/convert-a-list-of-characters-into-a-string

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""

st= input("Please enter a string of text (the bigger the better)")

print('You entered "' + st + '". Now jumble it: ') 

def reverse(st): 
  str = "" 
  for i in st: 
    str = i + str
  return str
print(reverse(st))

l= list(st)
j=len(l)
k=0
m=0
'''
for f in st:
    if f == " ":
        w = [j-k:j-j:1])
        print(w)
        m+=len(w)
    k+=1
'''
for i in reversed(l):
    if i == " ":
        r=(l[j-k:j-m:1])
        c = ""
        for i in r:
            c += i
        print((c))
        m+=len(r)
    k+=1
    
d=((l[:j-m]))
c = ''.join(d)
print(c)


o=1
z=0
t=0
y=0
#for f in reversed(l): 
    #if f ==" ": 
     #   l.sort()
     #   w = (l[:j-z:1])
    #    print(w)
    #    y+=len(w)
    #    m+=1
  #  t+=1
    
#print(w)
#x = (w[j-m:])
#print(x)
for i 
def reverse(st): 
  str = "" 
  for i in st: 
    str = i + str
  return str
print(reverse(st))



