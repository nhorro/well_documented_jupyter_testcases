import pytest
import requests

def test_mul(calculator_service):
    query = {'a':'3', 'b':'3'}
    response = requests.get("http://localhost:80/imul",query)
    assert(response.status_code == 200)
    assert("result" in response.json())
    assert(response.json()["result"] == 9)