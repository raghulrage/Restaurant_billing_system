from menu import *

import json

print('#'*10+' WELCOME '+'#'*10)

def getUserName(userDataFile):
        
    while True:
        username = input('\nEnter username: ')
    
        if username in userDataFile:
            print('Username Already Exists!!, Enter Again\n')
        else:
            return username

def signup():
    with open('Users/user.json') as json_file: 
        userDataFile = json.load(json_file)
        
    name = input('\nEnter Full Name: ')
    
    username = getUserName(userDataFile)

    phNo = input('\nEnter Mobile Number: ')

    password = input('\nEnter password: ')
    
    
    userData = {
                "Full Name" : name,
                "Phone Number" : phNo,  
                "Password" : password
                }
    
    f= open('Report/'+username+".txt","w+")

    

    userDataFile[username] = userData

    
    with open("Users/user.json", "w") as file:  
        json.dump(userDataFile, file,indent = 4)
        
    print('\n'+'*'*10+'Signup Successful'+'*'*10+'\n')

    mainFn(username)

def login():
    with open('Users/user.json') as json_file: 
        userDataFile = json.load(json_file)
        
    while True:
        username = input('\nEnter Username: ')
        
        if username in userDataFile:
            break
        if username.lower() == 'q':
            main()
        else:
            print("\nUser does not exist!!, Enter again or press 'Q' to home\n")
            
    while True:
        password = input('Enter password: ')
        
        if userDataFile[username]['Password'] == password:
            print('\n'+'*'*10+'Login Successful'+'*'*10+'\n')
            mainFn(username)
            exit()
        else:
            print('\nIncorrect password, Enter again\n')
        
    
def main():     
    while True:
        print('\n'+' '*5+'1. Login\n'+' '*5+'2. Signup\n'+' '*5+'3. Exit\n')
        opt = input('Select an option : ')
        if opt == '3':
            exit()
        elif opt == '1':
            login()
        elif opt == '2':
            signup()
        else:
            print('\nInvalid option, Enter again\n')
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Oops!',e.__class__,'error occured!!!')

