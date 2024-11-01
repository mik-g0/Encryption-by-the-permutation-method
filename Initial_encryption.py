def encrypt(text, keyword):
    """
    Реализует шифрование методом вертикальной перестановки, разбивая текст на столбцы и упорядочивая их по ключу.
    :param text: исходный текст
    :param keyword: ключ
    :return: encrypt_text - зашифрованное сообщение
    """
    num_columns = len(keyword)
    num_rows = -(-len(text) // num_columns)  # Округляем вверх для расчета строк
    empty_cells = num_columns * num_rows - len(text)

    # Заполняем таблицу посимвольно
    table = ['' for _ in range(num_columns)]
    for i, char in enumerate(text):
        column = i % num_columns
        table[column] += char

    # Заполняем пустые ячейки в последнем ряду символом "-"
    for i in range(empty_cells):
        table[-(i + 1)] += '-'

    # Сортируем столбцы по ключу
    sorted_columns = create_key_order(keyword)
    sorted_table = [table[i - 1] for i in sorted_columns]

    # Объединяем столбцы в зашифрованный текст
    encrypt_text = ''.join(sorted_table)
    return encrypt_text


def decrypt(text, keyword):
    """
    Реализует дешифрование, возвращая зашифрованный текст в исходное сообщение,
    распределяя символы по строкам в соответствии с ключом.
    :param text: зашифрованный текст
    :param keyword: ключ
    :return: decrypt_text - расшифрованное сообщение
    """
    num_columns = len(keyword)
    num_rows = len(text) // num_columns
    empty_cells = num_columns * num_rows - len(text)

    # Разделяем зашифрованный текст на столбцы
    sorted_columns = create_key_order(keyword)
    table = ['' for _ in range(num_columns)]
    col_start = 0

    for index in sorted_columns:
        col_len = num_rows - 1 if index > num_columns - empty_cells else num_rows
        table[index - 1] = text[col_start:col_start + col_len]
        col_start += col_len

    # Восстанавливаем текст, собирая строки по символам из каждого столбца
    decrypt_text = ''
    for row in range(num_rows):
        for col in table:
            if row < len(col):
                decrypt_text += col[row]
    decrypt_text = decrypt_text.replace("-", "")  # Убираем символы заполнения
    return decrypt_text


def create_key_order(keyword):
    """
    Создает порядок индексов для сортировки столбцов по ключу, чтобы использовать его при шифровании и дешифровании.
    :param keyword: ключ
    :return: index_list - список с измененными положениями столбцов
    """
    index_list = []
    key = list(keyword)
    indexed_key = list(enumerate(sorted(key), 1))
    for char in key:
        for index, sorted_char in indexed_key:
            if char == sorted_char:
                index_list.append(index)
                indexed_key.remove((index, sorted_char))
                break
    return index_list
