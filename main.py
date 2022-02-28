from time import sleep
from tkinter import *

password = "password"
fw = open("passwords.txt", 'at')
fr = open("passwords.txt", 'rt')
i = 2


while i >= 0:
    authentication = input("Login Password Authentication: ")
    if authentication == password:
        while True:

            services = input('What service would you like to access: \n 1)New Login \n 2)View Logins  \n 3)Log Out \n Please enter the number: ') 


            if services == '1':
                new_website = input('Which website: ')
                new_username = input('Enter username/email: ')
                new_password = input('Enter password: ')
                new_entity = (str(new_website) + ', ' + str(new_username) + ', ' + str(new_password))

                with open ('passwords.txt', 'a') as fw:
                    fw.write('\n')
                    fw.write(str(new_entity))
                print('Password Sucessfully Saved!')
                sleep(1)
                
            
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
                fr.close()
                fw.close()
                print('Have a good day!')
                sleep(1)
                exit()
    

    else:
        print('Your password is incorrect')
        print('You have ' + str(i) + ' attempts left')
        i = i-1

