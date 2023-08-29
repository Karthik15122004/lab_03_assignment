class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search_by_age(self, age, operator):
        results = []
        for employee in self.employees:
            if operator == "=" and employee.age == age:
                results.append(employee)
            elif operator == ">" and employee.age > age:
                results.append(employee)
            elif operator == ">=" and employee.age >= age:
                results.append(employee)
            elif operator == "<" and employee.age < age:
                results.append(employee)
            elif operator == "<=" and employee.age <= age:
                results.append(employee)
        return results

    def search_by_name(self, name):
        results = []
        for employee in self.employees:
            if name.lower() in employee.name.lower():
                results.append(employee)
        return results

    def search_by_salary(self, salary, operator):
        results = []
        for employee in self.employees:
            if operator == "=" and employee.salary == salary:
                results.append(employee)
            elif operator == ">" and employee.salary > salary:
                results.append(employee)
            elif operator == ">=" and employee.salary >= salary:
                results.append(employee)
            elif operator == "<" and employee.salary < salary:
                results.append(employee)
            elif operator == "<=" and employee.salary <= salary:
                results.append(employee)
        return results

def main():
    db = EmployeeDatabase()

    db.add_employee(Employee("161E90", "Raman", 41, 56000))
    db.add_employee(Employee("161F91", "Himadri", 38, 67500))
    db.add_employee(Employee("161F99", "Jaya", 51, 82100))
    db.add_employee(Employee("171E20", "Tejas", 30, 55000))
    db.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Search Parameters:")
    print("1. Age\n2. Name\n3. Salary (>, <, <=, >=)")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        age = int(input("Enter age: "))
        operator = input("Enter operator (=, >, >=, <, <=): ")
        results = db.search_by_age(age, operator)
    elif choice == 2:
        name = input("Enter name: ")
        results = db.search_by_name(name)
    elif choice == 3:
        salary = int(input("Enter salary: "))
        operator = input("Enter operator (=, >, >=, <, <=): ")
        results = db.search_by_salary(salary, operator)
    else:
        print("Invalid choice")

    if results:
        print("Search Results:")
        for employee in results:
            print(f"Employee ID: {employee.emp_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")
    else:
        print("No results found")

if __name__ == "__main__":
    main()
