"""
Class: Employee
"""

class Employee:
    def __init__(self, full_name, age, salary):
         self.full_name =full_name
         self.age = age
         self.salary = salary

    def __str__(self):
         return f"Full name: {self.full_name} \nAge: {self.age} \n Salary:${self.salary}"