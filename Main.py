'''
Ong Jia Soon TP064392

This is my online pharmacy management system created for both admin and customers
'''
#receives a list,a target and the supposed index number of the target
def search_from_list(list,target,position):

    #iterate through the entire list
    count=-1
    for item in list:
        count+=1

        #if the target is in the list,returns True and the index number of the list containing the target 
        if item[position]==target:
            return (True,count)
        
    #if every the target is not in the list
    return (False,0)
    


#function for reading from a file
def readfile(filename):

    final_list=[]

    
    try:
        #opens the file and use readlines to return them as a list
        with open(filename,'r') as file:
            file_content=file.readlines()

        #if the file had not been created
    except FileNotFoundError:
        return None
        
    #for every line in the file,remove the newlines and split them with : as the seperator and make them into a list and then append the list
    final_list=[(user.replace('\n','')).split(':') for user in file_content]

    return final_list


#function for people to register their account
def register(role):
    username=input('\n\nPlease enter your username:\n')
    password=input('\n\nPlease enter your password:\n')

    #decides the file_name according to the users name
    if role==1:
        file_name='AdminAccount.txt'
    elif role==2:
        file_name='CustomerAccount.txt'

    #gets a list of list containing every users name and password
    account_list=readfile(file_name)

    #if the file has not been created,just write the new users info into the newly created file
    if account_list==None:
        with open(file_name,'w') as file:
            file.write(f'{username}:{password}')    

    #if there are already existing users,check if there is any matching username and tell the user to enter a new name if required
    else:
        username_check=True
        while username_check:
            username_search_result=search_from_list(account_list,username,0)[0]
            if username_search_result==True:
                print('Your username is used')
                username=input('\nPlease enter a new username:\n')
            username_check=username_search_result


        #write the new info if there is no matching username
        with open(file_name,'a') as file:
            file.write(f'\n{username}:{password}')

#function for people to login
def login(role):

    #decides the filename according to role
    if role==1:
        file_name='AdminAccount.txt'
    elif role==2:
        file_name='CustomerAccount.txt'
    print('Please enter your username and password')
    username=input('\nPlease enter your username:\n')

    account_list=readfile(file_name)

    if account_list==None:
        print('Quit messing around')
    else:
        account_exist_check=True

        #while loop to check if account already exists
        while account_exist_check:
            account_exist_result=search_from_list(account_list,username,0)

            if account_exist_result[0]==False:
                print('Invalid Username')
                username=input('Please enter a valid username:\n')

            account_exist_check=not(account_exist_result[0])

        #if the user already exists, check if the password is correct        
        password=input('Please enter your password:\n')
        password_check=True
        while password_check:
            if account_list[account_exist_result[1]][1]==password:
                password_check=False
                pass
            else:
                password=input('Please enter the correct password:\n')
        
                

#function called to display different menus for different users
def menu(role_choice):

    #if the user is an admin
    if role_choice==1:
        print('1 - Login')
        print('2 - Register')
        function_choice=int(input('\nPlease enter your choice:\n'))
        if function_choice==1:
            login(1)
        elif function_choice==2:
            register(1)

    #if the user is a new customer
    elif role_choice==2:
        print('1 - View Medicine Detail')
        print('2 - Register')
        function_choice=int(input('\nPlease enter your choice:\n'))
        if function_choice==2:
            register(2)

    #if the user is a registered customer
    elif role_choice==3:
        print('1 - Login')
        function_choice=int(input('\nPlease enter your choice:\n'))

#function which should be called when users start the program for them to login into their own respective accounts
def start_menu():

    #condition for the while loop to keep executing the the statement below
    select_menu=True

    #while loop for users to choose their role
    while(select_menu):
        print('Welcome to OCEAN Sdn Bhd!')
        input()
        print('Roles available for you')
        print('\n1 - Admin')
        print('2 - New User')
        print('3 - Registered User')
        role_choice=input('\n Please enter your choice:\n')
        print(type(role_choice))
        print('\n'+role_choice+'\n')
        if not(role_choice=='1' or role_choice=='2' or role_choice=='3'):
            print('\nPlease input a correct number')
        else:
            select_menu=False
    
    #returns back the choices of the users
    return int(role_choice)

role_choice=start_menu()
menu(role_choice)

