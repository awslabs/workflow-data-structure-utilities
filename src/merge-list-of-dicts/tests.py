from main import lambda_handler, InvalidDataException


def test_valid_params_lambda_handler():
    event = {
        "parameters": {
            "data": [{"a": "b"}, {"c": "d"}]
        }
    }
    response = lambda_handler(event, None)
    assert response == {"a": "b", "c": "d"}


def test_collapse_root_dict():
    event = {
        "parameters": {
            "data": [[{"a": "b"}], [{"c": "d"}]],
            "collapse_root_list": True
        }
    }
    response = lambda_handler(event, None)
    assert response == {"a": "b", "c": "d"}


def _check_exc(data, exc_type):
    matched = False
    try:
        lambda_handler(data, None)
    except exc_type:
        matched = True
    assert matched, 'Exception was not triggered'


def test_mixed_root_dict():
    _check_exc({
        "parameters": {
            "data": [[{"a": "b"}], {"c": "d"}],
            "collapse_root_list": True
        }
    }, InvalidDataException)


def test_empty_parameters():
    _check_exc({
        "parameters": {
        }
    }, KeyError)


def test_null_data():
    _check_exc({
        "parameters": {
            "data": None
        }
    }, TypeError)
