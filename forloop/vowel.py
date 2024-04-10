st = input('Enter a string: ')
vowels = ['a', 'e', 'i', 'o', 'u']
e = []

# Check if the input string contains any alphabetic characters
if st.isalpha():
    for char in st:
        if char.lower() in vowels:
            e.append(char)
else:
    print('Invalid input!')

# Check if the list of found vowels is empty
if not e:
    print('There are no vowels in the string.')
else:
    print('The following vowels are present in the string:', ', '.join(e))

# output:
# Enter a string: aeiour
# The following vowels are present in the string: a, e, i, o, u

# Enter a string: dfjjfkgbjk
# There are no vowels in the string.

