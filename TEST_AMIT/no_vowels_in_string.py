strings = input('Enter a string: ')
vowels = set('aeiou')
countConsonants = {}

prev_char_is_vowel = False

for char in strings:
    if char in vowels:
        prev_char_is_vowel = True
    else:
        if prev_char_is_vowel:
            if char in countConsonants:
                countConsonants[char] += 1
            else:
                countConsonants[char] = 1
        prev_char_is_vowel = False  # Reset the flag after a consonant

print(countConsonants)



