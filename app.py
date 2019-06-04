# app that stores contacts
import os
import time

contacts = {}
user_name = input("Type your name:  ")


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def create_contact():
    new_contact_name = input('Enter the contact\'s name:  ').lower()
    new_contact_number = input('Enter the contact\'s number:  ')
    contacts[new_contact_name] = new_contact_number


def view_contact():
    contact_name = input('What\'s the name of the contact you wish to view:  ').lower()
    if contact_name in contacts:
        name = contact_name
        number = contacts.get(name)
        print(f'name: {name}, number: {number}')
    else:
        print('I couldn\'t find that contact')    


def update_contact():
    contact_name = input('What\'s the name of the contact you wish to update:  ').lower()
    if contact_name in contacts:
        name_or_number = input('What would you like to update? (Name/Number)  ').lower()
        if name_or_number == 'name':
            new_contact_name = input('Please enter a new name for your contact  ')
            contacts[new_contact_name] = contacts.pop(contact_name)
        if name_or_number == 'number':
            new_contact_number = input('Please enter a new number for your contact  ')
            contacts[contact_name] = new_contact_number   
    else:
        print('I couldn\'t find that contact')      


def delete_contact():
    contact_name = input('What\'s the name of the contact you wish to delete:  ').lower()
    if contact_name in contacts:
        contacts.pop(contact_name)
    else:
        print('I couldn\'t find that contact')    


def help_menu():
    cls()
    menu_decision = input('MENU: CREATE, VIEW, UPDATE, DELETE (PICK ONE):  ').lower()
    return menu_decision


cls()
print(f'Greetings {user_name}!')
while True:
    help_or_quit = input('Type HELP for help, and QUIT to quit:  ').lower()
    if help_or_quit == 'help':
        choice = help_menu()
        if choice == 'create':
            create_contact()
        elif choice == 'view':
            view_contact()
        elif choice == 'update':
            update_contact()
        elif choice == 'delete':
            delete_contact()   
        else:
            print('That\'s not a valid menu choice')    
    elif help_or_quit == 'quit':
        print('Goodbye')
        break 
    else:
        cls()
        print('INVALID COMMAND! *Type HELP or QUIT*')   
    

