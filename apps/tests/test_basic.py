import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from apps.accounts.models import User

@pytest.mark.django_db
def test_register_and_jwt():
    client = APIClient()
    payload = {'username': 'student1', 'password': 'StrongPass123', 'role': 'student'}
    resp = client.post('/api/auth/register/', payload, format='json')
    assert resp.status_code == 201
    resp2 = client.post('/api/token/', {'username':'student1','password':'StrongPass123'}, format='json')
    assert resp2.status_code == 200
    assert 'access' in resp2.data
