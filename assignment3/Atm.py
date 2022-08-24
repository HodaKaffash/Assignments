pin= 1234
i=0
while i<3:
   
    pin_user= int(input("Please enter your pin:"))
    if 1000<=pin_user<=9999:
        if pin== pin_user:
            print("access verified")
            break
        elif pin_user ==4321:
            print("You are suspected by police and your account is blocked by now")
            break
        else:
            print("Wrong pin.")
            i=i+1
    else:
        continue
if i>2:
    print("Too many attempts,There is a temporary card block for a day.")