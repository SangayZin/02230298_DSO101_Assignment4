"""
Unit tests for the Flask application
"""
import pytest
from app import app, add, multiply


@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestHome:
    """Test home endpoint"""

    def test_home(self, client):
        """Test home endpoint returns welcome message"""
        response = client.get('/')
        assert response.status_code == 200
        assert 'message' in response.json
        assert response.json['message'] == 'Welcome to the CI/CD Pipeline App!'

    def test_home_basic_assertion(self):
        """Test basic assertion"""
        assert 1 + 1 == 2


class TestHealth:
    """Test health check endpoint"""

    def test_health_check(self, client):
        """Test health endpoint"""
        response = client.get('/health')
        assert response.status_code == 200
        assert response.json['status'] == 'healthy'


class TestAddEndpoint:
    """Test add endpoint"""

    def test_add_endpoint(self, client):
        """Test add endpoint with valid numbers"""
        response = client.get('/api/add/5/3')
        assert response.status_code == 200
        assert response.json['a'] == 5
        assert response.json['b'] == 3
        assert response.json['result'] == 8
        assert response.json['operation'] == 'addition'

    def test_add_endpoint_negative(self, client):
        """Test add endpoint with negative numbers"""
        response = client.get('/api/add/-5/3')
        assert response.status_code == 200
        assert response.json['result'] == -2

    def test_add_endpoint_zero(self, client):
        """Test add endpoint with zero"""
        response = client.get('/api/add/0/0')
        assert response.status_code == 200
        assert response.json['result'] == 0


class TestMultiplyEndpoint:
    """Test multiply endpoint"""

    def test_multiply_endpoint(self, client):
        """Test multiply endpoint with valid numbers"""
        response = client.get('/api/multiply/5/3')
        assert response.status_code == 200
        assert response.json['a'] == 5
        assert response.json['b'] == 3
        assert response.json['result'] == 15
        assert response.json['operation'] == 'multiplication'

    def test_multiply_endpoint_zero(self, client):
        """Test multiply endpoint with zero"""
        response = client.get('/api/multiply/5/0')
        assert response.status_code == 200
        assert response.json['result'] == 0


class TestHelperFunctions:
    """Test helper functions"""

    def test_add_function(self):
        """Test add helper function"""
        assert add(1, 1) == 2
        assert add(5, 3) == 8
        assert add(-5, 3) == -2
        assert add(0, 0) == 0

    def test_multiply_function(self):
        """Test multiply helper function"""
        assert multiply(5, 3) == 15
        assert multiply(0, 5) == 0
        assert multiply(-5, 3) == -15
        assert multiply(2, 2) == 4
