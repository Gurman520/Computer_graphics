def create_bmp(width: int, height: int, f_name: str):
    with open(f_name, "wb") as f:
        f.write(b'BM')
        f.write((118 + int(height * width / 2)).to_bytes(4, "little"))  # Размер файла
        f.write((0).to_bytes(2, "little"))  # Зарезервированно
        f.write((0).to_bytes(2, "little"))  # Зарезервированно
        f.write((118).to_bytes(4, 'little'))  # Смещение изображение
        f.write((40).to_bytes(4, 'little'))  # Длина заголовка
        f.write(width.to_bytes(4, "little"))  # Ширина изображения
        f.write(height.to_bytes(4, "little"))  # Высота изображения
        f.write((1).to_bytes(2, 'little'))  # Число плоскостей
        f.write((4).to_bytes(2, 'little'))  # Количество цветов
        f.write((0).to_bytes(24, 'little'))  # Зарезервированно
        f.write((0).to_bytes(4 * 15, 'little'))  # Настройка цветов, 1- это белый и он заполняется 0-ми
        f.write(b"\xff\xff\xff\x00")  # Последний цвет отвечает за черный и его заполняем как в файле
        width_a = 1
        if width % 8 == 0:
            width_a = width // 8
        elif width > 8:
            width_a = width // 8 + 1
        for h in range(height):
            for w in range(width_a):
                if h % 2 == 0:
                    f.write(b"\x0f\x0f\x0f\x0f")
                else:
                    f.write(b"\xf0\xf0\xf0\xf0")
.

if __name__ == "__main__":
    x = int(input("Введите количество столбцов: "))
    y = int(input("Введите количество строк: "))
    file_name = input("Введите название файла: ")
    if file_name[-4:] == '.bmp':
        create_bmp(x, y, file_name)  # Количество столбцов на кол. строк
    else:
        print("Некорректное имя файла")
