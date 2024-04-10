
# if st.find('a')!=-1:
#     print('its vowel')
# elif st.find('e')!=-1:
#     print('its a vowel')
# elif st.find('i')!=-1:
#     print('its a vowel')
# elif st.find('o')!=-1:
#     print('its a vowel')
# elif st.find('u')!=-1:
#     print('its a vowel')
# else:
#     print('its not vowel')

# print(st.find('i'))

st = input('Enter a string: ')
vowels =['a','e','i','o','u']
isVowel=False
for x in  vowels:
    if(st.find(x)!=-1):
        isVowel=True
if isVowel:
    print('its is vowel')
else:
    print('it is not vowel')