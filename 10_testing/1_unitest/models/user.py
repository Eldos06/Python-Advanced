import hashlib  # Импортируем библиотеку для работы с криптографическими хэшами


def hash_password(value: str):  # Функция принимает чистый пароль в виде строки
    return hashlib.sha512(value.encode("utf-8")).hexdigest()  # Кодирует строку в байты, считает SHA-512 и возвращает текстовый хэш


def password_validator(pwd, hashed):  # Функция проверки соответствия пароля и хэша
    hashed_pwd = hash_password(pwd)  # Хэширует переданный юзером чистый пароль
    return hashed_pwd == hashed  # Сравнивает свежий хэш с тем, что лежит в базе, возвращает True или False


class User:  # Объявляем класс чертежа нашего пользователя

    def __init__(self, username, password):  # Конструктор объекта, принимает имя и чистый пароль
        self.username = username  # Записывает имя пользователя в обычный атрибут
        self.password = password  # ВНИМАНИЕ: это не просто запись, это вызов сеттера @password.setter ниже!

    @property  # Объявляем геттер для защищенного свойства password
    def password(self):  # Метод срабатывает, когда мы пишем `print(user.password)`
        return self.__password  # Возвращает скрытый хэшированный пароль из приватной переменной

    @password.setter  # Объявляем сеттер, который перехватывает изменение пароля
    def password(self, value):  # Срабатывает при создании юзера или при `user.password = "новое_говно"`
        self.__password = hash_password(value)  # Вызывает нашу функцию хэширования (исправлено дублирование, дебил!)

    @password.deleter  # Объявляем делитер, перехватывающий удаление свойства
    def password(self):  # Срабатывает, когда в коде пишут `del user.password`
        self.__password = None  # Вместо физического удаления переменной просто зануляет её в None