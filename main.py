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
		add_contact(contact_list_)
		
	elif choice == '3':
		if len(contact_list_) == 0:
			print("List is empty!")
			continue
		modify_contact(contact_list_)
		
	elif choice == '4':
		delete_contact(contact_list_)
		
	elif choice == '5':
		exit_program = True
	
	else:
		print("Invalid input.")
