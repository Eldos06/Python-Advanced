import pytest

TODO:""" Задача №7: Фикстура-фабрика (Factory as a Fixture). Иногда в тесте нужно создать 5 разных юзеров с разными именами.
Если фикстура возвращает объект, имя будет всегда одно. Напиши фикстуру, которая возвращает функцию
(лямбду или внутреннюю функцию make_user(name)), чтобы ты мог прямо внутри теста плодить кастомных юзеров."""


#You get one user, always "John". Need 5 users? Stuck! ❌
@pytest.fixture
def user():
    return {"name": "John"}

def test_something(user):
    # Every time, same name: "John"
    assert user["name"] == "John"
    # How to create 5 different users? CAN'T!

# The Solution: Factory Fixture
# Make the fixture return a function that creates users:
@pytest.fixture
def user_factory():
    # This function creates users with ANY name
    def make_user(name):
        return {"name": name, "role": "user"}

    return make_user  # Return the FUNCTION, not the object!
# expected: Created 5 users: {'name': 'Alice', 'role': 'user'}, {'name': 'Bob', 'role': 'user'}, ...
# PASSED [100%]



def test_create_multiple_users(user_factory):
    # NOW you can create 5 different users!
    user1 = user_factory("Alice")
    user2 = user_factory("Bob")
    user3 = user_factory("Charlie")
    user4 = user_factory("Diana")
    user5 = user_factory("Eve")

    assert user1["name"] == "Alice"
    assert user5["name"] == "Eve"
    print(f"Created 5 users: {user1}, {user2}, {user3}, {user4}, {user5}")


@pytest.fixture
def user_factory():
    # Factory function with multiple options
    def make_user(name="guest", role="user", email=None):
        return {
            "name": name,
            "role": role,
            "email": email or f"{name.lower()}@example.com"
        }

    return make_user


def test_different_user_types(user_factory):
    # Create users with different data
    admin_user = user_factory(name="Admin", role="admin")
    regular_user = user_factory(name="John")
    guest_user = user_factory(name="Guest", role="guest")

    assert admin_user["role"] == "admin"
    assert regular_user["name"] == "John"
    assert guest_user["email"] == "guest@example.com"


# Real Example: Creating Test Data
@pytest.fixture
def user_factory():
    """Factory to create test users with custom data"""

    def make_user(name="TestUser", age=25, email=None):
        if email is None:
            email = f"{name.lower()}@test.com"

        return {
            "id": 1,
            "name": name,
            "age": age,
            "email": email,
            "created_at": "2024-01-01"
        }

    return make_user


def test_create_5_users(user_factory):
    # Create 5 different users in ONE test
    users = [
        user_factory("Alice", 25),
        user_factory("Bob", 30),
        user_factory("Charlie", 35),
        user_factory("Diana", 28),
        user_factory("Eve", 32)
    ]

    # Verify each is different
    assert users[0]["name"] == "Alice"
    assert users[1]["name"] == "Bob"
    assert users[4]["age"] == 32
    assert len(users) == 5

    print(f"Created {len(users)} users: {[u['name'] for u in users]}")


def test_create_admin_and_guest(user_factory):
    admin = user_factory("AdminUser")
    guest = user_factory("GuestUser")

    assert admin["email"] == "adminuser@test.com"
    assert guest["email"] == "guestuser@test.com"


@pytest.fixture
def user_factory():
    return lambda name="guest", role="user": {
        "name": name,
        "role": role
    }

# short syntax:
def test_users(user_factory):
    user1 = user_factory("Alice")
    user2 = user_factory("Bob", "admin")
    assert user1["name"] == "Alice"


#With Cleanup (If Factory Creates Real Files)
@pytest.fixture
def user_factory():
    created_users = []  # Track created users

    def make_user(name):
        user = {"name": name, "file": f"/tmp/{name}.txt"}
        # Create actual file
        open(user["file"], "w").write(f"User: {name}")
        created_users.append(user)
        return user

    yield make_user  # Give factory to test

    # Cleanup: delete all created files
    import os
    for user in created_users:
        if os.path.exists(user["file"]):
            os.remove(user["file"])
    print(f"Cleaned up {len(created_users)} users")


def test_create_users_with_files(user_factory):
    user1 = user_factory("Alice")
    user2 = user_factory("Bob")
    user3 = user_factory("Charlie")

    assert len([user1, user2, user3]) == 3

#TODO: Make simple solution Task 7 Solution
@pytest.fixture
def user_factory():
    """Factory fixture to create users with custom names"""

    def make_user(name, role="user"):
        return {
            "id": 1,
            "name": name,
            "role": role,
            "email": f"{name.lower()}@example.com"
        }

    return make_user


# Test it
def test_create_5_different_users(user_factory):
    """Create 5 users with different names"""
    user1 = user_factory("Alice")
    user2 = user_factory("Bob")
    user3 = user_factory("Charlie")
    user4 = user_factory("Diana")
    user5 = user_factory("Eve")

    users = [user1, user2, user3, user4, user5]
    names = [u["name"] for u in users]

    assert names == ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    assert len(users) == 5
    print(f"✅ Created 5 users: {names}")


def test_create_users_with_roles(user_factory):
    """Create users with different roles"""
    admin = user_factory("AdminUser", "admin")
    user = user_factory("RegularUser", "user")
    guest = user_factory("GuestUser", "guest")

    assert admin["role"] == "admin"
    assert user["role"] == "user"
    assert guest["role"] == "guest"