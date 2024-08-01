import unittest
import datetime
import employee


class TestEmployee(unittest.TestCase):

    def test_employee_object_creation(self):
        emp = employee.Employee("Karen", "Jones", "Manager",
                                datetime.date.today())


if __name__ == "__main__":
    unittest.main()
