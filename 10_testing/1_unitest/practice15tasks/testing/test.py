import unittest  # Импортируем фреймворк, без него никуда


from practice15tasks.discountCalculator import calculate_discount


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
            calculate_discount(100, 150)