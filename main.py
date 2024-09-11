# Name: Eli Thomas
# Date: 9/11/2024
# File Purpose: Main driver for contact menu

from contacts import *

exit_program = False

while exit_program == False:

	print_menu()

	choice = input("Enter menu choice: ")
	print("")
	
	if choice == '1':
		print_list()
		
	elif choice == '2':
		first = input("Enter first name: ")
		last = input("Enter last name: ")
		add_contact(contact_list_, first, last)
		
	elif choice == '3':
		if len(contact_list_) == 0:
			print("List is empty!")
			continue
		index = int(input("Enter index to modify: "))
		first = input("Enter first name: ")
		last = input("Enter last name: ")
		modify_contact(contact_list_, first, last, index)
		
	elif choice == '4':
		index = int(input("Enter index to modify: "))
		delete_contact(contact_list_, index)
		
	elif choice == '5':
		sort_contacts(contact_list_, 0)
		
	elif choice == '6':
		sort_contacts(contact_list_, 1)
		
	elif choice == '7':
		exit_program = True
	
	else:
		print("Invalid input.")
