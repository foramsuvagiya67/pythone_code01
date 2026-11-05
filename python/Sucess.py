employees = []

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = input("Enter Salary: ")

    employee = {
        "ID": emp_id,
        "Name": name,
        "Department": department,
        "Salary": salary
    }

    employees.append(employee)
    print("\nEmployee added successfully!\n")


def view_employees():
    if not employees:
        print("\nNo employee records available!\n")
    else:
        print("\n===== EMPLOYEE DETAILS =====")

        for emp in employees:
            print("Employee ID:", emp["ID"])
            print("Name:", emp["Name"])
            print("Department:", emp["Department"])
            print("Salary:", emp["Salary"])
            print("----------------------------")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")

    for emp in employees:
        if emp["ID"] == emp_id:
            emp["Name"] = input("Enter New Name: ")
            emp["Department"] = input("Enter New Department: ")
            emp["Salary"] = input("Enter New Salary: ")

            print("\nEmployee updated successfully!\n")
            return

    print("\nEmployee not found!\n")


def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")

    for emp in employees:
        if emp["ID"] == emp_id:
            employees.remove(emp)
            print("\nEmployee deleted successfully!\n")
            return

    print("\nEmployee not found!\n")

while True:
    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        update_employee()

    elif choice == "4":
        delete_employee()

    elif choice == "5":
        print("\nThank you for using Employee Management System!")
        break

    else:
        print("\nInvalid choice! Please enter 1 to 5.")
