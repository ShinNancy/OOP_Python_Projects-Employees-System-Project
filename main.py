"""
Main Function
"""

from employee import Employee
from managers import Manager
from directors import Director

# Define passwords for roles

MAN_PASS ="man"
DIR_PASS ="dir"

def run_manager_mode(manager):
    while True:
        print("\n1. Add Employee\n2. List Employees\n3. Remove Employee\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter full name: ")
            age = int(input("Enter age: "))
            salary = float(input("Enter salary: "))
            manager.add_employee(Employee(name, age, salary))

        elif choice == "2":
            manager.show_employee()

        elif choice == "3":
            name = input("Enter full name of employee to remove: ")
            manager.del_employee(name)

        elif choice == "4":
            print("Exiting Manager Mode...")
            break
        else:
            print("Invalid choice! Please try again.")

def run_director_mode(director):
  while True:
        print("\n1. Add Employee\n2. List Employees\n3. Remove Employee\n4. Update Salary\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter full name: ")
            age = int(input("Enter age: "))
            salary = float(input("Enter salary: "))
            director.add_employee(Employee(name, age, salary))

        elif choice == "2":
            director.list_employees()

        elif choice == "3":
            name = input("Enter full name of employee to remove: ")
            director.del_employee(name)

        elif choice == "4":
            name = input("Enter full name of employee to update: ")
            new_salary = float(input("Enter new salary: "))
            director.update_employee_salary(name, new_salary)

        elif choice == "5":
            print("Exiting Director Mode...")
            break
        else:
            print("Invalid choice! Please try again.")  

def main():
    print("Welcome to Employee Management System!")
    password = input("Enter your password: ")

    if password == MAN_PASS:
        print("\n MANAGER MODE")
        manager = Manager("John", 40, 20000)
        run_manager_mode(manager)

    elif password == DIR_PASS:
        print("\n DIRECTOR MODE")
        director = Director("Nancy", 32, 2000000)
        run_director_mode(director)

if __name__ == "__main__":
    main()
