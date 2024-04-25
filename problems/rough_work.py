a={"max":"20","jomoon":"24"}
c=int(a.get("max"))+3
a['max']=c
print(a["max"])
no=[]
for i in range(1,31):
    if(i%3==0 and i%5==0 ):
        no.append(i)
s=sum(no)
print(no)
print(s)

age = int(input('enter your age:'))
if(age<18):
    print('you wont be able to vote')
else:
    print('you can vote')
r=0
hobby=[]
while r<3:
    hobbies = input(f'enter your Hobby{r}')
    hobby.append(hobbies)
    r+=1

print(hobby,sep=',')