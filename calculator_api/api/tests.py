import pytest
from .views import upload_file
from django.test import RequestFactory

# Sample data for tests
csv_data_valid = [
    ("2", "+", "3"),
    ("10", "-", "4"),
    ("3", "*", "3"),
    ("8", "/", "2")
]

csv_data_div_by_zero = [
    ("10", "/", "0")  # Division by zero
]

csv_data_invalid_operator = [
    ("5", "^", "2")  # Unsupported operator
]

AUTH_PASSPHRASE = "Jf8s!j9L2fS0K"


@pytest.mark.django_db
def test_addition():
    # Simulate a file upload request with valid CSV data
    request_factory = RequestFactory()
    request = request_factory.post('/api/upload/',
                                   data={"file": csv_data_valid},
                                   content_type='multipart/form-data')
    request.headers = {"Authorization": AUTH_PASSPHRASE}

    # Run the view
    response = upload_file(request)

    # Check that response contains the correct calculation
    assert response.status_code == 200
    assert response.json()["result"] == 24  # Expected result of (2+3) + (10-4) + (3*3) + (8/2)


@pytest.mark.django_db
def test_division_by_zero():
    request_factory = RequestFactory()
    request = request_factory.post('/api/upload/',
                                   data={"file": csv_data_div_by_zero},
                                   content_type='multipart/form-data')
    request.headers = {"Authorization": AUTH_PASSPHRASE}

    # Run the view
    response = upload_file(request)

    # Check that the view properly handles division by zero
    assert response.status_code == 400
    assert "Division by zero" in response.json()["error"]


@pytest.mark.django_db
def test_invalid_operator():
    request_factory = RequestFactory()
    request = request_factory.post('/api/upload/',
                                   data={"file": csv_data_invalid_operator},
                                   content_type='multipart/form-data')
    request.headers = {"Authorization": AUTH_PASSPHRASE}

    # Run the view
    response = upload_file(request)

    # Check that unsupported operators are ignored
    assert response.status_code == 200
    assert response.json()["result"] == 0  # Expect 0 as no valid operations are performed
