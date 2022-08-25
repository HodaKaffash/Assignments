import math
i=0
user_counter=int(input("How many times do you want to use this calculator?"))
while i< user_counter:   
   operation = input('''
   Please type in the math operation you would like to complete:
   + for addition
   - for subtraction
   * for multiplication
   / for  float division
   // for intiger division
   % for Modulus
   ** for Exponentiation
   sqr for radical
   fact for factorial
   sin , cos , tan  ,cot
   ''' )
   i=i+1
   print ("Round",i)
   if operation=="+" or operation=="-" or operation=="*" or operation=="/" or operation=="//"or operation=="//" or operation=="%" or operation=="**":
      number_1 = int(input('Enter your first number: '))
      number_2 = int(input('Enter your second number: '))
      if operation == '+':
         print('{} + {} = '.format(number_1, number_2))
         print(number_1 + number_2)

      elif operation == '-':
         print('{} - {} = '.format(number_1, number_2))
         print(number_1 - number_2)
         
      elif operation == '*':
         print('{} * {} = '.format(number_1, number_2))
         print(number_1 * number_2)
       
      elif operation == '/':
         if(number_2==0):
            print('can not divide by zero.')
            
         else:
            divi=number_1/number_2
            print('{} / {} = '.format(number_1, number_2))
            print(number_1 / number_2)    
      
      elif operation == '//':
         if(number_2==0):
            print('can not divide by zero.')
         else:
            divi=number_1  // number_2
            print('{} // {} = '.format(number_1, number_2))
            print(number_1 // number_2) 
            
      elif operation == '%':
         print('{} % {} = '.format(number_1, number_2))
         print(number_1 % number_2) 
        
      else:
         print('{} ** {} = '.format(number_1, number_2))
         print(number_1 ** number_2)
         i=i+1   
   
   elif operation=="sqr"or operation== "fact" or operation=="sin"or operation=="cos" or operation=="tan" or operation=="cot":
      number_1 = int(input('Enter your number: ')) 
      if operation == 'sqr':
         radical = math.sqrt(number_1)
         print('radical of number:',radical)
         
      elif operation=="fact":
         fact=math.factorial(number_1)
         print('factorial of number:',fact)         
       
      elif operation=="sin":
         sin=math.sin(number_1)
         print('sin of number:',sin)
                  
      elif operation=="cos":
         cos=math.cos(number_1)
         print('cos of number:',cos)
         
      elif operation=="tan":
         tan=math.tan(number_1)
         print('tan of number:',tan)
       
      else:
         cot=math.cot(number_1)
         print('cot of number:',sin) 
         i=i+1  
   else:
      print('You have not typed a valid operator.')
