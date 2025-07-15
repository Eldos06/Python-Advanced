

# def details(name):
#     print()
#     print(name)
#     print(f"repr: {repr(name)}")
#     print(f"type: {type(name)}")
#     print(f"len: {len(name)}")
#     print()
#     return

# details("Yeldos")
# details(b"Yeldos")

# details(b"Yeldos".decode())
# print(b'Suleimen' + 'Yeldos') #TypeError: can't concat str to bytes
# print(b'Suleimen '.decode() + 'Yeldos') #Suleimen Yeldos
# print(b"\xabs")
# print(b"\xabs".decode()) #UnicodeDecodeError: 'utf-8' codec can't decode byte 0xab in position 0: invalid start byte
# details(b'\xc2\xb1')
# details(b'\xc2\xb1'.decode())
# details(b'\xde'.decode("cp1251")) #Ю
# details("Ю".encode())
# details("Ю".encode("cp1251"))
# details("Ю".encode("utf-16"))
# details(u"\u042e")
# details("\u042e")

# line = "Hello, СУКА!"
# line_bytes = line.encode("utf-8")
# details(line.encode("utf-8"))
# details(line_bytes.decode("utf-8"))
# details(line_bytes.decode("ascii", "replace"))
# details(line_bytes.decode("ascii", "backslashreplace"))
# details(line_bytes.decode("ascii", "ignore"))
# details(line.decode("utf-8"))






