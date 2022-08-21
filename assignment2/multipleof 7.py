win = 0
lose = 0
draw = 0
score = 0
counter=0
while counter < 8:
    if 0 <= counter <= 3:
        if counter == 0:
            print("Enter the result of the First home match: " + "\n1.Win" + "\n2.Draw" + "\n3.Lose")
            matchresult = input('please select a number from above:')
            counter += 1
        
        elif counter == 1:
            print("\nEnter the result of the Second home match: " + "\n1.Win" + "\n2.Draw" + "\n3.Lose")
            matchresult = input('please select a number from above:')
            counter += 1
            
        elif counter == 2:
            print("\nEnter the result of the Third home match: " + "\n1.Win" + "\n2.Draw" + "\n3.Lose")
            matchresult = input("please select a number from above:")
            counter += 1
        
        elif counter == 3:
            print("\nEnter the result of the Fourth home match: " + "\n1.Win" + "\n2.Draw" + "\n3.Lose")
            matchresult = input('please select a number from above:')
            counter += 1

        if matchresult == '1':
            win += 1
            score += 3
            continue
        
        elif  matchresult == '2':
            draw += 1
            score += 1
            continue
        
        elif  matchresult == '3' :
            lose += 1
            continue
        
        else:
            counter -= 1
            print("\nInvalid option!!\nPlease ReEnter You're option please: ")
            continue
        
    elif 4 <= counter <= 7:
        if counter == 4:
            print("\nEnter the result of the First Away match:" + "\n1.Win" + "\n2.Draw" + "\n3.Lose")
            matchresult = input("please select a number from above:")
            counter += 1
            
        elif counter == 5:
            print("\nEnter the result of the Second Away match:" + "\n1.Win" + "\n2.Draw" + "\n3.Lose")
            matchresult = input("please select a number from above:")
            counter += 1
            
        elif counter == 6:
            print("\nEnter the result of the Third Away match: " + "\n1.Win" + "\n2.Draw" + "\n3.Lose")
            matchresult = input('please select a number from above:')
            counter += 1
            
        elif counter == 7:
            print("\nEnter the result of the Fourth Away match: " + "\n1.Win" + "\n2.Draw" + "\n3.Lose")
            matchresult = input("please select a number from above:")
            counter += 1

        if  matchresult == '1':
            win += 1
            score += 3
            continue
        
        elif  matchresult == '2':
            draw += 1
            score += 1
            continue
        
        elif matchresult == '3' :
            lose += 1
            continue
        
        else:
            counter -= 1
            print("\nInvalid option!!\nPlease ReEnter You're option please: ")
            continue

print("\n the result of the rezavan football team:")
print(' wins :' ,win)
print(' losses :',lose)
print("draws :" ,draw )
print("scores :"  ,score)