from employee import Employee
from file_handler import FileHandler
from report import Report
from employee_manager import EmployeeManager

manager=EmployeeManager()

while True:
    print("\nEMPLOYEE MANAGEMENT SYSTEM")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Highest Salary Employee")
    print("7. Experienced Employees")
    print("8. Save Data to File")
    print("9. Exit")

    choice=input("\nEnter your choice (1-9): ")

    if choice=="1":
        manager.add_employee()
    elif choice=="2":
        manager.view_employee()
    elif choice=="3":
        manager.search_employee()
    elif choice=="4":
        manager.update_employee()
    elif choice=="5":
        manager.delete_employee()
    elif choice=="6":
        manager.highest_salary()
    elif choice=="7":
        manager.experienced_employee()
    elif choice=="8":
        manager.save_to_file()
    elif choice=="9":
        print("\nThank you for using Employee Management System.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 9.")