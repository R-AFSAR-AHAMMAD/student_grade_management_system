student_grades = {}

def add_student(name, grade):
    student_grades[name] = grade
    print(f"✅ Added {name} with grade: {grade}")

def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"✅ Updated {name}'s grade to {grade}")
    else:
        print(f"❌ Student '{name}' not found!")

def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"✅ Deleted {name} from records")
    else:
        print(f"❌ Student '{name}' not found!")

def display_all_students():
    if student_grades:
        print("\n📋 All Student Grades:")
        for name, grade in student_grades.items():
            print(f" - {name}: {grade}")
    else:
        print("⚠️ No students found or added yet.")

def main():
    while True:
        print("\n🎓 Student Grade Management System")
        print("1. ➕ Add Student")
        print("2. ✏️ Update Student Grade")
        print("3. ❌ Delete Student")
        print("4. 📄 View All Students")
        print("5. 🚪 Exit")
        
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("❌ Invalid input! Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            name = input("Enter student name: ").strip()
            try:
                grade = float(input("Enter student grade (e.g., 88.5): "))
                add_student(name, grade)
            except ValueError:
                print("❌ Invalid grade. Please enter a numeric value.")
        elif choice == 2:
            name = input("Enter student name: ").strip()
            try:
                grade = float(input("Enter new grade: "))
                update_student(name, grade)
            except ValueError:
                print("❌ Invalid grade. Please enter a numeric value.")
        elif choice == 3:
            name = input("Enter student name: ").strip()
            delete_student(name)
        elif choice == 4:
            display_all_students()
        elif choice == 5:
            print("👋 Exiting the program. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
