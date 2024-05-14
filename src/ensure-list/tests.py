from main import lambda_handler

def test_is_already_list():
    assert lambda_handler({'parameters': {'data': []}}, None) == []

def test_single_string():
    assert lambda_handler({'parameters': {'data': 'foo'}}, None) == ['foo']

def test_falsy_value():
    assert lambda_handler({'parameters': {'data': ''}}, None) == ['']

def test_list_of_string():
    assert lambda_handler({'parameters': {'data': ['foo']}}, None) == ['foo']
