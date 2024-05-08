string='kskdYYEDEYYEY'
lower=[]
upper=[]
for i in string:
    if(i.islower()):
        lower.append(i)
    if(i.isupper()):
         upper.append(i)
print(len(lower))
print(len(upper))

