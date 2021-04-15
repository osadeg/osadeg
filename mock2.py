#Registring a User
# - first name, last name, password, email
# - generaten user account


#login
# - account number & password


#bank operations

#Initializing the system

import random

userdatabase = {} 
selectedOption = 1
balance = [235,950,44]
def init():

    print("*****Welcome to Bank Delux, where we valued our customers*****")

    haveAccount = int(input('Do you have an account with us? Press 1 for yes, or 2 for no \n'))
    
    if(haveAccount == 1):
        login()

    elif(haveAccount ==2):
        register()

    else:
        print('You have seleceted an invalid option')
        init()


#login 

def login():

    print("****** Please login with your details ******")
    isUserinDatabase = False
    while (isUserinDatabase == False):
        accountNumberFromUser = int(input("Enter your account number? \n"))
        password = input("Enter your password \n")

        for accountNumber,userDetails in userdatabase.items():
            if(accountNumber == accountNumberFromUser and userDetails[3] == password):
                isUserinDatabase = True
                print('***** Login successful*****')
                bankOperation(userDetails)
            else:
                print('invalid account or password, Try again')


    print('Invalid account or password')
    login()

#Register

def register():

    print("***** New User Registeration: *****")

    firstName = input("What is your first name? \n")
    lastName = input("What is your last name? \n")
    email = input("What is your email address? \n")
    password = input("create a password for yourself \n")

    accountNumber = generationAccountNumber()

#create database
    userdatabase[accountNumber] = [firstName, lastName, email, password]

    print("Your Account Has been succefully created")
    print(" ***** Login Details *****")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe \n")
    print(" ** ***** ***** **")

    login()

def bankOperation(user):

    print("Bank Operation %s %s " % ( user[0], user[1] ) )
    
    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit bank operation\n"))

    if(selectedOption == 1):

        depositOperation()
    elif(selectedOption == 2):

        withdrawalOperation()
    elif(selectedOption == 3):

        logout()
    elif(selectedOption == 4):

        exit()
    else:

        print("Invalid option selected")
        bankOperation(user)   
        
         
def withdrawalOperation():
    print('Withdraw option selected')
    withdraw_amount = int(input('How much would you like to withdraw?'))
    print('Please take your cash of %s' % withdraw_amount)

def depositOperation():
    #print("Deposit Operations")
    deposit_amount = int(input('How much would you like to to deposit?'))
    new_balance = str(deposit_amount)
    print('your cash of %s' % deposit_amount, 'has been deposited \n Your account balance is %s' % new_balance)


def generationAccountNumber():

    return random.randrange(1111111111,9999999999)

def logout():
    login()


init()