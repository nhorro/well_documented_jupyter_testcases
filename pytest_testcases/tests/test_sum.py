import pytest
import requests

def test_sum(calculator_service):
    query = {'a':'2', 'b':'2'}
    response = requests.get("http://localhost:80/isum",query)
    assert(response.status_code == 200)
    assert("result" in response.json())
    assert(response.json()["result"] == 4)