import unittest
import json
from flask import Flask, request, jsonify

# Create a Flask application instance
app = Flask(__name__)

# Define a route '/analyze' that accepts POST requests
@app.route('/analyze', methods=['POST'])
def analyze():
    # Extract Python code from the JSON data received in the request
    python_code = request.json['code']
    
    try:
        # Attempt to compile the Python code to check for syntax errors
        compile(python_code, '<string>', 'exec')
        # If compilation succeeds, return a JSON response indicating no syntax errors
        return jsonify({'result': 'No syntax errors detected.'})
    except SyntaxError as e:
        # If a SyntaxError occurs during compilation, return a JSON response with the error message
        return jsonify({'result': str(e)})

# Create a test case class for testing the Flask application
class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        # Create a test client for the Flask application
        self.app = app.test_client()

    def test_analyze_success(self):
        # Test the '/analyze' route with a valid Python code
        response = self.app.post(
            '/analyze',
            json={'code': 'print("Hello, World!")'}
        )
        # Parse the JSON response received from the server
        data = json.loads(response.data)
        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Assert that the result in the response indicates no syntax errors
        self.assertEqual(data['result'], 'No syntax errors detected.')

# Run the unit tests if this script is executed directly
if __name__ == '__main__':
    unittest.main()
