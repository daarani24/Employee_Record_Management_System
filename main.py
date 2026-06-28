from employee_manager import EmployeeManager

manager = EmployeeManager()

while True:
    print("\n=============================")
    print("  EMPLOYEE MANAGEMENT SYSTEM ")
    print("=============================")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Save Data to File")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "1":
        manager.add_employee()
    elif choice == "2":
        manager.view_employee()
    elif choice == "3":
        manager.search_employee()
    elif choice == "4":
        manager.update_employee()
    elif choice == "5":
        manager.delete_employee()
    elif choice == "6":
        manager.save_to_file()
    elif choice == "7":
        print("\nThank you for using Employee Management System.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")