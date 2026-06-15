def employee_generator():

    for i in range(1, 100001):

        yield {
            "employee_id": i,
            "name": f"Employee{i}",
            "department": "IT"
        }


employees = employee_generator()

for _ in range(10):
    print(next(employees))