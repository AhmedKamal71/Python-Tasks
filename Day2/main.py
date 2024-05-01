from employee import Employee
from manager import Manager

def interface_menu():
    while True:
        print("\nMenu:")
        print("1. Add a new employee (enter 'add')")
        print("2. Transfer an employee (enter 'transfer')")
        print("3. Fire an employee (enter 'fire')")
        print("4. List all employees (enter 'list')")
        print("5. Exit the program (enter 'q')")

        command = input("\nEnter your choice: ").strip().lower()

        if command == "add":
            role = input("If manager press 'm', if employee press 'e': ").strip().lower()
            if role == 'e':
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                age = int(input("Age: "))
                department = input("Department: ")
                salary = float(input("Salary: "))
                Employee(first_name, last_name, age, department, salary)
                print("Employee added successfully!")
            elif role == 'm':
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                age = int(input("Age: "))
                department = input("Department: ")
                salary = float(input("Salary: "))
                managed_department = input("Managed Department: ")
                Manager(first_name, last_name, age, department, salary, managed_department)
                print("Manager added successfully!")
            else:
                print("Invalid input. Please try again.")
        elif command == "transfer":
            first_name = input("First Name of the employee to transfer: ")
            last_name = input("Last Name of the employee to transfer: ")
            new_department = input("New Department: ")
            employee = Employee.db.find_one({"first_name": first_name, "last_name": last_name})
            if employee:
                emp = Employee(employee["first_name"], employee["last_name"], employee["age"], employee["department"],
                               employee["salary"])
                emp.transfer(new_department)
                print("Employee transferred successfully!")
            else:
                print("Employee not found.")
        elif command == "fire":
            first_name = input("First Name of the employee to fire: ")
            last_name = input("Last Name of the employee to fire: ")
            query = {"first_name": first_name, "last_name": last_name}
            result = Employee.db.delete_one(query)
            if result.deleted_count == 1:
                print("Employee fired successfully!")
            else:
                print("Employee not found.")
        elif command == "list":
            Employee.list_employees()
        elif command == "q":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    interface_menu()
