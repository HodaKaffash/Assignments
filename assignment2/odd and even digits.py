number = int(input("please enter a number : "))
odd = 0
even = 0
while number != 0:
    mod = number % 10
    if mod % 2 == 0:
        even += 1
    else:
        odd += 1
    number = number // 10
print('The number of even digits  is :', even )
print('The number of odd digits is:',odd)
if odd == even:
    print("The number of the odd and even digits are equal")
elif odd > even:
    print('The number of odd digits is  more than even digits.')
else:
    print('The number of even digits ismore than odd digits.')