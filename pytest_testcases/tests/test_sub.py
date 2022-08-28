import pytest
import requests

def test_sub(calculator_service):
    query = {'a':'5', 'b':'3'}
    response = requests.get("http://localhost:80/isub",query)
    assert(response.status_code == 200)
    assert("result" in response.json())
    assert(response.json()["result"] == 2)