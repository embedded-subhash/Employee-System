class EmployeeIDIterator:

    def __init__(self, employee_ids):
        self.employee_ids = employee_ids
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.index >= len(self.employee_ids):
            raise StopIteration

        emp_id = self.employee_ids[self.index]
        self.index += 1

        return emp_id


employee_ids = [101, 102, 103, 104, 105]

iterator = EmployeeIDIterator(employee_ids)

for emp_id in iterator:
    print(emp_id)