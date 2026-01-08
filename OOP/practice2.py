# import math
#
# class Point:
#     def move(self, x ,y):
#         self.x = x
#         self.y = y
#     def reset(self):
#         self.move(0, 0)
#     def calculate_distance(self, other_point):
#         return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
#
# point1 = Point()
# point2 = Point()
# point1.reset()
# point2.move(5, 0)
# print(point2.calculate_distance(point1))
# assert point2.calculate_distance(point1) == point1.calculate_distance(point2)
#
# point1.move(2, 6)
# print(point1.calculate_distance(point2))
# print(point1.calculate_distance(point1))


# class Point:
#     def __init__(self, x, y):
#         # При создании точки сразу вызываем метод move
#         self.move(x, y)
#
#     def move(self, x, y):
#         # Меняем координаты точки
#         self.x = x
#         self.y = y
#
#     def reset(self):
#         # Сброс в начало координат
#         self.move(0, 0)
#
# # Создаём точку с координатами (3, 5)
# point = Point(3, 5)
#
# # Выводим координаты
# print(point.x, point.y)

# Определяем пустой класс Point
# class Point:
#     pass
#
# # Создаём два объекта (экземпляра класса)
# p1 = Point()
# p2 = Point()
#
# # Задаём координаты для первой точки
# p1.x = 5
# p1.y = 4
#
# # Задаём координаты для второй точки
# p2.x = 3
# p2.y = 6
#
# # Выводим координаты первой точки
# print(p1.x, p1.y)   # 5 4
#
# # Выводим координаты второй точки
# print(p2.x, p2.y)   # 3 6


import datetime

# Храним следующий доступный id для всех новых заметок
last_id = 0


class Note:
    """Представляет заметку в блокноте."""

    def __init__(self, memo, tags=""):
        """Создать заметку с текстом и тегами (по умолчанию пусто)."""
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()

        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """Вернуть True, если filter содержится в memo или в tags."""
        return filter in self.memo or filter in self.tags


class Notebook:
    """Коллекция заметок: можно добавлять, изменять и искать."""

    def __init__(self):
        """Создать пустой список заметок."""
        self.notes = []

    def new_note(self, memo, tags=""):
        """Создать новую заметку и добавить её в блокнот."""
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        """Изменить текст (memo) у заметки по её id."""
        for note in self.notes:
            if note.id == note_id:
                note.memo = memo
                break

    def modify_tags(self, note_id, tags):
        """Изменить теги у заметки по её id."""
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break

    def search(self, filter):
        """Найти все заметки, где filter встречается в тексте или тегах."""
        return [note for note in self.notes if note.match(filter)]


# ----- Пример использования -----
notebook = Notebook()
notebook.new_note("Buy milk and eggs", "shopping food")
notebook.new_note("Finish Python project", "coding study")

# Поиск
results = notebook.search("Python")
for note in results:
    print(f"[{note.id}] {note.memo} ({note.tags})")

# Изменение заметки
notebook.modify_memo(1, "Buy milk, eggs and bread")
notebook.modify_tags(2, "python coding homework")

print("\nВсе заметки после изменений:")
for note in notebook.notes:
    print(f"[{note.id}] {note.memo} ({note.tags})")




