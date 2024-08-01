import unittest
import employee


class TestEmployee(unittest.TestCase):

    def test_employee_object_creation(self):
        emp = employee.Employee()


if __name__ == "__main__":
    unittest.main()
