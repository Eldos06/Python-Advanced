import pytest

db = []

@pytest.fixture()
def cleanDB():
    db.clear()
    yield
    db.clear()

# yield — это вежливая уступка. Функция говорит: «Я подготовила окружение, теперь я уступаю место тесту. Братан, выполняйся, а я подожду тебя здесь на паузе. Как закончишь — позови, я приберусь».


def test_add_first(cleanDB):
    db.append('Yeldos')
    assert len(db) == 1
    assert db[0] == 'Yeldos'

def test_add_second(cleanDB):
    db.append('Didara')
    assert len(db) == 1
    assert db[0] == 'Didara'




