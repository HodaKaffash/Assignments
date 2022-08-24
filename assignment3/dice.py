import random
min_=1
max_=6
i=0
sum=0
while True:
     d = random.randint(min_, max_)
     i=i+1
     sum=sum+d
     print("In round",i,"the face that has appeared is:",d)
     if d == 6:
          print("in this round 6 appeared so the total faces till now is:",sum)
          break