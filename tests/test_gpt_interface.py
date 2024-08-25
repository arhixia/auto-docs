import unittest
from unittest.mock import patch, mock_open
from my_autodoc.gpt_interface import request_gpt

class TestGptInterface(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="mock project summary")
    @patch("openai.Completion.create")
    def test_request_gpt(self, mock_create, mock_file):
        mock_create.return_value.choices = [type("Choice", (object,), {"text": "Generated documentation"})]

        response = request_gpt("fake_api_key", "project_summary.txt")
        self.assertEqual(response, "Generated documentation")

if __name__ == "__main__":
    unittest.main()

