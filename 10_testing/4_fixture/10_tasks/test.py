import pytest

@pytest.fixture()
def default_user():
    return {'username': 'john', 'role': 'user'}

def test_role(default_user):
    assert default_user['role'] == 'user'



