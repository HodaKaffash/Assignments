import random
b = 99
a = 0
i=0
number=0
print("Please select a number between 0 to 99.")
guess = random.randint(a,b)
while number != 1:
    print("our gussing is    ",guess,"    please choose 1.correct gussing  2.go higher  3.go lower ")
    number=int(input())
    i=i+1
    if number == 2:
        a = guess
    elif number == 3:
        b = guess
    guess = random.randint(a, b)
print("our gussing is correct and this operation was repeated ",i,"times")