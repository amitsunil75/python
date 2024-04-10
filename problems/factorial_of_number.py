
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(fact)


num = int(input('Enter a number: '))
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print(fact)

# output:
# Enter a number: 5
# 120