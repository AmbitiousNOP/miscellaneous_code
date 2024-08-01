import unittest
import datetime
import employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp = employee.Employee("Karen", "Jones", "Manager",
                                     datetime.date.today())
        print("Debug: setUp method being called")

    def test_get_employee_properties(self):
        self.assertEqual(self.emp.first_name, "Karen")
        self.assertEqual(self.emp.last_name, "Jones")
        self.assertEqual(self.emp.job, "Manager")
        self.assertEqual(self.emp.hired, datetime.date.today())

    def test_get_employee_id(self):
        self.assertTrue(hasattr(self.emp, "emp_id"))

    def test_cannot_change_employee_id(self):
        with self.assertRaises(AttributeError):
            self.emp.emp_id = 99


if __name__ == "__main__":
    unittest.main()
