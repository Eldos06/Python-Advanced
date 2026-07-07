[[SQL/lecture_1.sql|lecture_1]] [[SQL/SQLAlchemy 2.0/LAB 1.sql|LAB 1]] [[SQL/SQLAlchemy 2.0/config.py|config]] [[SQL/SQLAlchemy 2.0/main.py|main]]

---
tags:
  - sql
  - sqlalchemy
  - orm
---

# SQL (T-SQL) и SQLAlchemy 2.0

От сырого T-SQL с многотабличными `JOIN`'ами (учебная схема "University") к декларативному ORM SQLAlchemy 2.0.

## 1. T-SQL основы — [[SQL/lecture_1.sql|lecture_1.sql]]

```sql
USE UNIVERSITY;
GO

SELECT * FROM tblSTUDENT
WHERE StudentBirth > DateAdd(Year, -75, GetDate())   -- студенты младше 75 лет ("сегодня минус 75 лет")

SELECT GETDATE()   -- текущая дата/время на сервере
```

`DateAdd(unit, amount, date)` и `GetDate()` - функции работы с датами в диалекте T-SQL (MS SQL Server), а не
стандартного ANSI SQL (в PostgreSQL это были бы `CURRENT_DATE - INTERVAL '75 years'`).

Закомментированный запрос выше показывает классический паттерн многотабличного отчёта:

```sql
SELECT S.StudentID, S.StudentFname, S.StudentLname, SUM(CR.Credits) AS Rex
FROM tblSTUDENT S
JOIN tblCLASS_LIST CL ON S.StudentID = CL.StudentID
JOIN tblCLASS CS ON CL.ClassID = CS.ClassID
...
WHERE Q.QuarterName = 'Spring' AND D.DeptName LIKE 'Math%' AND CS.Year >= 1996
GROUP BY S.StudentID, S.StudentFname, S.StudentLname
HAVING SUM(CR.Credits) > 10      -- фильтр ПОСЛЕ агрегации (WHERE тут работать не может - Rex ещё не посчитан)
ORDER BY Rex DESC;
```

> [!NOTE] `WHERE` vs `HAVING`
> `WHERE` фильтрует строки ДО `GROUP BY` (работает со значениями отдельных строк). `HAVING` фильтрует ПОСЛЕ
> агрегации, поэтому только в `HAVING` можно написать условие на результат `SUM()`/`COUNT()`/`AVG()`.

## 2. Практика многотабличных `JOIN` — [[SQL/SQLAlchemy 2.0/LAB 1.sql|LAB 1.sql]]

Семь отчётных запросов над той же схемой "University" (`tblSTUDENT`, `tblCLASS`, `tblCOURSE`, `tblINSTRUCTOR`,
`tblDORMROOM`, `tblBUILDING` и т.д.), с растущей сложностью цепочки `JOIN`. Повторяющиеся паттерны:

```sql
WHERE T.InstructorState IN ('Michigan, MI', 'Wisconsin, WI')   -- IN вместо цепочки OR
      AND C.[YEAR] BETWEEN 1930 AND 1939                       -- [Year] в квадратных скобках - Year зарезервированное слово в T-SQL
      AND CR.ClassroomTypeName = 'small lecture hall'
      AND CO.CourseName LIKE 'PHYS%'                            -- LIKE с % для префиксного поиска
```

Задача 7 - самая длинная цепочка (8 `JOIN`), чтобы дойти от студента до конкретного дня недели занятия
(`tblSCHEDULE` -> `tblSCHEDULE_DAY` -> `tblDAY`) - типичный пример "путешествия" по нормализованной схеме БД от
одной сущности до другой через промежуточные связывающие таблицы.

## 3. SQLAlchemy 2.0: декларативные модели — [[SQL/SQLAlchemy 2.0/config.py|config.py]] + [[SQL/SQLAlchemy 2.0/main.py|main.py]]

```python
BASE_DIR = Path(__file__).parent
DB_URL = f"sqlite:///{BASE_DIR}/db.sqlite3"
DB_ECHO = True   # печатать в консоль каждый сгенерированный SQL-запрос - удобно для обучения/отладки
```

```python
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)
    email: Mapped[str]
    motto: Mapped[str | None]   # | None делает колонку NULLABLE - без этого SQLAlchemy считает поле NOT NULL

engine = create_engine(url=config.DB_URL, echo=config.DB_ECHO)
Base.metadata.create_all(engine)   # генерирует и выполняет CREATE TABLE для всех классов-моделей
```

Современный синтаксис SQLAlchemy 2.0 (`Mapped[...]`/`mapped_column`) выводит SQL-тип колонки из аннотации типа
Python - `Mapped[str]` даёт `NOT NULL`-колонку, `Mapped[str | None]` - `NULL`-колонку, без ручного указания
`nullable=True/False`, как в SQLAlchemy 1.x. `Base.metadata.create_all(engine)` - ORM-эквивалент ручного
`CREATE TABLE users (...)`, который иначе пришлось бы писать SQL-запросом вручную, как в [[SQL/lecture_1.sql|lecture_1.sql]].

## Служебные файлы

[[SQL/SQLAlchemy 2.0/db.sqlite3|db.sqlite3]] - файл базы данных, который создаёт (или дополняет) `main.py` при запуске
через `Base.metadata.create_all(engine)`. [[SQL/SQLAlchemy 2.0/queries.sql|queries.sql]] - пустой файл-заготовка для
ручных SQL-запросов к этой базе.
