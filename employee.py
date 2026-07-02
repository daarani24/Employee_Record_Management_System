from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self,empid,name,age,dept,mail,number,exp,salary,emp_type):
        self.__empid=empid
        self.__name=name
        self.__age=age
        self.__dept=dept
        self.__mail=mail
        self.__number=number
        self.__exp=exp
        self.__salary=salary
        self.__emp_type=emp_type

    def get_emp_id(self):
        return self.__empid
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_dept(self):
        return self.__dept
    def get_mail(self):
        return self.__mail
    def get_number(self):
        return self.__number
    def get_exp(self):
        return self.__exp
    def get_salary(self):
        return self.__salary
    def get_emp_type(self):
        return self.__emp_type

    def set_name(self, name):
        self.__name=name
    def set_salary(self, salary):
        self.__salary=salary
    def set_dept(self,dept):
        self.__dept=dept

    @abstractmethod
    def calculate_bonus(self):
        pass

    @abstractmethod
    def work_mode(self):
        pass

    def display_details(self):
        print("\nEmployee Details")
        print("ID         :",self.__empid)
        print("Name       :",self.__name)
        print("Age        :",self.__age)
        print("Department :",self.__dept)
        print("Email      :",self.__mail)
        print("Number     :",self.__number)
        print("Experience :",self.__exp, "years")
        print("Salary     : Rs.",self.__salary)
        print(f"Bonus     : Rs.{self.calculate_bonus():,.2f}")
        print(f"Work Mode :{self.work_mode()}")
    
class PermanentEmployee(Employee):
    def __init__(self,empid,name,age,dept,mail,number,exp,salary):
        super().__init__(empid,name,age,dept,mail,number,exp,salary,"Permanent")

    def calculate_bonus(self):
        return self.get_salary()*0.20
    def work_mode(self):
        return "Work From Office"

class ContractEmployee(Employee):
    def __init__(self,empid,name,age,dept,mail,number,exp,salary):
        super().__init__(empid,name,age,dept,mail,number,exp,salary,"Contract")

    def calculate_bonus(self):
        return self.get_salary()*0.10
    def work_mode(self):
        return "Hybrid"
    
class InternEmployee(Employee):
    def __init__(self,empid,name,age,dept,mail,number,exp,salary):
        super().__init__(empid,name,age,dept,mail,number,exp,salary,"Intern")
    
    def calculate_bonus(self):
        return self.get_salary*0.05
    def work_mode(self):
        return "Training + Office"
    