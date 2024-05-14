import logging

logger = logging.getLogger()


class InvalidDataException(Exception): pass


def lambda_handler(event, context):
    parameters = event["parameters"]

    data = parameters["data"]
    collapse_root_list = parameters.get('collapse_root_list', False)
    if collapse_root_list:
        logger.info('Collapsing root list...')

        data = [item for row in data for item in row]

    output = {}
    for item in data:
        if not isinstance(item, dict) or len(item.keys()) > 1:
            raise InvalidDataException(
                f"Invalid input type of item ({type(item)}), must be a list of dicts with a single key per dict")
        for entry_key in item.keys():
            if entry_key in output:
                raise InvalidDataException(f"Duplicate key ({entry_key}) in data")
        output.update(**item)
    return output
