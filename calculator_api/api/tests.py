import pytest
from .views import upload_file
from django.test import RequestFactory

csv_data_valid = [
    ("2", "+", "3"),
    ("10", "-", "4"),
    ("3", "*", "3"),
    ("8", "/", "2")
]

csv_data_div_by_zero = [
    ("10", "/", "0")
]

csv_data_invalid_operator = [
    ("5", "^", "2")
]

AUTH_PASSPHRASE = "Jf8s!j9L2fS0K"


@pytest.mark.django_db
def test_addition():
    request_factory = RequestFactory()
    request = request_factory.post('/api/upload/',
                                   data={"file": csv_data_valid},
                                   content_type='multipart/form-data')
    request.headers = {"Authorization": AUTH_PASSPHRASE}

    response = upload_file(request)

    assert response.status_code == 200
    assert response.json()["result"] == 24


@pytest.mark.django_db
def test_division_by_zero():
    request_factory = RequestFactory()
    request = request_factory.post('/api/upload/',
                                   data={"file": csv_data_div_by_zero},
                                   content_type='multipart/form-data')
    request.headers = {"Authorization": AUTH_PASSPHRASE}

    response = upload_file(request)

    assert response.status_code == 400
    assert "Division by zero" in response.json()["error"]


@pytest.mark.django_db
def test_invalid_operator():
    request_factory = RequestFactory()
    request = request_factory.post('/api/upload/',
                                   data={"file": csv_data_invalid_operator},
                                   content_type='multipart/form-data')
    request.headers = {"Authorization": AUTH_PASSPHRASE}

    response = upload_file(request)

    assert response.status_code == 200
    assert response.json()["result"] == 0
