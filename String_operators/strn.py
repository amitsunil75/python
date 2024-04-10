wd= 'MALAYALAM'
# COUNT IS CASE SENSITIVE
print(wd.count('M'))
# output:2
print(wd.count('M',1))
# output:1
print(wd.count('M',0,9))
# output:2
print(wd.center(20,'Y'))
# OUTPUT:YYYYYMALAYALAMYYYYYY
print(wd.encode())
# output:b'MALAYALAM'
print(wd.encode('UTF-16'))
# output:b'\xff\xfeM\x00A\x00L\x00A\x00Y\x00A\x00L\x00A\x00M\x00'
x=wd.encode('UTF-16')
print(x[4])
# output:65
print(wd.startswith('A'))
# output:False
print(wd.endswith('M'))
# output:True
print(wd.startswith('A',1))
# output:True
print(wd.startswith('A',0,1))
# output:False
print(wd.swapcase())
# output:malayalam
wd= 'malayalam'
print(wd.swapcase())
# output:MALAYALAM
print(wd.lower())
# output:malayalam
print(wd.upper())
# output:MALAYALAM
print(wd.casefold())
# output:malayalam
wgd= 'malay\talam'
print(wgd.expandtabs(5))
# output:malay     alam
print(wd.capitalize())
# output:Malayalam
print(wd.isupper())
# output:False

personalInfo = {
    "name": ["John", "Alice"],
    "profession": ["doctor", "engineer"],
    "age": ["30", "28"],
    "dob": ["01-01-1990", "02-02-1992"]
}

sentence = ("My name is {name[0]} and my name is {name[1]}. "
            "{name[0]} is a {profession[0]} and {name[1]} is a {profession[1]}. "
            "We are {age[0]} and {age[1]} respectively. "
            "The date of birth of {name[0]} is {dob[0]} and the date of birth of {name[1]} is {dob[1]}.")

print(sentence.format_map(personalInfo))

wdd='Single'
print(wdd.rfind('e'))
# output:5
print(wdd.find('g'))
# output:3
print(wdd.index('n'))
# output:2
print(wdd.rindex('i'))
# output:1
print(wdd.isupper())
# output:false
print(wdd.islower())
# output:false
print(wdd.isprintable())
# output:true
wdd='  '
print(wdd.isspace())
# output: True
print('hello'.isidentifier())
# output:True
print('4hello'.isidentifier())
# output:false
print('hwllo'.title())
# output:Hwllo
print('hwllo'.istitle())
# output : fasle
print('hwllo'.istitle())
# output:false
fgg ='ajjssk2233'
print(fgg.isnumeric())
# output:False
print(fgg.isalnum())
# output:True
fgg ='ajjssk2233...@###6&&***'
print(fgg.isalnum())
# output:False
fgg ='ajjssk2233'
print(fgg.isascii())
# output:True
print(fgg.isalpha())
# output:False
print(fgg.isdigit())
# output:False
numt='0.3444555'
print(numt.isdecimal())
# output:False
numt=0.3444555
numt= str(numt)
print(numt)