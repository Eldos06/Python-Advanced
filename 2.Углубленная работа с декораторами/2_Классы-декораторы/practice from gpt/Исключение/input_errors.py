# def sales():
#     try:
#         price = int(input("Enter price trau mat: "))  # Получаем цену как int сразу
#         if price < 0:
#             raise ValueError("СУКА ты достал меня, как цена можеть быть минус ДУРДОМ")
#         return price
#     except ValueError as e:
#         raise ValueError(f"БЯЯТЬ КОЖАНЫЙ ЦИФРЫ ПИШИ ЖИ ШИ КАК В КАЙФ ПИШИ: {e}")

# try:
#     print(sales())
# except ValueError as e:
#     print(f"ЁБ ТВОЮ МАТЬ, ОШИБКА: {e}")

import time
import random
class ConnectionError(Exception):
    pass

def connect_to_server():
    # Просто для примера — имитируем соединение
    response = random.choice(["SUCCESS", "FAIL"])
    print(f"Server response: {response}")
    if response == "FAIL":
        raise ConnectionError("Не удалось подключиться к серверу")

def try_connect(max_retries=3):
    for attempt in range(1, max_retries + 1):
        try:
            connect_to_server()  # Пытаемся подключиться
            print("Успешно подключились к серверу!")
            return  # Если подключились, выходим из функции
        except ConnectionError as e:
            print(f"Попытка #{attempt} не удалась: {e}")
            if attempt == max_retries:
                print("ВСЁ, НАХУЙ, В ЛЕС С ЭТИМ СЕРВЕРОМ")
                raise e
            time.sleep(1)  # Подождать перед повторной попыткой

try:
    try_connect()
except ConnectionError as e:
    print(f"Ошибка подключения: {e}")
