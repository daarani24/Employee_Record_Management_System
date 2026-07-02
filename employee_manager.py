from employee import PermanentEmployee, ContractEmployee

class EmployeeManager:
    def __init__(self):
        self.employees = {}

    def add_employee(self):
        try:
            emp_id = int(input("Enter Employee ID   : "))
        except ValueError:
            print("Invalid ID. Please enter a number.")
            return

        if emp_id in self.employees:
            print("Employee ID already exists.")
            return

        name = input("Enter Name          : ")
        
        try:
            age = int(input("Enter Age           : "))
            exp = int(input("Enter Experience (years): "))
            salary = float(input("Enter Salary (Rs.)  : "))
        except ValueError:
            print("Invalid input. Age, experience, and salary must be numbers.")
            return

        dept = input("Enter Department    : ")
        mail = input("Enter Email         : ")

        print("Employee Type: 1. Permanent  2. Contract")
        emp_choice = input("Enter choice (1/2)  : ")

        if emp_choice == "1":
            emp = PermanentEmployee(emp_id, name, age, dept, mail, exp, salary)
        elif emp_choice == "2":
            emp = ContractEmployee(emp_id, name, age, dept, mail, exp, salary)
        else:
            print("Invalid employee type.")
            return

        self.employees[emp_id] = emp
        print("Employee added successfully.")

    def view_employee(self):
        if not self.employees:
            print("No employee records found.")
            return
        for employee in self.employees.values():
            employee.display_details()
            print("Bonus      : Rs.", employee.calculate_bonus())

    def search_employee(self):
        try:
            emp_id = int(input("Enter Employee ID to search: "))
        except ValueError:
            print("Invalid ID.")
            return

        if emp_id in self.employees:
            self.employees[emp_id].display_details()
            print("Bonus          : Rs.", self.employees[emp_id].calculate_bonus())
        else:
            print("Employee not found.")

    def update_employee(self):
        try:
            emp_id = int(input("Enter Employee ID to update: "))
        except ValueError:
            print("Invalid ID.")
            return

        if emp_id not in self.employees:
            print("Employee not found.")
            return

        emp = self.employees[emp_id]
        new_name = input("Enter New Name   : ")
        try:
            new_salary = float(input("Enter New Salary : "))
        except ValueError:
            print("Invalid salary.")
            return

        emp.set_name(new_name)
        emp.set_salary(new_salary)
        print("Employee updated successfully.")

    def delete_employee(self):
        try:
            emp_id = int(input("Enter Employee ID to delete: "))
        except ValueError:
            print("Invalid ID.")
            return

        if emp_id in self.employees:
            del self.employees[emp_id]
            print("Employee deleted successfully.")
        else:
            print("Employee not found.")

    def save_to_file(self):
        with open("data.txt", "w") as file:
            for emp in self.employees.values():
                file.write(
                    f"{emp.get_emp_id()},"
                    f"{emp.get_name()},"
                    f"{emp.get_age()},"
                    f"{emp.get_dept()},"
                    f"{emp.get_mail()},"
                    f"{emp.get_exp()},"
                    f"{emp.get_salary()},"
                    f"{emp.get_emp_type()}\n"
                )
        print("Data saved to data.txt successfully.")