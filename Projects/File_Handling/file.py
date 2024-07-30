import pandas as pd

def add():
    cast_id = input("Enter the ID number: ")
    name = input("Enter the name: ")
    character_played = input("Enter the character played: ")
    salary = input("Enter the salary: ")

    with open("Projects/File_Handling/friends_cast_salaries.csv", "a") as f:
        f.write(cast_id + "\t" + name + "\t" + character_played + "\t" + salary + "\n")
        print("Record added.")
        
def display():
    with open("Projects/File_Handling/friends_cast_salaries.csv", "r") as f:
      

def search():
    cast_id = input("Enter the ID to be searched: ")
    found = False
    with open("Projects/File_Handling/friends_cast_salaries.csv", "r") as f:
        all_data = f.readlines()
        for data in all_data:
            d = data.split("\t")
            if d[0] == cast_id:
                print(data)
                found = True
                break
    if not found:
        print("Record not found.")

def delete():
    cast_id = input("Enter the ID to be removed: ")
    with open("Projects/File_Handling/friends_cast_salaries.csv", "r") as f:
        all_data = f.readlines()
    with open("Projects/File_Handling/friends_cast_salaries.csv", "w") as f:
        for data in all_data:
            d = data.split("\t")
            if d[0] != cast_id:
                f.write(data)
    print("Record deleted.")

def update():
    cast_id = input("Enter the ID to be updated: ")
    found = False
    with open("Projects/File_Handling/friends_cast_salaries.csv", "r") as f:
        all_data = f.readlines()
    with open("Projects/File_Handling/friends_cast_salaries.csv", "w") as f:
        for data in all_data:
            d = data.split("\t")
            if d[0] == cast_id:
                new_cast_id = input("Enter the new ID number: ")
                new_name = input("Enter the new name: ")
                new_character_played = input("Enter the new character played: ")
                new_salary = input("Enter the new salary: ")
                f.write(new_cast_id + "\t" + new_name + "\t" + new_character_played + "\t" + new_salary + "\n")
                found = True
            else:
                f.write(data)
    if found:
        print("Record updated.")
    else:
        print("Record not found.")

while (True):
    print("============ Friends Cast Salary Management ============")
    print("1. Add \n2. Delete \n3. Update \n4. Search \n5. Display \n6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add()
    elif choice == 2:
        delete()
    elif choice == 3:
        update()
    elif choice == 4:
        search()
    elif choice == 5:
        display()
    elif choice == 6:
        break
    else:
        print("Invalid choice, please enter a number between 1 and 6.")
