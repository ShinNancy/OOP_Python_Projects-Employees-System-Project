"""
Class: Manager
"""
from employee import Employee

class Manager(Employee):
    def __init__(self, full_name, age, salary):
        super().__init__(full_name, age, salary)
        self.employees =[]

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added: {employee.full_name}")

    def del_employee(self, full_name):
        # self.employees = [e for e in self.employees if e.full_name != full_name]
        for employee in self.employees:
            if employee.full_name == full_name:
                self.employees.remove(employee)
                print(f"Removed: {full_name}")
                return
        print(f"Employee {full_name} not found.")

    def show_employee(self):
        if not self.employees:
            print("Not found")
            return
        print("Employee list: ")
        for e in self.employees:
            print(f" {e.full_name}, {e.age}, {e.salary}")