import pytest
from models.user import User


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
