# Name: Eli Thomas
# Date: 9/11/2024
# File Purpose: Add extra functionality for contact list (sorting)

contact_list_ = []

def print_list():
	print("================== CONTACT LIST ==================")
	print("Index   First Name            Last Name")
	print("======  ====================  ====================")
	index = 0
	for contact in contact_list_:
		print("{:<7} {:<21} {:<22}".format(index, contact[0], contact[1]))
		index += 1

def add_contact(contact_list):
	first = input("Enter first name: ")
	last = input("Enter last name: ")
	contact_list.append([first,last])
	return contact_list

def modify_contact(contact_list):
	try:
		index = int(input("Enter index to modify: "))
		if index < 0 or index >= len(contact_list):		
			print("Invalid index number.")
			return False
		first = input("Enter first name: ")
		last = input("Enter last name: ")
		contact_list[index] = [first,last]
		return True
	except:
		print("Invalid input.")
	
def delete_contact(contact_list):
	try:
		index = int(input("Enter index to modify: "))
		if index < 0 or int(index) >= len(contact_list):
			print("Invalid index number.")
			return False
		contact_list.pop(index)
		return True
	except:
		print("Invalid input.")
	
def print_menu():
	print("\n     *** TUFFY TITAN CONTACT MAIN MENU ***     ")
	print("1. Print list")
	print("2. Add contact")
	print("3. Modify contact")
	print("4. Delete contact")
	print("5. Exit program\n")
	return
