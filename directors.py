"""
Class: Director
"""

from managers import Manager

class Director(Manager):
    def __init__(self, full_name, age, salary):
        super().__init__(full_name, age, salary)

    def update_employee_salary(self, full_name, new_salary):
        for e in self.employees:
            if e.full_name == full_name:
                e.full_name == new_salary
                print(f"Update {full_name}'s salary to $ {new_salary}")
                return
            
        print(f"{full_name} not found.")