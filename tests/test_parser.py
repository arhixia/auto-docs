import unittest
import os
from my_autodoc.parser import parse_project, save_summary

class TestParser(unittest.TestCase):

    def setUp(self):
        self.test_directory = "test_project"
        os.makedirs(self.test_directory, exist_ok=True)
        with open(os.path.join(self.test_directory, "test_file.py"), "w") as f:
            f.write("""
def test_function():
    pass

class TestClass:
    def method(self):
        pass
""")

    def tearDown(self):
        for root, _, files in os.walk(self.test_directory):

            for file in files:
                os.remove(os.path.join(root, file))
        os.rmdir(self.test_directory)

    def test_parse_project(self):
        project_data = parse_project(self.test_directory)
        expected_file_path = os.path.join("test_project", "test_file.py")
        self.assertIn(expected_file_path, project_data)
        self.assertIn("Function: test_function", project_data[expected_file_path])
        self.assertIn("Class: TestClass", project_data[expected_file_path])

    def test_save_summary(self):
        project_data = parse_project(self.test_directory)
        save_summary(project_data, "test_summary.txt")
        self.assertTrue(os.path.exists("test_summary.txt"))

        with open("test_summary.txt", "r") as f:
            content = f.read()
            expected_file_path = os.path.join("test_project", "test_file.py")
            self.assertIn(f"File: {expected_file_path}", content)
            self.assertIn("Function: test_function", content)
            self.assertIn("Class: TestClass", content)

        os.remove("test_summary.txt")

if __name__ == "__main__":
    unittest.main()
