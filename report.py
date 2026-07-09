class Report:
    def __init__(self,employees):
        self.employees=employees
    
    def highest_salary(self):
       if not self.employees:
            print("No Records Found")
            return
       
       highest = None
       for emp in self.employees.values():
           if highest is None or emp.get_salary() > highest.get_salary():
               highest = emp
       print("\nHighest Salary Employee")
       highest.display_details()

    def experienced_employee(self):
        exp=int(input("Enter Experience: "))
        f=False
        for emp in self.employees.values():
            if emp.get_exp()>=exp:
                emp.display_details()
                f=True
        if not f:
            print("No Employee Found.")