students = {}
student_id = 1

 
def add_student():
    global student_id
    name = input("👤Enter student name:").strip()
    for student in students.values():
        if student['name'].casefold() == name.casefold():
            print(f"{name} already exists in the list")
            return
    else:
        students[student_id] = {
           "name": name 
        }
        save_students_to_file()
        student_id+=1
        print("Student added successfully.")
        return
    
 
def view_student():
    if not students:
            print("List is empty.") 
            return
    else:
        print("Students List:")
        for sid, student_name in students.items():
            print(f"{sid}.{student_name['name']}")


def search_student():
    search_name = input("👤Enter the name to search:").strip()
    for student in students.values():
       if student['name'].casefold() == search_name.casefold():
            print(f"Student {student['name']} found in records.")
            return
    else:
            print(f"Student {search_name} not found in records.")
            return


def delete_student():
    delete_name = input("Enter the name to delete:").strip()
    for sid, student_name in list(students.items()):
        if student_name['name'].casefold() == delete_name.casefold():
            del students[sid]
            print(f"Student {student_name['name']} has been deleted from the list.")
            return
    else:
        print(f"Student {delete_name} is not in the list.")
        return


def update_student():
    old_name = input("Enter the name to update:").strip()
    for sid, student_name in list(students.items()):
        if student_name['name'].casefold() == old_name.casefold():
            new_name = input("Enter the new name:").strip()
            students[sid]['name'] = new_name
            print(f"Student updated: {old_name} → {new_name}")
            return
    else:
        print(f"{old_name} does not exist in the list.")
        return
        
        
def save_students_to_file():
    with open("students.txt", "w") as f:
        for sid , data in students.items():
            f.write(f"{sid},{data['name']}\n")
      
            
def load_students_from_file():
    global student_id
    students.clear()
    try:
        with open("students.txt", "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if "," not in line:
                    continue
                sid, name = line.split(",", 1)
                sid = int(sid)
                students[sid] = {"name": name}
        if students:
            student_id = max(students.keys()) + 1
    except FileNotFoundError:
        print("File not found.")


def search_by_id():
    try:
         search_id = int(input("Enter student ID: "))
    except ValueError:
        print("Invalid ID. Please enter a valid integer.")
        return
    if search_id in students:
        print(f"{search_id} → {students[search_id]['name']}")
    else:
        print("ID Not Found")
      
        
load_students_from_file()


while True:

    print("\n====  STUDENT MANAGEMENT SYSTEM  ====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Search BY ID")
    print("7. Exit")
    choice = input("Enter Your Choice:")
    if choice == "1":
        add_student()
        save_students_to_file()
    elif choice == "2":
        view_student()    
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
        save_students_to_file()
    elif choice == "5":
        update_student()
        save_students_to_file()
    elif choice == "6":
        search_by_id()
    elif choice == "7":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
        