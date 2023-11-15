from flask import Flask, render_template, request, jsonify
import ast

app = Flask(__name__)

def analyze_code(code):
    try:
        # Attempt to parse the code using AST (Abstract Syntax Tree)
        ast.parse(code)
        return {"error": False, "message": "No syntax errors detected."}
    except SyntaxError as e:
        return {"error": True, "message": str(e)}

# Define a route for the home page
@app.route('/')
def index():
    # Render the 'index.html' template for the home page
    return render_template('index.html')

# Define a route for analyzing code (POST request)
@app.route('/analyze_code', methods=['POST'])
def analyze_code_route():
    # Get the code from the form data in the request
    code = request.form['code']
    
    # Call the analyze_code function to check for syntax errors
    result = analyze_code(code)
    
    # Return the result as JSON (JavaScript Object Notation)
    return jsonify(result)

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
