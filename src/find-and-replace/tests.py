from main import lambda_handler, MissingParametersException


def test_happy_path():
    assert lambda_handler({
        'parameters': {
            'needle': 'foobar',
            'haystack': 'foo',
            'replacement': '-'
        }
    }, None) == {'value': '-bar'}


def test_happy_path_with_empty_replacement():
    assert lambda_handler({
        'parameters': {
            'needle': 'foobar',
            'haystack': 'foo',
            'replacement': ''
        }
    }, None) == {'value': 'bar'}


def test_empty_values():
    assert lambda_handler({
        'parameters': {
            'needle': '',
            'haystack': '',
            'replacement': ''
        }
    }, None) == {'value': ''}


def test_missing_params():
    matched = False
    try:
        lambda_handler({
            'parameters': {
                'replacement': ''
            }
        }, None)
    except MissingParametersException as e:
        matched = True
    assert matched
