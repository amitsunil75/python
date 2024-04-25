import os


def even_number(num):
    if num%2==0:
        print('its an even number')
    else:
        print('its not an even number')

def odd_number(num):
    if num%2!=0:
        print('its odd number')
    else:
        print('ita not an odd number')
def givenumbers():
    numbers=[]
    for i in range(2):
        n=int(input(f'enter number {i} :'))
        numbers.append(n)
    return numbers

def arthematic_operations(operation):
    total_sum=0
    total_sub=0
    total_mul=1
    to_do=input('enter add for addition ,minus to subtract and mul to multiply: ')
    for i in operation:
        total_sum +=int(i)
        total_sub -=int(i)
        total_mul*=int(i)

    case ={
      "add":f"sum is {total_sum}",
      "minus":f"diffrence is{total_sub}",
      "mul":f"multiplication is {total_mul}"
    }
    if case.get(to_do):
         print(case[to_do])
    else:
        print('invalid Choise taken')
        # os.system("shutdown /s /t 1") 

  