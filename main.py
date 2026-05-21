students = {}
student_id = 1

# try:
#     with open("students.txt" , "r") as file:
#         for line in file:
#             clean_line = line.strip()
#             students.append(clean_line)
# except FileNotFoundError:
#         print("File not found.")
 
def add_student():
    global student_id
    name = input("👤Enter student name:").strip()
    for student in students.values():
        if student.casefold() == name.casefold():
            print(f"⚠️{name} already exists in the list")
            return
    else:
        students[student_id] = name
        save_students_to_file()
        student_id+=1
        print("✅Student added successfully.")
        return
 
def view_student():
    if not students:
            print("📂 List is empty.") 
            return
    else:
        print("📂 Students List:")
        for sid, student_name in students.items():
            print(f"{sid}.{student_name}")

def search_student():
    search_name = input("👤Enter the name to search:").strip()
    for student in students.values():
       if student.casefold() == search_name.casefold():
            print(f"✅{student} is in the list.")
            return
    else:
            print(f"❌{search_name} not found in records.")
            return

def delete_student():
    delete_name = input("Enter the name to delete:").strip()
    for sid, student_name in list(students.items()):
        if student_name.casefold() == delete_name.casefold():
            del students[sid]
            print(f"🗑️{student_name} has been deleted from the list.")
            return
    else:
        print(f"❌{delete_name} is not in the list.")
        return

def update_student():
    old_name = input("✏️Enter the name to update:").strip()
    for sid, student_name in list(students.items()):
        if student_name.casefold() == old_name.casefold():
            new_name = input("🆕Enter the new name:").strip()
            students[sid] = new_name
            print(f"✅{old_name} has been updated to {new_name}.")
            return
    else:
        print(f"{old_name} does not exist in the list.")
        return
        
def save_students_to_file():
    with open("students.txt", "w") as f:
        for sid , name in students.items():
            f.write(f"{sid},{name}\n")
            
def load_students_from_file():
    global student_id
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
                students[sid] = name
        if students:
            student_id = max(students.keys()) + 1
    except FileNotFoundError:
        print("File not found.")
        
load_students_from_file()

def search_by_id():
    search_id = int(input("🔎 Enter student ID: "))
    if search_id in students:
        print(f"{search_id} → {students[search_id]}")
    else:
        print("❌ ID Not Found")

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
        print("🚪exiting...")
        break
    else:
        print("⚠️invalid choice")
         