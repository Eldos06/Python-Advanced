import sys
from typing import List

name = 'Yeldos'
# print(sys.getrefcount(name))

# names = [name, "Dosic"]
# print(sys.getrefcount(name))
# print(sys.getrefcount(names))
# del names
# print(sys.getrefcount(name))

class User:
    def __init__(self, username):
        self.username = username

    def find_user(username):
        print(f"username refs: {sys.getrefcount(username)}")
        user = User(username)
        print(f"user refs: {sys.getrefcount(user)}")
        return user

# user1 = User("Yeldos")
# user1.find_user()

class Node:
    def __init__(self, value, next_value):
        self.value = value
        self.next_value = next_value

node_a = Node('a', None)
print(node_a)
print(sys.getrefcount(node_a))

node_b = Node('b', node_a)
print(sys.getrefcount(node_a))
# print(node_a is node_b.next_value)
print(sys.getrefcount(node_b.next_value))

del node_a
# print(List(node_b.next_value))
print(sys.getrefcount(node_b.next_value))


import gc

print(gc.get_referents(node_b))

def outer_fun(param):
    print("param refs", sys.getrefcount(param))

    some_object = object()
    print("some_object refs:", sys.getrefcount(some_object))

    def inner_fun():
        return object()
    print("inner_fun refs:", sys.getrefcount(inner_fun))

    result = inner_fun()
    print("result refs:", sys.getrefcount(result))
    return result
new_param = object()
outer_fun(new_param)
print(help(gc))
