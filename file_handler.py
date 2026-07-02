class FileHandler:
    @staticmethod
    def save_to_file(employees):
        with open("data.txt", "w") as file:
            for emp in employees.values():
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
        print("Data saved successfully.")