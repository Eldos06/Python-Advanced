import pytest

@pytest.fixture(scope="module")
def config():
    print("Setup: Loading config")
    yield {"timeout": 30}
    print("Teardown: Saving config")

def test_a(config):
    print(f"Test A: {config}")

def test_b(config):
    print(f"Test B: {config}")

