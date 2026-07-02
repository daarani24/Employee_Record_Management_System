class Report:
    def __init__(self,employees):
        self.employees=employees
    
    def highest_salary(self):
       if not self.employees:
            print("No Records Found")
            return
       high=None
       for emp in self.employees.values():
           if high is None or self.get_salary()>high.get_salary():
               high=emp
       print("\nHighest Salary Employee")
       high.display_details()

    def experienced_employee(self):
        exp=int(input("Enter Experience: "))
        f=False
        for emp in self.employees.values():
            if emp.get_exp()>=exp:
                emp.display_details()
                f=True
        if not f:
            print("No Employee Found.")