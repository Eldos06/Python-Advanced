import os
import pytest

@pytest.fixture()
def temp_file():
    # 1. СТАРТ (setUp): Создаем реальный файл на диске
    fileName = "demo.txt"
    with open(fileName, 'w', encoding='utf-8') as f:
        f.write("Hello from fixture!")

    # 2. ПЕРЕДАЧА: Отдаем ИМЯ файла в тест
    yield fileName

    # 3. УБОРКА (tearDown): Этот код выполнится строго после теста
    if os.path.exists(fileName):
        os.remove(fileName)
        print(f"\n [Фикстура] Файл {fileName} успешно удален с диска!")


# А вот так мы этот файл используем в тесте
def test_read_temp_file(temp_file):
    # temp_file — это строка "demo.txt"
    assert os.path.exists(temp_file)

    with open(temp_file, "r", encoding="utf-8") as f:
        content = f.read()

    assert content == "Hello from fixture!"



