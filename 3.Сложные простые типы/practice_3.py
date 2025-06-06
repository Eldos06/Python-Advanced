import encodings


def safe_decode(b: bytes) -> str:
    """
    Декодирует байты в строку.
    Если ошибка — заменяет проблемные символы.
    """
    return (b.decode("ascii", "replace"),
            b.decode("ascii", "backslashreplace"),
            b.decode("utf-8", "ignore"))
    

bad_bytes = b"\xff\xfeHello"
print(safe_decode(bad_bytes))


# details(line_bytes.decode("ascii", "replace"))
# details(line_bytes.decode("ascii", "backslashreplace"))
# details(line_bytes.decode("ascii", "ignore"))