# Numeric Data Types
x=1.02
# integer 
print(int(x))
# output:1
# float :contains decimels
x=7
print(float(x))
# output:7.0
# complex
x=2+3j
print(x)
# output:(2+3j)

# Boolean Data types
isRaining=True
print(isRaining)
# output:True
isHumid=True
if(isHumid and not isRaining):
    print('sunny weather')
elif(isHumid and isRaining):
    print('cool weather ')
else:
    print('rainy weather')

# output:cool weather

# other data types
# list
# dict
# set