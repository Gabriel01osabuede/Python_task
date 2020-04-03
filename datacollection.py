import random

# creating a password validation function to check the length of the password inputted.
def PASSWORD(LENGHT=7):
    # password variable
    password = input("Enter your password : ")
    # using the len keyword to check the length of the password
    count = len(password)
    # using conditions to validate the length
    if count >= LENGHT:
        print("password succesful")
        print("YOUR SELECTED PASSWORD IS : " + password + '\n')
    elif count < LENGHT:
        print("Wrong password Try again \n")
        PASSWORD()
    else:
        print("invalid activation.")

# creating an empty list call data
data = []

# creating a
def Form(size=5):

    # using a while loop to make sure the loops goes on till its terminated by the user.
    while True:

        print("\nWelcome To HNG-Tech world")
        print("We would require some few personal data from you please.")
        print("Kindly fill the form below.")
        print("Thanks.")

        line = 50 * "="
        print(line)

        print(".REGISTRATION FORM.")
        FirstName = str(input("Firstname :    ")).upper()
        LastName = str(input("Lastname :  ")).upper()
        Email = str(input("Email :   "))

        F = FirstName[0:2]
        L = LastName[-2:]
        Alphabets = 'abcdefghijklmnopqrstuvwxyz0123456789'
        game = "" .join(random.choice(Alphabets.upper())for x in range(size))
        password = F + game + L
        print("YOUR PASSWORD IS :  " + password + '\n')


        print("Are you satisfied with your login password\n(Y/N)")

        select = input("ENTER SELECTION :  ").upper()

        if select == 'Y':
            print('Registration successful\nWelcome to HNG-TECH {}'.format(FirstName + ' ' + LastName))
        elif select == 'N':
            print("TYPE IN THE PASSWORD OF YOUR CHOICE\nAND IT MUST BE MORE THAN 7 CHARACTERS.")
            PASSWORD()
        else:
            print("INVALID SELECTION\nTRY AGAIN.")

        saved = ('NAME : {} \n'
                'Email : {} \n'
                 'Password : {} \n'
                 '\n'.format(FirstName + ' ' +LastName,Email,password))

        # appending to the data variable
        container = data.append(saved)


        select = input("ARE YOU DONE INPUTTING ALL RECORDS.(Y/N)\nENTER : ").upper()
        if select == 'Y':
            print("DATA SAVED\n")
            for x in data:
                print(x)
        elif select == 'N':
            Form()
        else:
            print("INVALID INPUT SELECTED = {} ".format(select))
        break


Form()