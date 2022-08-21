h=float(input("Enter your height in meters: "))
w=float(input("Enter your Weight in Kg: "))
BMI=w/(h**2)
print("BMI Calculated is:  ",BMI)
if(BMI>0):
    if(BMI<=16):
        print("You are very underweight,you may need to put on some weight. You are recommended to ask your doctor or a dietitian for advice.")
    elif(BMI<=18.5):
        print("You are underweight,You are recommended to ask your doctor or a dietitian for advice")
    elif(BMI<=25):
        print("you are at a healthy weight for your height. By maintaining a healthy weight, you lower your risk of developing serious health problems.")
    elif(BMI<=30):
        print("you are slightly overweight. You may be advised to lose some weight for health reasons. You are recommended to talk to your doctor or a dietitian for advice.")
    else: 
        print("you are heavily overweight. Your health may be at risk if you do not lose weight. You are recommended to talk to your doctor or a dietitian for advice.")
else:
    print(" please enter valid details")