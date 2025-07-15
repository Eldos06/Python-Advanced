bytes_text = "Привет, друг!".encode("cp1251")
# 1. Декодируй как cp1251

print(bytes_text)
print(bytes_text.decode("cp1251"))

# 2. Выведи тип, текст и длину
print(type(bytes_text))
print(type(bytes_text.decode("cp1251")))
print(repr(bytes_text.decode("cp1251")))
print(len(bytes_text))
print(len(bytes_text.decode("cp1251")))
