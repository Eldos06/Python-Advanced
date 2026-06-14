import unittest  # Импортируем фреймворк, без него никуда

from practice15tasks.fucntions import (
calculate_discount,
is_valid_email,
truncate_text,
is_admin,
)

class TestDiscountCalculator(unittest.TestCase):  # Называем класс по-человечески

    def test_calculate_discount_normal(self):  # 1. Тест на обычный, правильный расчет
        # Дано: цена 200, скидка 10%. Ожидаем: 180.0
        result = calculate_discount(200, 10)
        # assertEqual проверяет, что результат равен ожидаемому значению
        self.assertEqual(result, 180.0)

    def test_calculate_discount_zero(self):  # 2. Тест на граничное значение: скидка 0%
        result = calculate_discount(100, 0)
        self.assertEqual(result, 100.0)  # Цена не должна измениться

    def test_calculate_discount_full(self):  # 3. Тест на граничное значение: скидка 100%
        result = calculate_discount(500, 100)
        self.assertEqual(result, 0.0)  # Товар должен стать бесплатным

    def test_calculate_discount_invalid_raises_error(self):  # 4. Твой тест на ошибку
        # Проверяем, что при скидке 120% функция выкинет ValueError
        with self.assertRaises(ValueError):
            calculate_discount(200, 120)


class TestValidateEmail(unittest.TestCase):

    def test_valid_email_success(self):
        # Позитивный сценарий: нормальный рабочий email
        # Используем assertTrue, потому что ожидаем True
        self.assertTrue(is_valid_email("dumanakashov@gmail.com"))

    def test_email_without_at_sign(self):
        # Негативный сценарий: вообще нет знака @
        # Используем assertFalse, потому что функция должна вернуть False
        self.assertFalse(is_valid_email("dumanakashov_gmail.com"))

    def test_email_without_dot_after_at(self):
        # Негативный сценарий: @ есть, но после неё в домене нет точки
        self.assertFalse(is_valid_email("dumanakashov@gmailcom"))

    def test_email_with_dot_before_at_but_not_after(self):
        # Хитрый кейс: точка есть ДО собаки, но НЕТ после собаки
        # Твоя функция должна вернуть False, проверяем это
        self.assertFalse(is_valid_email("duman.akashov@gmailcom"))

    def test_empty_email(self):
        # Проверка пустой строки — одного теста на это БОЛЕЕ чем достаточно
        self.assertFalse(is_valid_email(""))


class TestLimitText(unittest.TestCase):  # Исправил имя класса на нормальный CamelCase!

    def test_limit_text_with_dots(self):
        # Отлично, тут всё правильно. Текст длиннее лимита — режем и шьём три точки
        self.assertEqual(truncate_text("yeldos", 3), "yel...")

    def test_limit_text_without_dots(self):
        # Тоже красавчик. Текст короче лимита — возвращаем как есть
        self.assertEqual(truncate_text("Yeldos Suleimonov", 30), "Yeldos Suleimonov")

    def test_limit_text_exactly_equal(self):
        # Граничный кейс: длина текста РОВНО равна лимиту.
        # "yeldos" — это 6 символов, лимит 6. Должно вернуться "yeldos" БЕЗ точек!
        self.assertEqual(truncate_text("yeldos", 6), "yeldos")

    def test_limit_text_empty_string(self):
        # На бэкенд часто прилетает пустая херня. Надо проверить, что функция не сдохнет
        self.assertEqual(truncate_text("", 5), "")

class TestIsAdmin(unittest.TestCase):

    def test_is_admin_success(self):
        self.assertTrue(is_admin(['teacher', 'admin']))

    def test_is_admin_success_upper(self):
        self.assertTrue(is_admin(['teAcher', 'AdmiN']))

    def test_without_admin(self):
        self.assertFalse(is_admin(['programmer', 'TEACHER', 'Singer']))

    def test_empty_string(self):
        self.assertFalse(is_admin([]))


