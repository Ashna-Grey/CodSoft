import os
import time
file_name="contacts.txt"

#Adding Contact details
def add():
    name=input("Enter name: ")
    phone=input("Enter phone number: ")  # CHANGED from int() to input()
    email=input("Enter email: ")
    address=input("Enter address (without '|'): ")
    with open(file_name,"a") as f:
        f.write(f"{name}|{phone}|{email}|{address}\n")
    print("Contact added.\n")
    time.sleep(2)

#All contact details
def view():
    if not os.path.exists(file_name):
        print("No contacts found.\n")
        return
    with open(file_name,"r") as f:
        lines=f.readlines()
        if not lines:
            print("No contacts found.\n")
            return
        print("\nContact List:")
        for i in lines:
            if "|" not in i:
                continue
            name,phone,email,address=i.strip().split("|")
            print(f"Name: {name}, Phone: {phone}, Email: {email}, Address: {address}")
        print()
    time.sleep(2)

#Search by name
def search():
    s_name,found=input("Enter name to search for : "),0
    if not os.path.exists(file_name):
        print("No contacts found.\n")
        return
    with open(file_name,"r") as f:
        for i in f:
            if "|" not in i:
                continue
            name,phone,email,address=i.strip().split("|")
            if (s_name.lower() in name.lower()):
                print(f"Name: {name}\n Phone: {phone}\n Email: {email}\n Address: {address}\n")
                found=1
    if not found:
        print("Contact not found.\n")
    time.sleep(2)

#Search and update
def update():
    nam,updated=input("Enter name of contact to update: "),0
    if not os.path.exists(file_name):
        print("No contacts found.\n")
        return
    with open(file_name, "r") as f:
        lines=f.readlines()
    with open(file_name, "w") as f:
        for i in lines:
            if "|" not in i:
                f.write(i)
                continue
            name, phone, email, address = i.strip().split("|")
            if (nam.lower()==name.lower()):
                print("Enter new details (leave blank to keep unchanged):")
                new_name=input(f"New name [{name}]: ") or name
                new_phone=input(f"New phone [{phone}]: ") or phone
                new_email=input(f"New email [{email}]: ") or email
                new_address=input(f"New address [{address}]: ") or address
                f.write(f"{new_name}|{new_phone}|{new_email}|{new_address}\n")
                updated=1
                print("Contact updated.\n")
            else:
                f.write(i)
    if not updated:
        print("Contact not found.\n")
    time.sleep(2)

#Delete contact
def delete():
    nam=input("Enter name of contact to delete: ")
    deleted=0
    if not os.path.exists(file_name):
        print("No contacts found.\n")
        return
    with open(file_name,"r") as f:
        lines=f.readlines()
    with open(file_name,"w") as f:
        for i in lines:
            if "|" not in i:
                f.write(i)
                continue
            name, phone, email, address = i.strip().split("|")
            if nam.lower() == name.lower():
                deleted=1
                print("Contact deleted successfully.\n")
            else:
                f.write(i)
    if not deleted:
        print("Contact not found.\n")
    time.sleep(2)
    
while True:
    print("\n\tContact Book\t\n1. Add Contact\n2. View Contact List\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit\n")
    choice = input("Choose an option (1-6): ")
    if choice == "1":
        add()
    elif choice == "2":
        view()
    elif choice == "3":
        search()
    elif choice == "4":
        update()
    elif choice == "5":
        delete()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid input.\n")
        time.sleep(2)
