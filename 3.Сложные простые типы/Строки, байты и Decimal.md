[[3.Сложные простые типы/MAIN.PY|MAIN]] [[3.Сложные простые типы/Stroki_i_bayty.py.py|Stroki_i_bayty]] [[3.Сложные простые типы/practice_1.py|practice_1]] [[3.Сложные простые типы/practice_2.py|practice_2]] [[3.Сложные простые типы/practice_3.py|practice_3]] [[3.Сложные простые типы/practice_4.py|practice_4]] [[3.Сложные простые типы/practice_5.py|practice_5]] [[3.Сложные простые типы/practice_6.py|practice_6]]

---
tags:
  - python
  - strings
  - bytes
  - encoding
  - decimal
---

# Строки, байты и Decimal

Тема — почему "простые" типы (`str`, `bytes`, `float`) на деле полны нюансов: кодировки при `encode`/`decode`
и потеря точности у `float`, которую решает `Decimal`.

## 1. `Decimal` вместо `float` — [[3.Сложные простые типы/MAIN.PY|MAIN.PY]]

```python
def multi_div(iterations, number, divisor):
    number = Decimal(number)
    for i in range(iterations):
        number /= divisor
    return number
```

Многократное деление гоняется через `Decimal`, а не `float` - `Decimal` хранит число как точную десятичную дробь,
а не двоичное приближение, поэтому не накапливает ошибку округления на повторных операциях.

> [!NOTE] Почему не просто `float`
> `0.1 + 0.2 == 0.30000000000000004` в двоичном `float`. `Decimal("0.1") + Decimal("0.2") == Decimal("0.3")` - точно.

## 2. `str` vs `bytes` — [[3.Сложные простые типы/Stroki_i_bayty.py.py|Stroki_i_bayty.py]]

Файл - "черновик"-эксперименты (в основном закомментированы), показывающий типичные грабли работы с байтами и Юникодом:

```python
print(b'Suleimen' + 'Yeldos')  # TypeError: can't concat str to bytes
```

`str` и `bytes` - разные типы, конкатенация между ними без явного `encode`/`decode` запрещена.

```python
print(b"\xabs".decode())  # UnicodeDecodeError: invalid start byte 0xab (в UTF-8)
details(b"\xde".decode("cp1251"))  # "Ю" - тот же байт в другой кодировке даёт другой символ
```

Один и тот же набор байт превращается в разные символы в зависимости от того, какую кодировку указать при `decode` -
байты сами по себе не знают, в какой кодировке они записаны, это нужно знать заранее (или угадывать).

```python
details("Ю".encode())          # UTF-8: b'\xd0\xae' (2 байта)
details("Ю".encode("cp1251"))  # CP-1251: b'\xde' (1 байт)
details("Ю".encode("utf-16"))  # UTF-16: с BOM, 2 байта на символ + метка порядка байт
```

Один символ в разных кодировках занимает разное число байт - вот почему `len(bytes_obj)` и `len(decoded_str)`
для не-ASCII текста почти всегда отличаются (см. [[3.Сложные простые типы/practice_2.py|practice_2.py]]).

### Обработка ошибок декодирования (`errors=`)

```python
line_bytes.decode("ascii", "replace")         # проблемные байты -> "?"
line_bytes.decode("ascii", "backslashreplace")# проблемные байты -> "\xNN" как текст
line_bytes.decode("ascii", "ignore")          # проблемные байты выбрасываются молча
```

## 3. Практика decode/encode

- [[3.Сложные простые типы/practice_1.py|practice_1.py]] - простой `bytes.decode()` для валидного UTF-8.
- [[3.Сложные простые типы/practice_2.py|practice_2.py]] - `encode("cp1251")` → `decode("cp1251")`, сравнение `len()` байтов и строки.
- [[3.Сложные простые типы/practice_3.py|practice_3.py]] - `safe_decode`: одни и те же "битые" байты (`b"\xff\xfeHello"`) через три разных
  обработчика ошибок (`replace`/`backslashreplace`/`ignore`), результат возвращается кортежем из трёх вариантов.
- [[3.Сложные простые типы/practice_4.py|practice_4.py]] - `encode(..., "backslashreplace")` при кодировании (не только при декодировании).
- [[3.Сложные простые типы/practice_5.py|practice_5.py]] - `is_ascii(s)`: пробует `s.encode("ascii")` и ловит `UnicodeEncodeError`, чтобы определить,
  весь ли текст укладывается в ASCII.
- [[3.Сложные простые типы/practice_6.py|practice_6.py]] - `encode("utf-16")` / `decode("utf-16")` по кругу (round-trip).
