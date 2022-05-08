'''
Ong Jia Soon TP064392

This is my online pharmacy management system created for both admin and customers
'''
#function for people to register their account
def register(role):
    username=input('\n\nPlease enter your username:\n')
    password=input('\n\nPlease enter your password:\n')

    if role==1:
        file_to_open='AdminAccount.txt'
    elif role==2:
        file_to_open='CustomerAccount.txt'

    final_account_list=[]
    account_list=[]
    with open(file_to_open,'r') as file:
        file_content=file.readlines()
        

    for line in file_content:
        account_list=(line.replace('\n','')).split(':')
        final_account_list.append(account_list)

    for user in final_account_list:
        if user[0]==username:
            print('Your username is used')

    with open(file_to_open,'a') as file:
        file.write(f'\n{username}:{password}')


#function called to display different menus for different users
def menu(role_choice):

    #if the user is an admin
    if role_choice==1:
        print('1 - Login')
        print('2 - Register')
        function_choice=int(input('\nPlease enter your choice:\n'))
        if function_choice==2:
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
def login():

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

role_choice=login()
menu(role_choice)

