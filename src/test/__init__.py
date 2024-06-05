import unittest
from app import app

class BasicTests(unittest.TestCase):
    """
    Basic unit tests for the Flask application.
    """

    def setUp(self):
        """
        Set up the test client for the Flask application.
        This method is called before each test.
        """
        self.app = app.test_client()  # Create a test client for the Flask application
        self.app.testing = True       # Enable testing mode for better error messages

    def test_home(self):
        """
        Test the home page ('/') route.
        Ensures that the home page loads successfully with a status code of 200.
        """
        response = self.app.get('/')  # Make a GET request to the home page
        self.assertEqual(response.status_code, 200)  # Check that the response status code is 200

if __name__ == '__main__':
    unittest.main()  # Run the unit tests
