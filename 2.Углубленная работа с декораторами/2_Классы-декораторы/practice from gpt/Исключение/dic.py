

def get_value(data: dict, key: str):
    if key not in data:
        raise KeyError(f'KeyError: Key not found: {key}')
    return data[key]


try:
    print(get_value({"name": "Baha"}, "hehe"))
except ValueError as e:
    print("Error:", e)
    