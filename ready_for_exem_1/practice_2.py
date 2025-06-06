s = "привет"
b = b"hello"
# Сделай 2 версии: одна с ошибкой, вторая — рабочая
try:
    print(s + b)
except:
    print(f'{s} {b.decode()}')

