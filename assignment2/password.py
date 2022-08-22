count=0
while count <= 3:
    psw=2000
    username = input(' please enter username: ')
    password = int(input('please enter password: '))
    if password==psw and username=='hodakf':
        print('Access granted')
        break
    else:
        print('Access denied.  please Try again.')
        count += 1
if count >3: 
    print ('too many login attempts, please try again later')
