import re
from time import sleep
from tkinter import *
import string
import random

password = "password"

fw = open("passwords.txt", 'at')
fr = open("passwords.txt", 'rt')
i = 2
letters = string.ascii_letters
numbers = string.digits
punctuation = string.punctuation


while i >= 0:
    authentication = input("Login Password Authentication: ")
    if authentication == password:
        while True:

            services = input('What service would you like to access: \n 1)New Login \n 2)View Logins  \n 3) Change Login Information \n 4)Log Out  \n Please enter the number: ') 


            if services == '1':
                generate_password = input('Would you like to generate a password? (Y/N) ')
                new_website = input('Which website: ')
                new_username = input('Enter username/email: ')
                
                if generate_password == 'Y':
                    new_password = (''.join(random.choice(letters+numbers+punctuation) for i in range (15)))
                    print('Your new password is: ' + new_password)

                else:                   
                    new_password = input('Enter password: ')


                new_entity = (str(new_website) + ', ' + str(new_username) + ', ' + str(new_password))

                with open ('passwords.txt', 'a') as fw:
                    fw.write('\n')
                    fw.write(str(new_entity))
                print('Password Sucessfully Saved!')
                sleep(1)
                
            #add passwords that are available
            if services == '2':
                search_query = input('What password are you looking for? ')
                myline = fr.readline()
                while myline:
                    myline = fr.readline()
                    if search_query in myline:
                        mylinelist = myline.split(', ')
                        requested_username = mylinelist[1]
                        requested_password = mylinelist[2]
                        print('Username: ' + requested_username + '\nPassword: ' + requested_password)
                        sleep(1)
            

            if services == '3':
                search_query = input('What password would you like to change (enter website): ')
                myline = fr.readline()
                while myline:
                    myline = fr.readline()
                    if search_query in myline:
                        mylinelist = myline.split(', ')
                        requested_username = mylinelist[1]
                        requested_password = mylinelist[2]
                        print('This is your current password: ' + requested_password)
                        change_password = input('Please enter your new password: ')
                        replaced_line = myline.replace(str(requested_password), str(change_password))
                        print('Your new login information is: ' + '\n Username: ' + requested_username + '\n Password: ' + change_password)
                        with open ('passwords.txt', 'a') as fw:
                            #replacing the line does not work
                            fw.write(myline.replace(str(myline), str(replaced_line)))
                            print('Your new password has been saved!')
                            sleep(1)
                            break

            

            if services == '4':
                fr.close()
                fw.close()
                print('Have a good day!')
                sleep(1)
                exit()
    

    else:
        print('Your password is incorrect')
        print('You have ' + str(i) + ' attempts left')
        i = i-1

