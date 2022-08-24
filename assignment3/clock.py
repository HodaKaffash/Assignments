while True:
    seconds=0
    hour=0
    minutes=0
    clock=0
    print("please choose which converter you want ")
    a=input("1.Hour to secounds      2.Secounds to hour:")
    if a=="1":
        hour_user=int(input("hour:"))
        if  0<= hour_user<= 24:
            minutes_user=int(input("minuts:"))
        else:
            print("please write a correct hours")
            continue
        if 0<= minutes_user<=60:   
            secounds_user=int(input("secounds:"))
        else:
            print("please write a correct hours")
            continue
        if 0<= secounds_user<=60:
        
            seconds = secounds_user
            hour = hour_user*3600
            minutes = minutes_user*60
            clock=seconds+hour+minutes
            print("The clock is " , clock,"secounds")
            break
        else:
            print("please write a correct secounds")
            continue
    elif a=="2":
        secounds_user=int(input("please enter secounds to convert to hours"))
        if 0<= secounds_user <= 86400:
            seconds = secounds_user % (24 * 3600)
            hour = seconds // 3600
            seconds %= 3600
            minutes = seconds // 60
            seconds %= 60 
            print("%d:%02d:%02d" % (hour, minutes, seconds))
            break
        else: 
            print("please enter correct secounds")
            continue
    else:
        print("please write correct number.")
        continue
         
            
      