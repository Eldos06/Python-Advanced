from typing import TypeVar, overload, Any, Generic

# 1. Создаем TypeVar для ЭЛЕМЕНТА контейнера, ограничив его str и int
E = TypeVar('E', int, str)

# 2. Используем @overload, чтобы связать входной list с выходным list
@overload
def reverse_container(container: list[E]) -> list[E]:
    ...

# Используем @overload для tuple
@overload
def reverse_container(container: tuple[E, ...]) -> tuple[E, ...]:
    ...

# Реальное тело функции (Mypy не проверяет типы строго внутри реализации с overload,
# он ориентируется на сигнатуры выше)
def reverse_container(container: Any) -> Any:
    return container[::-1]  # Срез [::-1] идеально сохраняет тип контейнера

# 3. Проверка тестами для Mypy:
res_list = reverse_container([1, 2, 3])       # Mypy понимает, что это list[int]
res_tuple = reverse_container(("a", "b", "c")) # Mypy понимает, что это tuple[str]

# print(res_list)
# print(res_tuple)

# Если раскомментировать строку ниже:
# print(reverse_container([1.1, 2.2]))
# Mypy выдаст: Value of type variable "E" of "reverse_container" cannot be "float"
T = TypeVar('T', bound= str | int )
class Box(Generic[T]):
    all_items: list[T] = []
    def __init__(self, item: T) -> None:
        self.item = item


    def add_item(self, item: T) -> None:
        self.all_items.append(item)

    def get_all_items(self) -> list[T]:
        return self.all_items

id_box = Box[int|str]("sdkf")

id_box.add_item(1024)
id_box.add_item("ART-99") # Mypy ДОЛЖЕН выдать ошибку: ожидается int, передана str