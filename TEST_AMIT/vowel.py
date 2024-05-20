someString=input('enter a string:')
vowel=['a','e','i','o','u']
isVowel=True
for i in someString:
    if(i in vowel):
       isVowel=True
    else:
       pass
if isVowel:
   print('it is a vowel')
else:
   pass
