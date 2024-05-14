def lambda_handler(event, context):
    parameters = event['parameters']

    data = parameters['data']

    if isinstance(data, list):
        return data
    return [data]