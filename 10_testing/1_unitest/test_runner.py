import unittest  # Импортируем модуль unittest для запуска тестов

from testing.test_models.test_user import (
    user_test_suite,
)  # Из твоего тестового пакета импортируем главную сюиту сборщик

if (
    __name__ == "__main__"
):  # Проверяем, что файл запущен напрямую руками, а не импортирован кем-то
    runner = unittest.TextTestRunner(
        verbosity=2
    )  # Создаем обьект запускатора тестов с детализированным выводом (уровень 2)
    runner.run(
        user_test_suite()
    )  # Запускаем наш огромный мешок тестов, собранный функцией user_test_suite