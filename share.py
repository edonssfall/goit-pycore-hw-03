def parse_value(value, type, name):
    try:
        return type(value)
    except Exception:
        raise Exception(f'Error: {name} have not valid format')
