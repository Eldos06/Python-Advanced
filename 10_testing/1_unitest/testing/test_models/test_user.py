import os  # Импортируем модуль ОС для проверки системных переменных
import sys  # Импортируем модуль sys, чтобы узнать, на какой винде или маке мы сидим
import unittest  # Импортируем главный фреймворк тестирования
from unittest import TestCase  # Вытаскиваем конкретно класс TestCase, от которого будем наследоваться

from models.user import (
    User,
    hash_password,
    password_validator,
)  # Импортируем нашу логику из соседней папки models


def setUpModule():  # Функция фикстуры уровня модуля
    print("set up (create connection to DB")  # Запустится ОДИН раз перед вообще всеми тестами в этом файле


def tearDownModule():  # Функция фикстуры уровня модуля
    print("tear down (close connection to DB")  # Запустится ОДИН раз после того, как абсолютно все тесты завершатся


class UserTestCase(TestCase):  # Создаем класс с тестами для модели User

    def setUp(self):  # Фикстура уровня метода
        self.user = User("username", "ewwq")  # Создает свежего юзера ПЕРЕД каждым тестом в этом классе

    def tearDown(self):  # Фикстура уровня метода
        print("delete user", self.user.username)  # Вызывается ПОСЛЕ каждого теста, просто срет в консоль

    def test_del_password(self):  # Тест проверяет deleter пароля
        user = User("Yeldos", "qwerty")  # Создаем локального тест-юзера Елдоса с паролем
        self.assertIsNotNone(user.password)  # Проверяем, что хэш пароля создался и он не равен None
        del user.password  # Дергаем наш делитер через ключевое слово del
        self.assertIsNone(user.password)  # Проверяем, что делитер отработал и внутри теперь реально None


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
        self.assertEqual(os.name, "posix")  # Проверяет системное имя мака (оно тоже posix)


def test_password_validator_func():  # Отдельная голая функция-тест (вне классов)
    pwd = "qwerty"  # Задаем пароль
    hashed_pwd = hash_password(pwd)  # Хэшируем его
    assert (
        password_validator(pwd, hashed_pwd) is True
    )  # Проверяем через чистый питоновский assert, что вернулось True


pwd_validator_test_case = unittest.FunctionTestCase(  # Оборачиваем голую функцию в объект, который понимает unittest
    testFunc=test_password_validator_func  # Передаем ссылку на нашу функцию внутрь конструктора
)


def test_password_validator_suit():  # Функция для создания изолированного набора тестов
    suite = unittest.TestSuite()  # Создаем пустой контейнер (мешок) для тестов
    suite.addTest(pwd_validator_test_case)  # Закидываем в этот мешок наш одиночный FunctionTestCase
    return suite  # Возвращаем готовый мешок наружу


def user_test_suite():  # Главная функция сборки ВСЕХ тестов проекта
    main_suite = unittest.TestSuite()  # Создаем огромный главный мешок для тестов
    main_suite.addTest(pwd_validator_test_case)  # Первым делом суем туда наш кастомный одиночный тест из функции
    test_loader = (
        unittest.TestLoader()
    )  # Создаем автоматический загрузчик, который умеет потрошить классы

    main_suite.addTests(
        test_loader.loadTestsFromTestCase(UserTestCase)
    )  # Находим все тесты в классе UserTestCase и добавляем в главный мешок
    main_suite.addTests(
        test_loader.loadTestsFromTestCase(PasswordValidator)
    )  # Находим все тесты в классе PasswordValidator и тоже докидываем их туда

    return main_suite  # Возвращаем один большой мешок, в котором лежат вообще все тесты модуля