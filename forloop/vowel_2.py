# using only if statement 
st = input('Enter a string: ')

if st.find('a')!=-1:
    print('its vowel')
elif st.find('e')!=-1:
    print('its a vowel')
elif st.find('i')!=-1:
    print('its a vowel')
elif st.find('o')!=-1:
    print('its a vowel')
elif st.find('u')!=-1:
    print('its a vowel using else if statement')
else:
    print('its not vowel using  using else if satement')




vowels =['a','e','i','o','u']
isVowel=False
for x in  vowels:
    if(st.find(x)!=-1):
        isVowel=True
if isVowel:
    print('its is vowel')
else:
    print('it is not vowel')



v = []
notv = set()  # Using a set to avoid duplicate non-vowel characters

for x in vowels:
    if st.find(x) != -1:
        v.append(x)
    else:
        for i in st:
            if i.lower() not in vowels and i.isalpha():
                notv.add(i)

print(f'Vowels present in the string {st} are {v}')
print(f'Number of vowels: {len(v)}')
print(f'Non-vowels present in the string {st} are {list(notv)}')
print(f'Number of non-vowels: {len(notv)}')

# output:
# Enter a string: aixngoccu
# its is vowel
# Vowels present in the string aixngoccu are ['a', 'i', 'o', 'u']
# Number of vowels: 4
# Non-vowels present in the string aixngoccu are ['c', 'x', 'n', 'g']
# Number of non-vowels: 4


    # print(nv)

# 