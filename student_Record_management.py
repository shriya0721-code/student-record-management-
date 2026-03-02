students = []

def add_student():
    name = input("Enter student name: ")

    marks = []
    for i in range(3):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)

    average = sum(marks) / len(marks)

    student = {
        "name": name,
        "marks": marks,
        "average": average
    }

    students.append(student)
    print("Student added successfully!\n")


def view_students():
    if not students:
        print("No students found.\n")
        return

    for student in students:
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("Average:", round(student["average"], 2))
        print("-" * 30)


def search_student():
    name = input("Enter student name to search: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("Student Found!")
            print("Marks:", student["marks"])
            print("Average:", round(student["average"], 2))
            return

    print("Student not found.\n")


def show_topper():
    if not students:
        print("No students available.\n")
        return

    topper = max(students, key=lambda x: x["average"])

    print("Topper is:", topper["name"])
    print("Average:", round(topper["average"], 2))


def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Show Topper")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            show_topper()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")


main()