import unittest
import os
from my_autodoc.doc_generator import save_documentation

class TestDocGenerator(unittest.TestCase):

    def test_save_documentation(self):
        doc_text = "This is a test documentation."
        save_documentation(doc_text, "test_documentation.md")
        self.assertTrue(os.path.exists("test_documentation.md"))

        with open("test_documentation.md", "r") as f:
            content = f.read()
            self.assertEqual(content, doc_text)

        os.remove("test_documentation.md")

if __name__ == "__main__":
    unittest.main()
