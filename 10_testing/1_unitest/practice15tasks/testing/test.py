import unittest  # Импортируем фреймворк, без него никуда



from practice15tasks.fucntions import *


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

class TestCheckNickname(unittest.TestCase):  # Название класса по PEP 8

    def test_nickname_success(self):
        # Позитивный кейс: обычный чистый никнейм. Должен вернуть True
        self.assertTrue(check_nickname("yeldos"))

    def test_nickname_with_bad_word_inside(self):
        # Негативный кейс: плохое слово спрятано внутри. Должен вернуть False
        self.assertFalse(check_nickname("vipecodinggavno"))

    def test_nickname_empty_string(self):
        # ИСПРАВЛЕНО: Пустая строка не содержит мата, поэтому функция вернет True!
        # Мы тестируем логику функции, а не наши фантазии
        self.assertTrue(check_nickname(""))

    def test_nickname_bad_word_upper_case(self):
        # ИСПРАВЛЕНО: Вот это реальная проверка верхнего регистра!
        # Слово "ADMIN" написано капсом, но функция должна его поймать и вернуть False
        self.assertFalse(check_nickname("SUPER_ADMIN_99"))

    def test_nickname_bad_word_embedded(self):
        # Дополнительный крутой кейс: запрещенное слово зажато между другими буквами
        self.assertFalse(check_nickname("123root456"))


class TestCart(unittest.TestCase):

    def setUp(self):
        # Этот метод вызывается ПЕРЕД КАЖДЫМ тестом.
        # У каждого теста будет своя чистая, пустая корзина!
        self.cart = Cart()

    def test_cart_add_single_item_success(self):
        # Позитивный кейс: добавили один товар, проверили сумму
        self.cart.add_item("Apple", price=10.0, quantity=2)
        self.assertEqual(self.cart.get_total(), 20.0)

    def test_cart_add_multiple_items_success(self):
        # Проверяем добавление РАЗНЫХ товаров
        self.cart.add_item("Apple", price=10.0, quantity=2)  # +20.0
        self.cart.add_item("Banana", price=15.0, quantity=1)  # +15.0
        self.assertEqual(self.cart.get_total(), 35.0)

    def test_cart_increase_quantity_of_same_item(self):
        # ИСПРАВЛЕНО: Вот так проверяется "изменение количества" и дублирование!
        # Сначала добавляем 2 яблока по 10 (сумма 20)
        self.cart.add_item("Apple", price=10.0, quantity=2)
        # Потом добавляем туда же ЕЩЁ 3 яблока по той же цене (сумма должна стать 50)
        self.cart.add_item("Apple", price=10.0, quantity=3)

        # Проверяем общую стоимость в корзине
        self.assertEqual(self.cart.get_total(), 50.0)

    def test_cart_add_item_invalid_quantity_raises_error(self):
        # Отлично, проверка ошибки на нулевое количество
        with self.assertRaises(ValueError):
            self.cart.add_item("Banana", price=100.0, quantity=0)

    def test_cart_add_item_invalid_price_raises_error(self):
        # Дополнительно проверим отрицательную цену, функция ведь тоже должна упасть
        with self.assertRaises(ValueError):
            self.cart.add_item("Orange", price=-5.0, quantity=1)


class TestSessionManager(unittest.TestCase):

    def setUp(self):
        # Перед каждым тестом создаем изолированный менеджер сессий
        self.manager = SessionManager()

    def test_session_is_active_success(self):
        # Позитивный кейс: создаем живую сессию на 60 секунд
        token = "token_123"
        username = "yeldos"

        self.manager.create_session(token, username, duration_sec=60)

        # Проверяем, что сессия активна
        self.assertTrue(self.manager.is_active(token))

        # МИДЛ-ПРОВЕРКА: заглядываем внутрь структуры и проверяем, что юзер записался корректно!
        self.assertEqual(self.manager.sessions[token]["username"], username)

    def test_session_not_found(self):
        # Негативный кейс: проверяем токен, которого никогда не существовало
        self.assertFalse(self.manager.is_active("non_existent_token"))

    def test_session_expired(self):
        # Негативный кейс: создаем сессию, которая протухла 10 секунд назад
        token = "expired_token"
        self.manager.create_session(token, "user_test", duration_sec=-10)

        # Проверяем, что менеджер видит её мертвой
        self.assertFalse(self.manager.is_active(token))

class TestParse(unittest.TestCase):

    def test_parse_success(self):
        api_response = {"response": {"user": {"id": 42, "balance": "150.00"}}}

        result = parse_user_balance(api_response)

        expected_result = {"user_id": 42, "balance": 150.00}

        self.assertEqual(result, expected_result)

    def test_parse_failure(self):
        invalid_response = {"response": {"user": {"number": 42, "cash": "150.50"}}}

        with self.assertRaises(KeyError):
            parse_user_balance(invalid_response)

class TestGetPage(unittest.TestCase):
    def setUp(self):
        self.items = ["A", "B", "C", "D", "E"]

    def test_page_success(self):
        self.assertListEqual(get_page_items(self.items, 1, 2), ["A", "B"])

    def test_page_success_mid(self):
        self.assertListEqual(get_page_items(self.items, 2, 3), ["D", "E"])

    def test_page_out_of_bounds(self):
        self.assertListEqual(get_page_items(self.items, 10, 2), [])

    def test_invalid_page_zero(self):
        self.assertListEqual(get_page_items(self.items, 0, 2), [])




