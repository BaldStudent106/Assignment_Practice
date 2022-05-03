'''
Ong Jia Soon TP064392

This is my online pharmacy management system created for both admin and customers
'''

#function called to display different menus for different users
def menu(role_choice):

    #if the user is an admin
    if role_choice==1:
        print('1 - Login')
        print('2 - Register')

    #if the user is a new customer
    elif role_choice==2:
        print('1 - View Medicine Detail')
        print('2 - Register')

    #if the user is a registered customer
    elif role_choice==3:
        print('1 - Login')

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