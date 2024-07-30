import pandas as pd

# File path to the CSV file
file_path = r"Projects/File_Handling/friends_cast_salaries.csv"

def add():
    cast_id = input("Enter the ID number: ")
    name = input("Enter the name: ")
    character_played = input("Enter the character played: ")
    salary = input("Enter the salary (per episode): ")

    # Create a DataFrame with the new record
    new_record = pd.DataFrame({
        "Id": [cast_id],
        "Name": [name],
        "Character Played": [character_played],
        "Salary (per episode)": [salary]
    })

    # Append the new record to the CSV file
    new_record.to_csv(file_path, mode='a', header=False, index=False)
    print("Record added.")
        
def display():
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        if df.empty:
            print("No records found.")
        else:
            print(df.to_string(index=False))
    except FileNotFoundError:
        print("No records found.")
    except pd.errors.EmptyDataError:
        print("No records found.")

def search():
    cast_id = input("Enter the ID to be searched: ").strip()
    try:
        df = pd.read_csv(file_path)
        # Convert 'Id' to string to ensure consistent comparison
        df['Id'] = df['Id'].astype(str)
        result = df[df['Id'] == cast_id]
        if not result.empty:
            print(result.to_string(index=False))
        else:
            print("Record not found.")
    except FileNotFoundError:
        print("No records found.")
    except pd.errors.EmptyDataError:
        print("No records found.")

def delete():
    cast_id = input("Enter the ID to be removed: ").strip()
    try:
        df = pd.read_csv(file_path)
        df['Id'] = df['Id'].astype(str)
        updated_df = df[df['Id'] != cast_id]
        if len(updated_df) < len(df):
            updated_df.to_csv(file_path, index=False)
            print("Record deleted.")
        else:
            print("Record not found.")
    except FileNotFoundError:
        print("No records found.")
    except pd.errors.EmptyDataError:
        print("No records found.")

def update():
    cast_id = input("Enter the ID to be updated: ").strip()
    try:
        df = pd.read_csv(file_path)
        df['Id'] = df['Id'].astype(str)
        if cast_id in df['Id'].values:
            new_cast_id = input("Enter the new ID number: ").strip()
            new_name = input("Enter the new name: ").strip()
            new_character_played = input("Enter the new character played: ").strip()
            new_salary = input("Enter the new salary (per episode): ").strip()

            df.loc[df['Id'] == cast_id, ['Id', 'Name', 'Character Played', 'Salary (per episode)']] = [new_cast_id, new_name, new_character_played, new_salary]
            df.to_csv(file_path, index=False)
            print("Record updated.")
        else:
            print("Record not found.")
    except FileNotFoundError:
        print("No records found.")
    except pd.errors.EmptyDataError:
        print("No records found.")

while True:
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
