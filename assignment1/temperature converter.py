print(""" select one of the Temperature conversions in below:
1.Celsius to Fahrenheit
2.Celsius to Kelvin
3.Fahrenheit to Celsius
4.Fahrenheit to Kelvin
5.Kelvin to Celsius
6.Kelvin to Fahrenheit""")
conversions=input('please write your choice:')
if conversions == "1":
    temperature = float(input("Enter the temperature in Celsius: "))
    result = (temperature * 1.8) + 32
    print('the conversion of your temperature is:' ,result)
elif conversions == "2":
    temperature = float(input("Enter the temperature in Celsius: "))
    result = temperature + 273.15
    print('the conversion of your temperature is:' ,result)
elif conversions == "3":
    temperature = float(input("Enter the temperature in Fahrenheit: "))
    result = (temperature - 32) * 5 / 9
    print('the conversion of your temperature is:' ,result)
elif conversions == "4":
    temperature = float(input("Enter the temperature in Fahrenheit: "))
    result = ((temperature - 32) * 5 / 9) + 273.15
    print('the conversion of your temperature is:' ,result)
elif conversions == "5":
    temperature = float(input("Enter the temperature in Kelvin: "))
    result = temperature - 273.15
    print('the conversion of your temperature is:' ,result)
elif conversions == "6":
    temperature = float(input("Enter the temperature in Kelvin: "))
    result = ((temperature - 273.15) * 1.8) + 32
    print('the conversion of your temperature is:' ,result)
else:
    print('invalid number, please try again')
