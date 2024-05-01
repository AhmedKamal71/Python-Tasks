from database import Database

class Employee:
    db = Database().collection

    def __init__(self, first_name, last_name, age, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary

        self.insert_into_db()

    def insert_into_db(self):
        employee_data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "department": self.department,
            "salary": self.salary
        }
        self.db.insert_one(employee_data)

    def transfer(self, new_department):
        query = {"first_name": self.first_name, "last_name": self.last_name}
        new_values = {"$set": {"department": new_department}}

        result = self.db.update_one(query, new_values)

        if result.modified_count == 1:
            print("Employee's department has been successfully updated.")
            self.department = new_department
        else:
            print("Failed to update employee's department.")

    def fire(self):
        query = {"first_name": self.first_name, "last_name": self.last_name}
        self.db.delete_one(query)

    def show(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")

    @classmethod
    def list_employees(cls):
        employees = cls.db.find()
        for emp in employees:
            print(
                f"First Name: {emp['first_name']}, Last Name: {emp['last_name']}, Age: {emp['age']}, Department: {emp['department']}, Salary: {emp['salary']}")
