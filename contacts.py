# Name: Eli Thomas
# Date: 9/11/2024
# File Purpose: Add extra functionality for contact list (sorting)

contact_list_ = []

def print_list():
	"""lists contacts"""
	print("================== CONTACT LIST ==================")
	print("Index   First Name            Last Name")
	print("======  ====================  ====================")
	index = 0
	for contact in contact_list_:
		print("{:<7} {:<21} {:<22}".format(index, contact[0], contact[1]))
		index += 1

def add_contact(contact_list, first_name = "N/A", last_name = "N/A"):
	"""adds a contact to end of list"""
	contact_list.append([first_name,last_name])
	return contact_list

def modify_contact(contact_list, first_name = "N/A", last_name = "N/A", index = 0):
	"""modify a contact within a valid index range"""
	try:
		if index < 0 or index >= len(contact_list):		
			print("Invalid index number.")
			return False
		contact_list[index] = [first_name, last_name]
		return True
	except:
		print("Invalid input.")
	
def delete_contact(contact_list, index = 0):
	"""delete contact within valid index range"""
	try:
		if index < 0 or int(index) >= len(contact_list):
			print("Invalid index number.")
			return False
		contact_list.pop(index)
		return True
	except:
		print("Invalid input.")
		
def sort_contacts(contact_list, column=0):
	"""If column is 0, sort by first name, else, sort by last name"""
	if column == 0:
		contact_list.sort()
	elif column == 1:
		contact_list.sort(key=lambda contact_list: contact_list[1])
	
def print_menu():
	"""GUI for program"""
	print("\n     *** TUFFY TITAN CONTACT MAIN MENU ***     ")
	print("1. Print list")
	print("2. Add contact")
	print("3. Modify contact")
	print("4. Delete contact")
	print("5. Sort list by first name")
	print("6. Sort list by last name")
	print("7. Exit program\n")
	return
