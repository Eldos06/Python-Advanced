import unittest  # Импортируем фреймворк, без него никуда


from practice15tasks.discountCalculator import calculate_discount
from practice15tasks.validateEmail import is_valid_email

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




