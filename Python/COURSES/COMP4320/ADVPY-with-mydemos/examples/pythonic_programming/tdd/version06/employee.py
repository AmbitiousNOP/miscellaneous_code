class Employee:
    id_generator = 1000  # Shared Class variable

    def __init__(self, first_name, last_name, job, hired):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.hired = hired
        self.emp_id = Employee.id_generator
        Employee.id_generator += 1
