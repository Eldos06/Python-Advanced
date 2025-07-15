def readFile():
    try:
        # Открываем файл
        with open('C:/Users/Acer Nitro 5/Desktop/myProject/python_test/Academy/Python Advanced/Углубленная работа с декораторами/2_Классы-декораторы/practice from gpt/Исключение/file.txt', 'r', encoding='utf-8') as text_file:
            content = text_file.read()
            if not content:  # Если файл пустой
                raise ValueError("Файл пустой")
            return content
    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден")  # Ошибка если файл не найден
    except ValueError as ve:
        raise ve  # Ошибка, если файл пустой
    except Exception as e:
        raise Exception(f"Неизвестная ошибка: {e}")

# Вызываем функцию и обрабатываем ошибки
try:
    print(readFile())
except Exception as e:
    print(f"Ошибка: {e}")
