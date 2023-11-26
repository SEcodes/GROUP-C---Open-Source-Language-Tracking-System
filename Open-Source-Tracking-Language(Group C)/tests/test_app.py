import unittest
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    python_code = request.json['code']
    try:
        compile(python_code, '<string>', 'exec')
        return jsonify({'result': 'No syntax errors detected.'})
    except SyntaxError as e:
        return jsonify({'result': str(e)})

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_analyze_success(self):
        response = self.app.post(
            '/analyze',
            json={'code': 'print("Hello, World!")'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 'No syntax errors detected.')

   

if __name__ == '__main__':
    unittest.main()