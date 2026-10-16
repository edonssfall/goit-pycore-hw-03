def parse_value(value, type, name):
    try:
        return type(value)
    except Exception:
        raise Exception(f'{name}: {value} have not valid format')
