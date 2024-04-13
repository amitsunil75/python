number = int(input('enter a number: '))

if number==0 or number==1:
    print('prime nor comaposite')           
else :
 isprime=True
 for i in range(2,number):
    if number%i==0:
        isprime=False
        break

 if isprime:
    print('its prime')
 else:print('not prime')

startIndex = int(input('enter start index:'))
endIndex = int(input('enter end index:'))
non_prime_numbers = []
prime_numbers = []

for j in range(max(2,startIndex), endIndex):
    isPrime = True  # Reset isPrime for each value of j
    for y in range(2, j):  # Use j instead of i
        if j % y == 0:
            isPrime = False
            break  # No need to continue checking if j is not prime

    if isPrime:
        prime_numbers.append(j)

print(f'list of prime:{prime_numbers}')

for j in range(max(2,startIndex), endIndex):
    isPrime = True  # Reset isPrime for each value of j
    for y in range(2, j):  # Use j instead of i
        if j % y == 0:
            isPrime = False
            continue  # No need to continue checking if j is not prime

    if isPrime:
        pass
    else:
        non_prime_numbers.append(j)

print(f'list of Non prime:{non_prime_numbers}')
