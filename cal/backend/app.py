from flask import Flask, request, jsonify
import math

app = Flask(__name__)

# Safe evaluation function
def safe_eval(expr):
    try:
        # Only allow math functions and numbers
        allowed_names = {k: v for k, v in math.__dict__.items()}
        return eval(expr, {"__builtins__": {}}, allowed_names)
    except Exception:
        return "Error"

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get("expression", "")
    result = safe_eval(expression)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
