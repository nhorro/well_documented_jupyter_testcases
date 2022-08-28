import pytest
import requests

def test_div(calculator_service):
    query = {'a':'8', 'b':'2'}
    response = requests.get("http://localhost:80/idiv",query)
    assert(response.status_code == 200)
    assert("result" in response.json())
    assert(response.json()["result"] == 4)