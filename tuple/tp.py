tp=(2,3,5,6,78,9,9)
ty=9,8,9,5,5,1,54,9,2
print(tp+ty)
# output:(2, 3, 5, 6, 78, 9, 9, 8, 9, 5, 5, 1, 54, 9, 2)
print('tp[2]is {},ty[2] is{}'.format(tp[2],ty[2]))
# output :tp[2]is 5,ty[2] is 9
print(tp.index(78))
# output:4
print(tp.count(9))
# output:2
td=2,4,5,[6,7,9]
td[3][0]=10
print(td)
# output:(2, 4, 5, [10, 7, 9])
# convert list to tuple
li1=[2,4,5,67,7,7,778,8]
print(tuple(li1))
# output :(2, 4, 5, 67, 7, 7, 778, 8)
# covert set to tuple
si ={1,4,5,6,7,8,9}
print(tuple(si))
# output:(1, 4, 5, 6, 7, 8, 9)
dt={"name":"amit","nature":"Kind","age":"15","race":"indian"}
print(tuple(dt))
# output:('name', 'nature', 'age', 'race')
print(tuple(dt.values()))
# output:('amit', 'Kind', '15', 'indian')