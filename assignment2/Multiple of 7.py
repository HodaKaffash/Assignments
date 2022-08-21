number = int(input("Enter a number: "))
if number % 7 ==0:
    print("It's a multiple of 7.")
else:
    while number % 7 != 0:
        number +=1
    print(' the next multiple of 7 is = ' , number)