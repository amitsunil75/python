# methord one 
st=input('enter a string: ')
if(st !=st[::-1]):
    print('its not a palindrome')
else:
    print('its is a palindrome')
# methord 2

st=st.lower()
st_o=st
print(st_o)
st_r=reversed(st)
# print(str(st_r))
reversed_string = "".join(st_r)
print(reversed_string)
if(st_o == reversed_string):
    print('pal')
else:
    print('its not pal')