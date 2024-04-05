dt={"name":"jobin","nature":"arrogant","age":"15","race":"indian"}
print(dt['name'])
# output:jobin
sd=dt.copy()
print(sd)
# output:{'name': 'jobin', 'nature': 'arrogant', 'age': '15', 'race': 'indian'}
dt['nature']   ="kind"
print(sd)
# output:{'name': 'jobin', 'nature': 'arrogant', 'age': '15', 'race': 'indian'}
print(dt)
# output:{'name': 'jobin', 'nature': 'kind', 'age': '15', 'race': 'indian'}
# print items in dict
for x,y in  dt.items():
    print(x,'\t',y,sep=':')
    kyy=dt.keys()
print(dt)
print(kyy)
# output:
#     name:   :jobin
# nature: :kind
# age:    :15
# race:   :indian
# {'name': 'jobin', 'nature': 'kind', 'age': '15', 'race': 'indian'}
# dict_keys(['name', 'nature', 'age', 'race'])
c=dt.get('age')
print(c)
# output:15
dt.update({"marks":100})
print(dt)
# output:{'name': 'jobin', 'nature': 'kind', 'age': '15', 'race': 'indian', 'marks': 100}
dt.setdefault('year',2024)
print(dt)
# output:{'name': 'jobin', 'nature': 'kind', 'age': '15', 'race': 'indian', 'marks': 100, 'year': 2024}
dt.pop("nature")
print(dt)
# output:{'name': 'jobin', 'age': '15', 'race': 'indian', 'marks': 100, 'year': 2024}
dt.popitem()
print(dt)
# output:{'name': 'jobin', 'age': '15', 'race': 'indian', 'marks': 100}
# convert list to dictionary:
li=[2,3,5,6]
newdct=dict.fromkeys(li,2)
print(newdct)
# output:{2: 2, 3: 2, 5: 2, 6: 2}
# convert tuple to dictionary
tp=33,97,88,67
newdctp = dict.fromkeys(tp,'maths')
print(newdctp)
# output:{33: 'maths', 97: 'maths', 88: 'maths', 67: 'maths'}
# convert set to dictionary
si={200,4000,8000,900,1122}
newsitcp = dict.fromkeys(si,"rent")
print(newsitcp)
# output:{8000: 'rent', 4000: 'rent', 1122: 'rent', 900: 'rent', 200: 'rent'}
# clear dt.clear()