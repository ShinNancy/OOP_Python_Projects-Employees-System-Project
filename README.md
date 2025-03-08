### <h1>Employees System Project </h1>

The **Employees System Project** is a Python-based application that demonstrates the principles of **Object-Oriented Programming (OOP)**. This project includes three main classes: **Employee, Manager, and Director**, each with distinct roles and permissions. It serves as a foundational example of how OOP concepts can be applied to manage employee data and interactions efficiently.

---

## Table of Contents

- [Introduction](#introduction)  
- [Classes](#classes)  
  - [Employee](#employee)  
  - [Manager](#manager-inherits-from-employee)  
  - [Director](#director-inherits-from-manager)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  

---

## Introduction

This project provides a **structured way to manage employees** using OOP principles in Python. Each class represents a different role within a company, **inheriting and extending functionalities accordingly**.

---

## Classes

### Employee

The **Employee** class represents a basic employee with the following attributes:

- `full_name`: The name of the employee.  
- `age`: The age of the employee.  
- `salary`: The salary of the employee.  

This class provides methods for **displaying employee information** in a formatted manner.

### Manager (Inherits from Employee)

The **Manager** class extends the `Employee` class and includes additional functionalities, such as:

- Managing a **list of employees**.  
- **Adding new employees**.  
- **Removing employees** by name.  

### Director (Inherits from Manager)

The **Director** class further extends the `Manager` class with **higher-level privileges**, including:

- **Modifying system-wide settings**.  
- **Overriding employee data**.  
- **Having full control** over the employee management system.  

---

## Features

✔️ **Object-Oriented Design** – Implements **inheritance, encapsulation, and polymorphism**.  
✔️ **Role-Based Access** – Employees, Managers, and Directors have different levels of control.  
✔️ **Employee Management** – Easily **add, update, and remove** employees.  
✔️ **Command-Line Interface (CLI)** – Provides an **interactive experience**.  

---

## Installation

Clone the repository:

```bash
git clone https://github.com/ShinNancy/OOP_Python_Projects-Employees-System-Project.git
```

Navigate to the project directory:

```bash
cd employeesSystem
```

Run the program:

```bash
python main.py
```

---

## Usage

1. Run `main.py` to start the system.  
2. Enter login credentials to determine **access level** (Manager or Director).  
3. Use the **interactive menu** to manage employees.  

---

This project is designed for **beginners** to learn **OOP in Python** while implementing a simple yet functional **employee management system**.  

**Contributions are welcome! 🚀**
