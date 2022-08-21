number = int(input("please enter a number: "))
reverse = 0
num = number
while num != 0:
    reverse =  (num % 10)+(10 * reverse) 
    num = num // 10
print('The inverse of the number is = ' , reverse)
if number == reverse:
    print('The actual number and reverse of that are the same')
else:
    print("The number is not equal to reverse of that")