[[10_testing/7_pytest_configuration_test/testing/conftest.py|conftest]] [[10_testing/7_pytest_configuration_test/testing/test_fixtures.py|test_fixtures]] [[10_testing/7_pytest_configuration_test/testing/test_models/test_user.py|test_user]] [[10_testing/7_pytest_configuration_test/models/user.py|models/user]] [[10_testing/7_pytest_configuration_test/pytest.ini|pytest.ini]]

---
tags:
  - python
  - testing
  - pytest
  - conftest
---

# `conftest.py` — общие фикстуры без импорта

Главное отличие этого урока от [[10_testing/6_pytest_prametrize/parametrize.md|6_pytest_prametrize]]: фикстуры
`user`, `user_w_username`, `user_u` переехали из `test_user.py` в отдельный [[10_testing/7_pytest_configuration_test/testing/conftest.py|conftest.py]] -
и при этом продолжают работать в тестах без единого `import`.

## 1. Как pytest находит `conftest.py`

```
testing/
├── conftest.py          <- фикстуры отсюда видны ВСЕМ файлам ниже по дереву
├── test_fixtures.py      <- использует author_john и т.д. из своего собственного набора
└── test_models/
    └── test_user.py      <- использует user/user_w_username/user_u из conftest.py, хотя ни разу их не импортирует
```

`conftest.py` - специальное имя файла, которое pytest подхватывает автоматически при сборе тестов: все `@pytest.fixture`,
объявленные внутри, становятся доступны любому тестовому файлу **в этой же папке и во всех вложенных** (здесь -
и `test_fixtures.py`, и `test_models/test_user.py`), без `from conftest import ...`. Это и есть основной механизм
переиспользования фикстур между несколькими тестовыми модулями - в отличие от локальных фикстур урока
[[10_testing/6_pytest_prametrize/parametrize.md|6_pytest_prametrize]], которые были видны только внутри одного файла.

```python
# conftest.py
@pytest.fixture()
def user_w_username(request):
    username = request.param
    return User(username, 'pwd')

@pytest.fixture(params=[...])
def user_u(request): ...

@pytest.fixture()
def user():
    return User('yeldos', 'pwd')
```

[[10_testing/7_pytest_configuration_test/testing/test_models/test_user.py|test_user.py]] использует `user`/`user_w_username`
как параметры тестов ровно так же, как в предыдущем уроке - только теперь эти имена берутся из `conftest.py`, а не
объявлены в том же файле.

## 2. `test_fixtures.py` — граф зависимых фикстур

Мини-модель блога (`Author` → `Post` → `Comment`, датаклассы) и фикстуры, которые зависят друг от друга:

```python
@pytest.fixture()
def author_john():
    return Author(name="john")

@pytest.fixture(scope="class")
def author_sam():
    author = Author(name="sam")
    yield author
    print("delete (teardown)", author)

@pytest.fixture()
def post_1_by_john(author_john: Author):
    post = Post(title="Title 1 by John", author=author_john)
    author_john.posts.append(post)
    return post
```

### Фикстура-фабрика

```python
@pytest.fixture()
def create_post_for_john(author_john: Author):
    def create_post(title: str):
        post = Post(title=title, author=author_john)
        author_john.posts.append(post)
        return post
    return create_post
```

Тот же приём "фикстура возвращает функцию", что и в [[10_testing/4_fixture/Фикстуры pytest.md|4_fixture]] - позволяет
создать в одном тесте сколько угодно постов одного автора (`create_post_for_john("Title 1")`, `create_post_for_john("Title 2")`),
а не один фиксированный объект.

### `autouse=True` — фикстура без явного запроса

```python
@pytest.fixture(autouse=True)
def post_by_sam(author_sam: Author):
    post = Post(title="Some title by Sam", author=author_sam)
    author_sam.posts.append(post)
    return post
```

`autouse=True` заставляет pytest выполнять эту фикстуру для **каждого теста в файле**, даже если тест не принимает
`post_by_sam` как параметр - именно поэтому в `test_fixtures` аргумент `post_by_sam: Post` закомментирован: он
и так создаётся автоматически на фоне.

> [!WARNING] Дублирующиеся определения в файле
> `create_post_for_author(title, author)` и `test_john_posts(...)` в файле объявлены **дважды подряд**, с
> идентичным телом. Python просто молча перезаписывает первое определение вторым - первая версия функции никогда
> не выполняется, второй `test_john_posts` полностью маскирует первый. Похоже на случайно продублированный кусок
> при копировании кода, а не два разных теста.

## 3. `test_models/test_user.py` — фикстура прямо в классе теста

```python
@pytest.mark.password_validator
class TestPasswordValidator:

    @pytest.fixture()
    def user_pwd(self):
        return User("u", "p")

    def test_set_pwd(self, user_pwd: User):
        ...
```

Новое по сравнению с прошлым уроком: `@pytest.fixture()` объявлена **внутри тестового класса**, а не на уровне
модуля/`conftest.py` - такая фикстура видна только тестам этого конкретного класса (`TestPasswordValidator`), а не
всему файлу. Это третий уровень области видимости фикстур, помимо `conftest.py` (весь каталог) и модуля (весь файл).

## Служебные файлы

[[10_testing/7_pytest_configuration_test/pytest.ini|pytest.ini]] - та же конфигурация покрытия и маркеров, что и в
[[10_testing/6_pytest_prametrize/parametrize.md|6_pytest_prametrize]]. [[10_testing/7_pytest_configuration_test/models/user.py|models/user.py]] -
тот же `User` с хэшируемым паролем и вычисляемым `email`.

Пустые файлы-пакеты: [[10_testing/7_pytest_configuration_test/__init__.py|__init__.py]],
[[10_testing/7_pytest_configuration_test/models/__init__.py|models/__init__.py]],
[[10_testing/7_pytest_configuration_test/testing/__init__.py|testing/__init__.py]],
[[10_testing/7_pytest_configuration_test/testing/test_models/__init__.py|testing/test_models/__init__.py]].
БД покрытия: [[10_testing/7_pytest_configuration_test/.coverage|.coverage]],
[[10_testing/7_pytest_configuration_test/testing/.coverage|testing/.coverage]].

> [!NOTE] Про [[10_testing/7_pytest_configuration_test/parametrize.md|parametrize.md]] в этой же папке
> Файл `parametrize.md` рядом с этой заметкой - копия конспекта из [[10_testing/6_pytest_prametrize/parametrize.md|6_pytest_prametrize]]
> (все ссылки в нём указывают на файлы того урока, а не на файлы `7_pytest_configuration_test`). Похоже, папка была
> скопирована как шаблон для нового урока, и старая заметка скопировалась вместе с кодом - вероятно, стоит её удалить
> или переименовать, чтобы не путать с этим конспектом.
