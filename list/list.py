li=['2','2.5','ab','cd','a+id']
# find the length of the list
print(len(li))
# output :5
li.append('6')
print(li)
# output:['2', '2.5', 'ab', 'cd', 'a+id', '6']
# print entire list 
print(li[:])
# output:['2', '2.5', 'ab', 'cd', 'a+id', '6']
# zero index to 2 index
print(li[0:2])
# output:['2', '2.5']
print(li[1:2])
# output:['2.5']
print(li[2:2])
# output:[]
print(li[3:2])
# output:[]
print(li[1:-1])
# output:['2.5', 'ab', 'cd', 'a+id']
print(li[2:-1])
# output :'ab', 'cd', 'a+id']
print(li[2:-2])
# output:['ab', 'cd']
print(li[2:-3])
# output :['ab']
print(li[2:-4])
# output:[]

# list concatination
li1=[2,3,4,5,5,6,6,7]
li2=[8,10,11,12,12,13,14,15,16,17,19]
print(li1+li2)
# output:[2, 3, 4, 5, 5, 6, 6, 7, 8, 10, 11, 12, 12, 13, 14, 15, 16, 17, 19]
# updating  specific index in list
li1[3]=3
print(li1)
# output:[2, 3, 4, 3, 5, 6, 6, 7]
# print the list mutiple times
print(li1*3)
# output :[2, 3, 4, 3, 5, 6, 6, 7, 2, 3, 4, 3, 5, 6, 6, 7, 2, 3, 4, 3, 5, 6, 6, 7]
li1=[2,3,4,5,5,6,6,7]
li2=[8,10,11,12,12,13,14,15,16,17,19]
li1.extend(li2)
print(li1)
# output:[2, 3, 4, 5, 5, 6, 6, 7, 8, 10, 11, 12, 12, 13, 14, 15, 16, 17, 19]
# pop()
print(li1.pop())
# output:19
print(li1.pop(5))
# output:6 it will pop the element in fiveth index
li1[0:7]='43'
print(li1)
# output :['4', '3', 8, 10, 11, 12, 12, 13, 14, 15, 16, 17]
li1.reverse()
print(li1)
# output:[17, 16, 15, 14, 13, 12, 12, 11, 10, 8, '3', '4']
print(li1)
print(li1.index(8))
# output :9 l11:17, 16, 15, 14, 13, 12, 12, 11, 10, 8, '3', '4']
li1.insert(10,2000)
print(li1)
# output:[17, 16, 15, 14, 13, 12, 12, 11, 10, 8, 2000, '3', '4']
li1.remove(2000)
print(li1)
# output:[17, 16, 15, 14, 13, 12, 12, 11, 10, 8, '3', '4']
print(li1.count(17))
# output:1
# convert tuple to list
tp=3,55,99
print(list(tp))
# output:[3, 55, 99]
# convert set to list
st={1,2,3,4,5,6}
print(list(st))
# output:[3, 55, 99]
# convert dictionary to list
dt={"name":"amit","nature":"Kind","age":"15","race":"indian"}
print(list(dt))
# output:['name', 'nature', 'age', 'race']
print(list(dt.values()))
# output:['amit', 'Kind', '15', 'indian']
# li1.sort()
print(li1)
# output:[2, 3, 4, 5, 5, 6, 7, 8, 10, 11, 12, 12, 13, 14, 15, 16, 17]
print(list(range(2,5)))
# output:[2, 3, 4]
print(list(range(10)))
# output:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0,10,3)))
# output:[0, 3, 6, 9]
print(list(range(1,10,3)))
# output:[1, 4, 7]
