[[10_testing/1_unitest/models/user.py|models/user]] [[10_testing/1_unitest/testing/test_models/test_user.py|test_user]] [[10_testing/1_unitest/test_runner.py|test_runner]] [[10_testing/1_unitest/practice15tasks/fucntions.py|practice15tasks/fucntions]] [[10_testing/1_unitest/practice15tasks/testing/test.py|practice15tasks/test]]

---
tags:
  - python
  - testing
  - unittest
---

# `unittest` — основы

Первая тестовая тема: `unittest.TestCase`, фикстуры уровня метода/класса/модуля, ручная сборка `TestSuite` и
свой раннер, плюс большая практика (15 задач) на позитивные/негативные/граничные кейсы.

## 1. Модель под тестом — [[10_testing/1_unitest/models/user.py|models/user.py]]

`User` с `@property` на `password`: геттер отдаёт захэшированное значение, сеттер сразу хэширует
(`hash_password`) при любой записи (в т.ч. в `__init__`), делитер зануляет пароль вместо реального удаления
атрибута. Та же модель, что и в [[10_testing/6_pytest_prametrize/parametrize|6_pytest_prametrize]], только на уровень раньше в курсе.

## 2. `unittest.TestCase` и фикстуры разных уровней — [[10_testing/1_unitest/testing/test_models/test_user.py|test_user.py]]

```python
def setUpModule():     # один раз ДО всех тестов файла
    print("set up (create connection to DB")

def tearDownModule():  # один раз ПОСЛЕ всех тестов файла
    print("tear down (close connection to DB")

class UserTestCase(TestCase):
    def setUp(self):     # перед КАЖДЫМ тестом класса
        self.user = User("username", "ewwq")
    def tearDown(self):  # после КАЖДОГО теста класса
        print("delete user", self.user.username)
```

Три уровня фикстур - модуль (`setUpModule`/`tearDownModule`), класс (`setUpClass`/`tearDownClass`, тут не
используется) и метод (`setUp`/`tearDown`) - выполняются в порядке "снаружи внутрь" и "внутри наружу" при выходе.

### Условный пропуск тестов

```python
@unittest.skip("not ready yet")                                   # пропустить всегда
@unittest.skipIf(sys.platform.startswith("win"), "Does not run on Windows")  # пропустить, ЕСЛИ условие True
@unittest.skipUnless(sys.platform == "darwin", "Run tests for macOS")        # пропустить, ЕСЛИ условие False
```

### Голая функция как тест — `FunctionTestCase`

```python
def test_password_validator_func():
    assert password_validator(pwd, hashed_pwd) is True

pwd_validator_test_case = unittest.FunctionTestCase(testFunc=test_password_validator_func)
```

`unittest` работает с классами `TestCase`, но `FunctionTestCase` умеет обернуть обычную функцию с `assert` внутри,
чтобы её тоже можно было добавить в `TestSuite` наравне с методами класса.

### Ручная сборка `TestSuite`

```python
def user_test_suite():
    main_suite = unittest.TestSuite()
    main_suite.addTest(pwd_validator_test_case)                                   # одиночный FunctionTestCase
    test_loader = unittest.TestLoader()
    main_suite.addTests(test_loader.loadTestsFromTestCase(UserTestCase))          # все тесты класса разом
    main_suite.addTests(test_loader.loadTestsFromTestCase(PasswordValidator))
    return main_suite
```

`TestLoader.loadTestsFromTestCase` рефлексией находит все методы `test_*` в классе и оборачивает каждый в
отдельный тест-кейс - не нужно перечислять их руками.

## 3. Свой раннер — [[10_testing/1_unitest/test_runner.py|test_runner.py]]

```python
runner = unittest.TextTestRunner(verbosity=2)
runner.run(user_test_suite())
```

Альтернатива команде `python -m unittest discover`: явно собрать нужный набор тестов функцией и прогнать его
через `TextTestRunner` - удобно, когда набор тестов должен быть кастомным (не "все файлы `test_*.py`").

## 4. Практика — 15 задач с полным набором тестов

[[10_testing/1_unitest/practice15tasks/fucntions.py|fucntions.py]] - бизнес-логика (скидки, обрезка текста,
валидация email/никнейма/пароля, конвертация валют, пагинация, `Cart`, `SessionManager`, разбор ответа API).
[[10_testing/1_unitest/practice15tasks/testing/test.py|testing/test.py]] - тесты на неё, по классу `unittest.TestCase`
на каждую функцию/класс, с акцентом на три типа кейсов:

```python
def test_calculate_discount_invalid_raises_error(self):   # негативный: ошибка
    with self.assertRaises(ValueError):
        calculate_discount(200, 120)

def test_limit_text_exactly_equal(self):                  # граничный: длина == лимиту
    self.assertEqual(truncate_text("yeldos", 6), "yeldos")

def test_zero_division_with_custom_default(self):         # позитивный: явный default
    self.assertEqual(safe_divide(10, 0, default=99.0), 99.0)
```

`SessionManager`/`Cart` дополнительно проверяются через `setUp` (свежий объект перед каждым тестом) и "заглядывание"
во внутреннее состояние (`self.manager.sessions[token]["username"]`) - не только через публичный API класса.

## Служебные файлы пакета

Пустые файлы-маркеры, превращающие папки в импортируемые пакеты (без них `from models.user import User` не сработал бы):
[[10_testing/1_unitest/models/__init__.py|models/__init__.py]], [[10_testing/1_unitest/testing/__init__.py|testing/__init__.py]],
[[10_testing/1_unitest/testing/test_models/__init__.py|testing/test_models/__init__.py]],
[[10_testing/1_unitest/practice15tasks/testing/__init__.py|practice15tasks/testing/__init__.py]].
