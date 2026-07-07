[[10_testing/2_coverage/models/user.py|models/user]] [[10_testing/2_coverage/testing/test_models/test_user.py|test_user]]

---
tags:
  - python
  - testing
  - unittest
  - coverage
---

# `coverage.py` поверх `unittest`

Тот же `User` из [[10_testing/1_unitest/Unittest основы.md|1_unitest]], но с двумя изменениями: сеттер пароля
теперь умеет `None`, и тесты параметризуются через `subTest` вместо простого цикла. Тема - измерить, какой процент
кода реально выполняется тестами.

## 1. Отличие модели от предыдущего занятия — [[10_testing/2_coverage/models/user.py|models/user.py]]

```python
@password.setter
def password(self, value):
    if value is not None:
        value = hash_password(value)
    self.__password = value
```

В [[10_testing/1_unitest/Unittest основы.md|1_unitest]] сеттер безусловно звал `hash_password(value)` - передать
`None` туда сломало бы код (`None.encode(...)` не существует). Здесь `None` явно пропускается насквозь, не хэшируясь -
это и позволяет протестировать `del user.password` (который зануляет пароль) без побочных крашей.

## 2. `subTest` — таблица кейсов в одном тесте — [[10_testing/2_coverage/testing/test_models/test_user.py|test_user.py]]

```python
def test_set_password(self):
    passwords = [
        ("qwerty", "0dd3e512..."),
        ("abc", "ddaf35a1..."),
        (None, None),
        ("", "cf83e135..."),
    ]
    for pwd, expected in passwords:
        with self.subTest(pwd=pwd):
            self.user.password = pwd
            self.assertEqual(self.user.password, expected)
```

Без `subTest` первый же неверный кейс в цикле остановил бы весь тест и скрыл бы остальные. С `self.subTest(pwd=pwd)`
каждая итерация цикла считается отдельным под-тестом: если один кейс упадёт, остальные всё равно выполнятся, а
в отчёте будет видно, именно при каком `pwd` был провал - это unittest-аналог `@pytest.mark.parametrize`.

## 3. Как посчитать покрытие

```bash
coverage run -m unittest testing.test_models.test_user
coverage report -m       # таблица: файл, % покрытия, номера непокрытых строк
coverage html             # подробный HTML-отчет по строкам (аналогично pytest --cov, см. 3_pytest)
```

`coverage.py` инструментирует запуск тестов и считает, какие строки `models/user.py` реально выполнились. Например,
без кейса `(None, None)` в `test_set_password` ветка `if value is not None:` (случай `False`) осталась бы
непокрытой - в HTML-отчёте она подсветилась бы как красная строка. Более подробный конфиг (`pytest.ini` с
`addopts = --cov`, `.coveragerc` с `omit=`) разобран в [[10_testing/3_pytest/pytest.md|3_pytest]] - здесь та же идея,
но без интеграции с pytest, чистым `coverage` CLI поверх `unittest`.

## Служебные файлы

Бинарные БД покрытия, которые оставляет после себя `coverage run` ([[10_testing/2_coverage/.coverage|.coverage]] в корне
урока и [[10_testing/2_coverage/testing/.coverage|testing/.coverage]]), и пустые файлы-пакеты
[[10_testing/2_coverage/models/__init__.py|models/__init__.py]], [[10_testing/2_coverage/testing/__init__.py|testing/__init__.py]],
[[10_testing/2_coverage/testing/test_models/__init__.py|testing/test_models/__init__.py]].
