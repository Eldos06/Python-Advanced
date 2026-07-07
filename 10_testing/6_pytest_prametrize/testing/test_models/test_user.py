import os  # Импортируем модуль ОС для проверки системных переменных
import sys  # Импортируем модуль sys, чтобы узнать, на какой винде или маке мы сидим
import unittest  # Импортируем главный фреймворк тестирования
from unittest import TestCase

import pytest  # Вытаскиваем конкретно класс TestCase, от которого будем наследоваться

from models.user import (
    User,
    hash_password,
    password_validator,
)  # Импортируем нашу логику из соседней папки models


class UserTestCase(TestCase):  # Создаем класс с тестами для модели User

    def setUp(self):  # Фикстура уровня метода
        self.user = User("username", "ewwq")  # Создает свежего юзера ПЕРЕД каждым тестом в этом классе

    def test_del_password(self):  # Тест проверяет deleter пароля
        user = User("Yeldos", "qwerty")  # Создаем локального тест-юзера Елдоса с паролем
        self.assertIsNotNone(user.password)  # Проверяем, что хэш пароля создался и он не равен None
        del user.password  # Дергаем наш делитер через ключевое слово del
        self.assertIsNone(user.password)  # Проверяем, что делитер отработал и внутри теперь реально None

    def test_set_password(self):
        passwords = [
            ("qwerty", "0dd3e512642c97ca3f747f9a76e374fbda73f9292823c0313be9d78add7cdd8f72235af0c553dd26797e78e1854edee0ae002f8aba074b066dfce1af114e32f8"),
            ("abc", "ddaf35a193617abacc417349ae20413112e6fa4e89a97ea20a9eeee64b55d39a2192992a274fc1a836ba3c23a3feebbd454d4423643ce80e2a9ac94fa54ca49f"),
            (None, None),
            ("", "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e"),
        ]
        for pwd, expected in passwords:
            with self.subTest(pwd=pwd):
                self.user.password = pwd
                self.assertEqual(self.user.password, expected)


class PasswordValidator(TestCase):  # Класс с тестами для функций валидации (без лишних пустых setUp/tearDown!)

    def test_password_validator_ok(self):  # Тест успешной валидации
        pwd = "qwerty"  # Задаем чистый тестовый пароль
        hashed_pwd = hash_password(pwd)  # Генерируем для него правильный хэш
        self.assertTrue(
            password_validator(pwd, hashed_pwd)
        )  # Проверяем, что валидатор вернул True (исправил твой косяк с assertIsNotNone)

    def test_password_validator_doesnt_match(self):  # Тест на несовпадение паролей
        pwd = "qwerty"  # Задаем тестовый пароль
        self.assertFalse(
            password_validator(pwd, pwd)
        )  # Проверяем, что если сунуть вместо хэша чистую строку, валидатор вернет False

    @unittest.skip("not ready yet")  # Декоратор безусловного пропуска теста
    def test_fails(self):  # Сам тест
        assert False  # Этот бред никогда не выполнится, потому что тест скипнут

    @unittest.skipIf(
        sys.platform.startswith("win"), "Does not run on Windows"
    )  # Пропустить, ЕСЛИ это Винда
    def test_all_but_windows(self):  # Тест для Линукса и Мака
        self.assertIn("ix", os.name)  # Проверяет, что операционка относится к семейству POSIX (ко ко ко, винда мимо)

    @unittest.skipUnless(
        sys.platform == "darwin", "Run tests for macOS"
    )  # Пропустить ВСЕГДА, ЕСЛИ ТОЛЬКО это не Мак
    def test_for_mac(self):  # Тест чисто под макось
        self.assertEqual(os.name, "posix")  # Проверяет системное имя мака (оно тоже posix)s

#First version
# Фикстура для "непрямой" (indirect) параметризации: сама по себе params не задает,
# значение приходит извне — из pytest.mark.parametrize(..., indirect=["user_w_username"])
@pytest.fixture()
def user_w_username(request):
    username = request.param  # request.param - это то значение, что pytest.mark.parametrize передал для этого кейса
    return User(username, 'pwd')  # фикстура отдает в тест уже готового User, а не голую строку username

# #Second version
# Альтернативный вариант той же идеи: не создаем нового юзера с нуля,
# а переиспользуем фикстуру user() и просто подменяем ей username на лету
# @pytest.fixture()
# def user_w_username(request, user):
#     username = request.param
#     user.username = username
#     return user

# Фикстура, параметризованная "изнутри" через params= .
# pytest сам размножит КАЖДЫЙ тест, который запросит user_u, на 3 прогона (по числу элементов params) -
# отдельный pytest.mark.parametrize над тестом для этого не нужен
@pytest.fixture(
    params=[
        pytest.param(("nick", "pwd-n"), id="nick"),  # id задает читаемое имя кейса в выводе pytest вместо автогенерируемого
        pytest.param(("yeldosik", "pwd"), id='y'),
        pytest.param(("sam", "pwd2"), id='s'),
    ]
)
def user_u(request):
    username, pwd = request.param  # request.param - текущий элемент params для этого конкретного прогона
    return User(username, pwd)

@pytest.fixture()
def user():
    return User('yeldos', 'pwd')  # простая непараметризованная фикстура - один готовый юзер по умолчанию


class TestUser:  # Класс тестов в стиле pytest (без наследования от TestCase)
    def test_del_password(self, user: User):  # user подставляется автоматически по имени фикстуры
        assert user.password is not None
        del user.password
        assert user.password is None

    @pytest.mark.parametrize(
            "user_w_username, email",  # имена аргументов теста перечисляем одной строкой через запятую
            [
                ("john", "john@example.com"),
                ("john", "john@example.com"),  # дубликат кейса специально - pytest не проверяет кейсы на уникальность
                pytest.param("sam", "sam@example.com", id="upperToLower")  # свой id вместо автосгенерированного "sam-sam@example.com"
            ],
            indirect=["user_w_username"],  # ключевой момент: "john"/"sam" не подставляются в тест напрямую,
            # а сначала проходят через фикстуру user_w_username как request.param
    )
    def test_email(self, user: User, user_w_username: str, email: str):
        assert user_w_username.email == email  # тут user_w_username - уже готовый объект User, а не строка


@pytest.mark.password_validator  # кастомный маркер, зарегистрирован в pytest.ini - можно запускать выборочно: pytest -m password_validator
class TestPasswordValidator:
    def test_password_validator(self):
        pwd = "qwerty"
        hashed_pwd = hash_password(pwd)
        assert password_validator(pwd, hashed_pwd) is True

    @pytest.mark.skip("not ready yet")  # pytest-аналог unittest.skip - тест безусловно пропускается
    def test_skip(self):
        1 / 0

    @pytest.mark.xfail(reason="a fifty fifty change")  # тест, от которого ЗАРАНЕЕ ожидаем провал:
    # упал -> XFAIL (не считается ошибкой прогона), неожиданно прошел -> XPASS (тоже не ошибка, но заметно в отчете)
    def test_fails(self):
        assert True

@pytest.mark.password_validator
def test_password_validator_ok_func():
    pwd = "qwerty"
    hashed_pwd = hash_password(pwd)
    assert password_validator(pwd, hashed_pwd) is True

