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
