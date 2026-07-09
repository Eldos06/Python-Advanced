[[10_testing/6_pytest_prametrize/testing/test_models/test_user.py|test_user]] [[10_testing/6_pytest_prametrize/models/user.py|user]] [[10_testing/6_pytest_prametrize/pytest.ini|pytest.ini]]

---
tags:
  - python
  - testing
  - pytest
  - parametrize
---

# Pytest Parametrize — конспект

Разбор всех способов параметризации тестов из [[10_testing/6_pytest_prametrize/testing/test_models/test_user.py|test_user.py]]: `@pytest.mark.parametrize`, indirect-параметризация фикстур, параметризованные фикстуры через `params=`, кастомные маркеры, `skip`/`xfail`.

## 1. Обычный `@pytest.mark.parametrize`

Самый простой способ прогнать один тест с разными данными:

```python
@pytest.mark.parametrize(
    "username, email",   # имена аргументов - ОДНА строка, через запятую (а не кортеж!)
    [
        ("john", "john@example.com"),
        pytest.param("sam", "sam@example.com", id="upperToLower"),  # pytest.param(...) дает кейсу свое читаемое id
    ],
)
def test_email(username, email):
    ...
```

> [!WARNING] Частая ошибка
> Если обернуть `argnames` и `argvalues` в одну общую скобку/кортеж - `parametrize((argnames, argvalues))` -
> pytest получит только ОДИН позиционный аргумент вместо двух и упадет с
> `TypeError: ParameterSet._parse_parametrize_args() missing 1 required positional argument: 'argvalues'`
> ещё на этапе сборки тестов (collection error), до запуска.
> Правильно: `parametrize("username, email", [...])` - два отдельных аргумента.

## 2. Indirect-параметризация (`indirect=[...]`)

Когда тесту нужен не голый параметр, а готовый объект, который собирается через фикстуру:

```python
@pytest.fixture()
def user_w_username(request):
    username = request.param       # значение приходит из mark.parametrize, а не из вызова фикстуры напрямую
    return User(username, 'pwd')

@pytest.mark.parametrize(
    "user_w_username, email",
    [("john", "john@example.com"), ("sam", "sam@example.com")],
    indirect=["user_w_username"],  # <- ключевое: это имя не подставляется в тест как строка,
                                   #    а прогоняется через одноименную фикстуру
)
def test_email(self, user_w_username: User, email: str):
    assert user_w_username.email == email
```

Без `indirect` в тест пришла бы строка `"john"`. С `indirect` pytest вызывает фикстуру `user_w_username`,
кладет `"john"` в `request.param` внутри нее, и в тест приходит уже готовый `User`.

Плюс подхода: логика сборки объекта живет в одном месте (фикстуре), а не дублируется в каждом тесте.

## 3. Параметризованная фикстура (`@pytest.fixture(params=[...])`)

Другой способ параметризации - "снизу", через саму фикстуру, без `mark.parametrize` над тестом:

```python
@pytest.fixture(
    params=[
        pytest.param(("nick", "pwd-n"), id="nick"),
        pytest.param(("yeldosik", "pwd"), id="y"),
        pytest.param(("sam", "pwd2"), id="s"),
    ]
)
def user_u(request):
    username, pwd = request.param
    return User(username, pwd)
```

Любой тест, который запросит `user_u` как аргумент, автоматически прогонится 3 раза (по числу элементов `params`) -
даже если сам тест ничем не декорирован. Разница с `indirect`:

| | `mark.parametrize(..., indirect=[...])` | `fixture(params=[...])` |
|---|---|---|
| Где задаются кейсы | над конкретным тестом | в самой фикстуре |
| Кто размножается | только этот тест | **все** тесты, использующие фикстуру |
| Удобно, когда | у разных тестов разные наборы данных | один и тот же набор данных нужен много где |

## 4. Кастомные маркеры

Маркеры регистрируются в [[10_testing/6_pytest_prametrize/pytest.ini|pytest.ini]]:

```ini
markers =
    password_validator: all pwd validator tests
    web_test
    slow: all slow test
```

Без регистрации pytest выдаст `PytestUnknownMarkWarning`. Использование:

```python
@pytest.mark.password_validator
class TestPasswordValidator:
    ...
```

Запуск только помеченных тестов:

```bash
pytest -m password_validator
```

## 5. `skip` и `xfail`

- `@pytest.mark.skip("причина")` - тест безусловно пропускается (аналог `unittest.skip`).
- `@pytest.mark.xfail(reason="...")` - тест **ожидаемо** падает:
  - упал -> `XFAIL`, не считается ошибкой прогона;
  - неожиданно прошел -> `XPASS`, тоже не ошибка, но видно в отчете как повод перепроверить условие.

## 6. Что дальше проверить в [[10_testing/6_pytest_prametrize/models/user.py|user.py]]

- `User.email` - вычисляемое свойство `f"{username.lower()}@example.com"`, на нем и построен `test_email`.
- `password`/`hash_password`/`password_validator` - та же логика хэширования SHA-512, что и в [[10_testing/3_pytest/pytest|3_pytest]].

## Служебные файлы

[[10_testing/6_pytest_prametrize/.coverage|.coverage]], [[10_testing/6_pytest_prametrize/testing/.coverage|testing/.coverage]] -
БД покрытия от `coverage run`/`pytest --cov` (см. [[10_testing/3_pytest/pytest.md|3_pytest]] про сам конфиг).
Пустые файлы-пакеты: [[10_testing/6_pytest_prametrize/models/__init__.py|models/__init__.py]],
[[10_testing/6_pytest_prametrize/testing/__init__.py|testing/__init__.py]],
[[10_testing/6_pytest_prametrize/testing/test_models/__init__.py|testing/test_models/__init__.py]].
