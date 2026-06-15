import unittest  # Импортируем фреймворк, без него никуда


from practice15tasks.fucntions import (
calculate_discount,
is_valid_email,
truncate_text,
is_admin,
safe_divide,
rub_to_usd,
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
        # "Yeldos" — это 6 символов, лимит 6. Должно вернуться "yeldos" БЕЗ точек!
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

class TestSafeDivide(unittest.TestCase):  # Имя класса с большой буквы!

    def test_safe_divide_success(self):
        # Обычное деление. Ждем ровно 1.0 (float)
        self.assertEqual(safe_divide(10, 10), 1.0)

    def test_small_number_divide_big_number(self):
        # Исправил твой "smail" на нормальный "small"! 1 делим на 10 = 0.1
        self.assertEqual(safe_divide(1, 10), 0.1)

    def test_zero_division_with_default_value(self):
        # Деление на ноль. По умолчанию функция должна вернуть 0.0
        self.assertEqual(safe_divide(10, 0), 0.0)

    def test_zero_division_with_custom_default(self):
        # А вот этот критически важный кейс ты просрал!
        # Проверяем, что если мы передали свой default=99.0, то функция вернет именно его
        self.assertEqual(safe_divide(10, 0, default=99.0), 99.0)

    def test_both_inputs_are_zero(self):
        # Деление нуля на ноль. Тоже должно вернуть дефолт 0.0
        self.assertEqual(safe_divide(0, 0), 0.0)

class TestRubToUsd(unittest.TestCase):

    def test_rub_to_usd_success(self):
        # Отлично. Проверка обычной конвертации (100 / 50 = 2.0)
        self.assertEqual(rub_to_usd(100.0, 50.0), 2.0)

    def test_rub_to_usd_with_round(self):
        # Отлично. Проверка округления до 2 знаков (100 / 3 = 33.33)
        self.assertEqual(rub_to_usd(100.0, 3.0), 33.33)

    def test_rub_to_usd_value_error_negative_rate(self):
        # Проверка отрицательного курса (rate = -1). Ошибка должна быть!
        with self.assertRaises(ValueError):
            rub_to_usd(100.0, -1.0)

    def test_rub_to_usd_value_error_negative_rub_amount(self):
        # ИСПРАВЛЕНО: Ты передавал 0, а нужно отрицательное число, например -100!
        # Теперь 0 не сломает тест, и вылетит честный ValueError
        with self.assertRaises(ValueError):
            rub_to_usd(-100.0, 100000.0)

    def test_rub_to_usd_value_error_zero_rate(self):
        # Тот самый кейс, из-за которого ты со мной спорил.
        # Курс равен 0, условие rate <= 0 срабатывает, вылетает ValueError.
        with self.assertRaises(ValueError):
            rub_to_usd(100000.0, 0.0)





