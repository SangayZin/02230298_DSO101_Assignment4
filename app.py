"""
Flask application for CI/CD pipeline demonstration
"""
from flask import Flask, jsonify, request
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


@app.route('/api/add')
def add_numbers():
    """Add two numbers - accepts query parameters for negative numbers
    Usage: /api/add?a=-5&b=3
    """
    try:
        a = int(request.args.get('a', 0))
        b = int(request.args.get('b', 0))
        result = a + b
        return jsonify({
            'a': a,
            'b': b,
            'result': result,
            'operation': 'addition'
        })
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid parameters'}), 400


@app.route('/api/add/<int:a>/<int:b>')
def add_numbers_path(a, b):
    """Add two numbers - path parameters for positive numbers
    Usage: /api/add/5/3
    """
    result = a + b
    return jsonify({
        'a': a,
        'b': b,
        'result': result,
        'operation': 'addition'
    })


@app.route('/api/multiply')
def multiply_numbers():
    """Multiply two numbers - accepts query parameters for negative numbers
    Usage: /api/multiply?a=-5&b=3
    """
    try:
        a = int(request.args.get('a', 1))
        b = int(request.args.get('b', 1))
        result = a * b
        return jsonify({
            'a': a,
            'b': b,
            'result': result,
            'operation': 'multiplication'
        })
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid parameters'}), 400


@app.route('/api/multiply/<int:a>/<int:b>')
def multiply_numbers_path(a, b):
    """Multiply two numbers - path parameters for positive numbers
    Usage: /api/multiply/5/3
    """
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