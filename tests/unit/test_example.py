"""test example module."""
import unittest


class TestExampleCase(unittest.TestCase):
    
    # @unittest.skip("Example Test Case")
    def test_example_case(self):
        """Test that the files are retrieved."""
        token = "test"
        assert token == "test"