class MissingParametersException(Exception): pass


def lambda_handler(event, context):
    parameters = event['parameters']
    try:
        fields = {k: parameters[k] for k in ['needle', 'haystack', 'replacement']}
    except KeyError as e:
        raise MissingParametersException(f'Could not find field: {e}')

    return {
        'value': fields['needle'].replace(fields['haystack'], fields['replacement'])
    }
