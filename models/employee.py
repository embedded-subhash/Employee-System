class Employee:
    def __init__(
            self,
            employee_id,
            name,
            email,
            department,
            salary,
            experience
            ):
        
        self.employee_id=employee_id
        self.name=name
        self.email=email
        self.department=department
        self.salary=salary
        self.experience =experience

    def display_details(self):
        print("\nEmployee Details")
        print("-" * 30)
        print(f"Employee ID : {self.employee_id}")
        print(f"Name        : {self.name}")
        print(f"Email       : {self.email}")
        print(f"Department  : {self.department}")
        print(f"Salary      : {self.salary}")
        print(f"Experience  : {self.experience} years")


    def calculate_bonus(self):
        if self.experience <= 2:
            bonus_percentage = 0.05
        elif self.experience <= 5:
            bonus_percentage = 0.10
        elif self.experience <= 10:
            bonus_percentage = 0.15
        else:
            bonus_percentage = 0.20

        bonus = self.salary * bonus_percentage
        return bonus

    def generate_salary_slip(self):
        bonus = self.calculate_bonus()
        total_salary = self.salary + bonus

        print("\n" + "=" * 40)
        print("         EMPLOYEE SALARY SLIP")
        print("=" * 40)
        print(f"Employee ID : {self.employee_id}")
        print(f"Name        : {self.name}")
        print(f"Email       : {self.email}")
        print(f"Department  : {self.department}")
        print(f"Salary      : ₹{self.salary}")
        print(f"Experience  : {self.experience} years")
        print(f"Bonus       : ₹{bonus}")
        print(f"Total Salary: ₹{total_salary}")
        print("=" * 40)
    def update_details(self,name,email,department,salary,experience):
        self.name=name
        self.email=email
        self.department=department
        self.salary=salary
        self.experience =experience
        print("Employee details updated successfully.")
    def to_dict(self):
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "email": self.email,
            "department": self.department,
            "salary": self.salary,
            "experience": self.experience
        }