# set 
st={100,500,131,221,222,900,131,331}
print(st)
# output:{131, 900, 100, 500, 331, 221, 222}
for x in st:
    print(x)
# output:
# 131
# 900
# 100
# 500
# 331
# 221
# 222

st.add(333)
print(st)
# output :{131, 900, 100, 500, 331, 333, 221, 222}
st.update({20,29,30})
print(st)
# output:{131, 900, 100, 331, 333, 29, 500, 20, 30, 221, 222}
st.remove(333)
print(st)
# output:{131, 900, 100, 331, 29, 500, 20, 30, 221, 222}
st.discard(900)
print(st)
# output:{131, 100, 331, 29, 500, 20, 30, 221, 222}
print(max(st))
# output:500
print(min(st))
# output:20
print(sorted(st))
# output:[20, 29, 30, 100, 131, 221, 222, 331, 500]
print(sorted(st,reverse=True))
# output:[500, 331, 222, 221, 131, 100, 30, 29, 20]
print(any(st))
# output:True
print('sum of elements in set{} is {}'.format(st,sum(st)))
# output :sum of elements in set{131, 100, 331, 29, 500, 20, 30, 221, 222} is 1584
print('enumerated set st={}'.format(enumerate(st)))
# output:enumerated set st=<enumerate object at 0x0000028724B730B0>
print('enumerated set ={}'.format(set(enumerate(st))))
# output:enumerated set ={(6, 30), (2, 331), (8, 222), (3, 29), (0, 131), (4, 500), (5, 20), (7, 221), (1, 100)}
print({100,200} is st)
# output:False
print({100,200} is not st)
# output:True
print(st)
print(100 in st)
# output:{131, 100, 331, 29, 500, 20, 30, 221, 222}
#        True
print(100 not in st)
# output:False
st.pop()
print(st)
#output: {100, 331, 29, 500, 20, 30, 221, 222}
setnew =st.copy()
print(setnew)
# output:{100, 331, 222, 500, 20, 221, 29, 30}
st.clear() and setnew.clear()
print(st)
# output:set()
st.clear() or setnew.clear()
print(st,setnew)
# output: set() set()
st1={0,2,4,6,9,12,15}
st2={7,3,5,11,17,1,0,8,14,0}
print(st1.issuperset(st2))
# output:False
print(st1.isdisjoint(st2))
# output:False
print(st1.intersection(st2))
# output:{0}
print(st1.intersection_update(st2))
# output:None
print(st2.difference(st1))
# output:{1, 3, 5, 7, 8, 11, 14, 17}
print(st1.difference(st2))
# output:set()
print(st1.difference_update(st2))
# output:None
print(st1.issubset(st2))
# output:True
print(st1.union(st2))
# output:{0, 1, 3, 5, 7, 8, 11, 14, 17}
print(st1^st2)
# output:{0, 1, 3, 5, 7, 8, 11, 14, 17}
print(st1.symmetric_difference(st2))
# output:{0, 1, 3, 5, 7, 8, 11, 14, 17}
print(st1.symmetric_difference_update(st2))
# output:None
# convert list to set
li1=[1,2,3,4,5,6,99,99,100,10000,1000,5000,6000,7000,5000,6000,2000,100,2,3,4,5]
print(set(li1))
# output:{1, 2, 3, 4, 5, 6, 99, 100, 1000, 5000, 10000, 6000, 2000, 7000}
# convert tuple to set
tp=2,4,6,8,9,20,22,20,23
print(type(tp))
print(set(tp))
# output:
# <class 'tuple'>
# {2, 4, 6, 8, 9, 20, 22, 23}
dt={"name":"amit","nature":"Kind","age":"15","race":"indian"}
print(set(dt))
# output:{'nature', 'race', 'name', 'age'}
print(set(dt.values()))
# output:{'indian', 'amit', 'Kind', '15'}
