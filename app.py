"""
Flask application for CI/CD pipeline demonstration
"""
from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({'message': 'Welcome to the CI/CD Pipeline App!'})


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200


@app.route('/api/add/<int:a>/<int:b>')
def add_numbers(a, b):
    """Add two numbers"""
    result = a + b
    return jsonify({
        'a': a,
        'b': b,
        'result': result,
        'operation': 'addition'
    })


@app.route('/api/multiply/<int:a>/<int:b>')
def multiply_numbers(a, b):
    """Multiply two numbers"""
    result = a * b
    return jsonify({
        'a': a,
        'b': b,
        'result': result,
        'operation': 'multiplication'
    })


def add(a, b):
    """Helper function to add two numbers"""
    return a + b


def multiply(a, b):
    """Helper function to multiply two numbers"""
    return a * b


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
