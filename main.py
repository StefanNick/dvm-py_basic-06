password = input("Введите пароль: ")

if len(password) > 12:
    print("Длинный")
else:
    print("Короткий")

for symbol in password:
    if symbol.isdigit():
        print(symbol, "- Цифра")
    else:
        print(symbol,"- Буква")