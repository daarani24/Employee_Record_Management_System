from employee import PermanentEmployee,ContractEmployee,InternEmployee

class EmployeeManager:
    def __init__(self):
        self.employees = {}

    def _create_employee(self,empid,name,age,dept,mail,number,exp,salary,emp_type):
        if emp_type==1:
            return PermanentEmployee(empid,name,age,dept,mail,number,exp,salary)
        elif emp_type==2:
            return ContractEmployee(empid,name,age,dept,mail,number,exp,salary)
        elif emp_type==3:
            return InternEmployee(empid,name,age,dept,mail,number,exp,salary)
        else:
            return None

    def add_employee(self):
        empid=int(input("Enter Employee ID   : "))

        if empid in self.employees:
            print("Employee ID already exists.")
            return
        
        name=input("Enter Name: ")
        age=int(input("Enter Age: "))
        exp=int(input("Enter Experience (years): "))
        salary=float(input("Enter Salary (Rs.): "))
        dept=input("Enter Department: ")
        mail=input("Enter Email: ")
        number=input("Enter number: ")

        if len(number)!=10:
            return "Invalid, Enter 10 digits."
        
        print("Employee Type: 1.Permanent  2.Contract  3.Intern")

        emp_type=int(input("Enter choice (1/2/3): "))

        emp=self._create_employee(empid,name,age,dept,mail,number,exp,salary,emp_type)
        if emp is None:
            print("Invalid employee type.")
            return
        self.employees[empid]=emp
        print("Employee added successfully.")

    def view_employee(self):
        if not self.employees:
            print("\nNo employee records found.")
            return
        for employee in self.employees.values():
            employee.display_details()

    def search_employee(self):
        empid=int(input("Enter Employee ID: "))
        if empid in self.employees:
            self.employees[empid].display_details()
        else:
            print("Employee not found.")

    def update_employee(self):
        empid=int(input("Enter Employee ID: "))
        if empid not in self.employees:
            print("Employee not found.")
            return
        emp=self.employees[empid]
        new_name=input("Enter New Name: ")
        new_dept=input("Enter new Department: ")
        new_salary = float(input("Enter New Salary: "))
        emp.set_name(new_name)
        emp.set_dept(new_dept)
        emp.set_salary(new_salary)
        print("Employee updated successfully.")

    def delete_employee(self):
        empid=int(input("Enter Employee ID: "))
        if empid in self.employees:
            del self.employees[empid]
            print("Employee deleted successfully.")
        else:
            print("Employee not found.")