[[10_testing/4_fixture/test_fixture.py|test_fixture]] [[10_testing/4_fixture/scopeInFixture.py|scopeInFixture]] [[10_testing/4_fixture/testing/test_models/test_user.py|test_user]] [[10_testing/4_fixture/10_tasks/test.py|10_tasks/test]] [[10_testing/4_fixture/10_tasks/CleanUpScope.py|10_tasks/CleanUpScope]] [[10_testing/4_fixture/10_tasks/task3.py|10_tasks/task3]] [[10_testing/4_fixture/10_tasks/task4.py|10_tasks/task4]] [[10_testing/4_fixture/10_tasks/task7.py|10_tasks/task7]]

---
tags:
  - python
  - testing
  - pytest
  - fixtures
---

# Фикстуры pytest

Тема - `@pytest.fixture`: изоляция состояния между тестами, `scope=`, зависимости фикстур друг от друга,
`yield`-фикстуры с teardown, и фикстуры-фабрики.

## 1. Изоляция состояния — [[10_testing/4_fixture/10_tasks/test.py|10_tasks/test.py]]

```python
@pytest.fixture()
def default_user():
    return {'username': 'john', 'role': 'user'}   # выполняется заново для КАЖДОГО теста

def test_modify_role(default_user):
    default_user['role'] = 'admin'
    assert default_user['role'] == 'admin'

def test_role_is_isolated(default_user):
    assert default_user['role'] == 'user'  # изменение из прошлого теста сюда не просочилось
```

Ключевая идея всей темы: фикстура без `scope=` (по умолчанию `scope="function"`) пересоздаётся с нуля перед
каждым тестом - мутация объекта в одном тесте не влияет на другой.

## 2. `scope=` и зависимости фикстур друг от друга — [[10_testing/4_fixture/test_fixture.py|test_fixture.py]]

```python
@pytest.fixture(scope="module")   # создаётся ОДИН раз на весь файл, переиспользуется всеми тестами модуля
def author_john():
    return Author("John")

@pytest.fixture(scope="class")    # один раз на класс тестов
def author_sam():
    author = Author("Sam")
    yield author
    print("delete (teardown)", author)   # teardown - код после yield

@pytest.fixture()                 # scope="function" по умолчанию
def post_1_by_john(author_john: Author):   # фикстура может запрашивать другую фикстуру как аргумент
    post = Post(title="Title 1 by John", author=author_john)
    author_john.posts.append(post)
    return post
```

Цепочка `comment_for_post_1_by_sam` -> зависит от `post_1_by_john` И `author_sam` -> `post_1_by_john` зависит от
`author_john` - pytest сам строит граф зависимостей и создаёт фикстуры в нужном порядке один раз за тест.

> [!NOTE] Иерархия scope: `function` < `class` < `module` < `session`
> Более "широкая" фикстура (`module`) может использоваться внутри более "узкой" (`function`), но не наоборот -
> `function`-скоуп фикстура не может быть зависимостью для `session`-скоуп, потому что её пришлось бы пересоздавать
> посреди жизни родителя.

## 3. `yield`-фикстура: setup / teardown в одной функции — [[10_testing/4_fixture/scopeInFixture.py|scopeInFixture.py]]

```python
@pytest.fixture(scope="module")
def config():
    print("Setup: Loading config")
    yield {"timeout": 30}
    print("Teardown: Saving config")
```

Всё до `yield` - код настройки (выполняется один раз для `module`-скоупа), значение после `yield` - то, что получит
тест, всё после `yield` - гарантированно выполнится после последнего теста, использующего фикстуру (даже если тест упал).

## 4. `10_tasks/` — практика по фикстурам

### Область видимости и уборка ресурсов — [[10_testing/4_fixture/10_tasks/CleanUpScope.py|CleanUpScope.py]]

```python
@pytest.fixture(scope='function')
def cleanUP():
    print("setUP")
    yield 'Didara'
    print("\ncleanUP")
```

и в этом же файле - демонстрация `scope="module"`: три теста (`testFirstTimeNuraim`/`testSecondTimeNuraim`/
`testThirdTimeNuraim`) получают **один и тот же** объект `cleanUPwithMODULE` (setup печатается только один раз
на все три теста, а не три раза, как было бы при `scope="function"`).

### Реальный файл на диске: setup создаёт, teardown удаляет — [[10_testing/4_fixture/10_tasks/task3.py|task3.py]]

```python
@pytest.fixture()
def temp_file():
    fileName = "demo.txt"
    with open(fileName, 'w', encoding='utf-8') as f:
        f.write("Hello from fixture!")
    yield fileName
    if os.path.exists(fileName):
        os.remove(fileName)   # гарантированная уборка после теста, даже если тест упал на assert
```

### Общее мутируемое состояние между тестами — [[10_testing/4_fixture/10_tasks/task4.py|task4.py]]

```python
db = []  # общий список на уровне модуля (не фикстуры!)

@pytest.fixture()
def cleanDB():
    db.clear()   # чистим ДО теста
    yield
    db.clear()   # и ПОСЛЕ теста
```

В отличие от `default_user` из `10_tasks/test.py` (где сама фикстура создаёт новый объект), здесь общий `db` -
это модульная переменная, поэтому фикстура вручную обнуляет её до и после - иначе `test_add_second` увидел бы
элемент, оставленный `test_add_first`.

### Фикстура-фабрика — [[10_testing/4_fixture/10_tasks/task7.py|task7.py]]

Задача: обычная фикстура возвращает **один** готовый объект - если нужно 5 разных юзеров в одном тесте, обычная
фикстура не подходит (она вызывается один раз за тест и с одними и теми же аргументами). Решение - фикстура
возвращает не объект, а **функцию**:

```python
@pytest.fixture
def user_factory():
    def make_user(name, role="user"):
        return {"id": 1, "name": name, "role": role, "email": f"{name.lower()}@example.com"}
    return make_user   # возвращаем ФУНКЦИЮ, а не готовый словарь

def test_create_5_different_users(user_factory):
    users = [user_factory(n) for n in ["Alice", "Bob", "Charlie", "Diana", "Eve"]]
    assert len(users) == 5
```

Тот же приём с `yield` вместо `return` заодно решает и уборку за фабрикой - если `make_user` создаёт реальные
файлы, фикстура копит их в списке `created_users` и удаляет все разом в teardown после `yield make_user`.

## 5. Смешение `unittest.TestCase` и pytest-фикстур в одном файле — [[10_testing/4_fixture/testing/test_models/test_user.py|test_user.py]]

Файл показывает, что `unittest.TestCase`-классы (`UserTestCase`, `PasswordValidator`) и обычные pytest-классы/функции
(`TestPasswordValidator`, `test_password_validator_ok_func`, `TestUser` с фикстурой `user`) спокойно живут в одном
модуле - pytest умеет запускать оба стиля тестов, но `@pytest.fixture` работает только с pytest-style тестами,
методы `TestCase` фикстуры как аргумент принять не могут (у них своя система `setUp`/`tearDown`).

## Модель и конфигурация

[[10_testing/4_fixture/models/user.py|models/user.py]] - тот же `User` с хэшируемым паролем (`hash_password`/`password_validator`),
что и в [[10_testing/2_coverage/Coverage.md|2_coverage]]. [[10_testing/4_fixture/testing/pytest.ini|testing/pytest.ini]] включает
`-s -v` по умолчанию (печатать все `print()` и подробные имена тестов - удобно, чтобы видеть setup/teardown принты фикстур в выводе).

Служебное: [[10_testing/4_fixture/.coverage|.coverage]], [[10_testing/4_fixture/testing/.coverage|testing/.coverage]],
[[10_testing/4_fixture/models/__init__.py|models/__init__.py]], [[10_testing/4_fixture/testing/__init__.py|testing/__init__.py]],
[[10_testing/4_fixture/testing/test_models/__init__.py|testing/test_models/__init__.py]].
