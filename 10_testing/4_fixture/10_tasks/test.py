import tempfile

import pytest

@pytest.fixture()
def default_user():
    # Каждый раз, когда тест просит эту фикстуру, pytest выполняет этот код заново
    return {'username': 'john', 'role': 'user'}


def test_modify_role(default_user):
    # Изменяем роль прямо в тесте
    default_user['role'] = 'admin'
    # Проверяем, что в рамках ЭТОГО теста роль действительно изменилась
    assert default_user['role'] == 'admin'


def test_role_is_isolated(default_user):
    # Магия! Несмотря на то, что предыдущий тест изменил словарь,
    # этот тест получает АБСОЛЮТНО НОВУЮ, чистую копию от фикстуры.
    print(default_user)
    assert default_user['role'] == 'user'




