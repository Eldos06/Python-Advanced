from typing import TypeVar, Any

AddParam = TypeVar('AddParam', float, str, list[Any])

def hello(name: str) -> str:
    line = f"Hi, {name}!"
    return line

def add(a: AddParam, b: AddParam) -> AddParam:
    return a + b

def repeat_item(item: AddParam, n: int) -> list[AddParam]:
    return [item] * n

print(hello("Yeldos"))
# print(hello(2341))
# print(hello(b'dwin'))
print(add(1, 2))
print(add(4.5, 4.2))
print(add('sdf', 'weqr'))
print(add(['qwerty'], ['sdfa']))
print(repeat_item(add(1, 2), 3))
items = repeat_item('string', 3)
print(items)
items.append('qwerty')
# items.append(12345)
print(items)
