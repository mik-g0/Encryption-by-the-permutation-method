def encrypt(text, keyword):
    """
    Реализует шифрование методом вертикальной перестановки, разбивая текст на столбцы и упорядочивая их по ключу.
    :param text: исходный текст
    :param keyword: ключ
    :return: encrypt_text - зашифрованное сообщение
    """
    num_columns = len(keyword)
    table = [''] * num_columns
    empty_cells = len(text) % num_columns + 1
    for inx, char in enumerate(text):
        column = inx % num_columns
        table[column] += char
    for i in range(1, empty_cells):
        empty_char = '-'
        table[-i] += empty_char
    sorted_columns = create_key_order(keyword)
    len_table = len(table)
    encrypt_list = []
    i = 0
    if i < len_table:
        for value in sorted_columns:
            value_tuple = value, table[i]
            encrypt_list.append(value_tuple)
            i += 1
    sorted_list = sorted(encrypt_list)
    encrypt_text = ''
    for i in range(num_columns):
        encrypt_text += sorted_list[i][1]
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
    num_rows = len(text) // len(keyword)
    table = []
    for i in range(num_columns):
        row_text = text[i * num_rows: (i + 1) * num_rows]
        table.append(row_text)
    sorted_columns = create_key_order(keyword)
    table = list(enumerate(table, 1))
    decrypt_list_enumerate = []
    decrypt_list = []
    for value in sorted_columns:
        value_tuple = value, table[value-1][1]
        decrypt_list_enumerate.append(value_tuple)
        decrypt_list.append(table[value-1][1])
    decrypt_text = ""
    for i in range(len(decrypt_list[0])):
        for block in decrypt_list:
            decrypt_text += block[i]
    decrypt_text = decrypt_text.replace("-", "")
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


text = "ВОТЭТОДАКОДСУПЕР"
key = "СЕКРЕТ"
print(create_key_order(key))