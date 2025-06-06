def detect_days(numbers):
    number = {
        0: "н л",
        1: "к г",
        2: "б ц х",
        3: "т з",
        4: "ч р",
        5: "п қ",
        6: "ж ш щ",
        7: "с м",
        8: "в ф",
        9: "д ғ"
    }
    return number.get(numbers)

while True:
    user_input = input("Enter your number (or 'exit' to stop): ")
    
    if user_input.lower() == 'exit':
        break
    
    if not user_input.isdigit():
        print("Please enter digits only.")
        continue
    
    myList = list(map(int, user_input))
    
    for i in myList:
        print(detect_days(i))
