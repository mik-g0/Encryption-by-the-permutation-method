from Initial_encryption import encrypt, decrypt


import random

def substitution(text, keyword):
    """
    Применяет подстановку к тексту на основе таблицы, сгенерированной по ключу.
    :param text: исходный текст
    :param keyword: ключ для генерации таблицы подстановки
    :return: заменённый текст
    """
    sub_table = create_substitution_table(keyword)  # создаём таблицу подстановки по ключу
    return ''.join(sub_table.get(char, char) for char in text)

def reverse_substitution(text, keyword):
    """
    Применяет обратную подстановку к тексту для восстановления исходного текста.
    :param text: зашифрованный текст
    :param keyword: ключ для генерации таблицы подстановки
    :return: восстановленный текст
    """
    sub_table = create_substitution_table(keyword)  # создаём таблицу подстановки по ключу
    reverse_table = {v: k for k, v in sub_table.items()}  # переворачиваем таблицу для обратной подстановки
    return ''.join(reverse_table.get(char, char) for char in text)

def create_substitution_table(keyword):
    """
    Создаёт таблицу подстановки на основе заданного ключа.
    :param keyword: ключ для генерации таблицы
    :return: sub_table - таблица подстановки
    """
    # Используем хеш от ключа для установки начального значения генератора случайных чисел
    random.seed(hash(keyword))  # хешируем ключ для получения начального значения
    alphabet = list('abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    shuffled = alphabet[:]  # копируем алфавит

    # Перемешиваем алфавит в предсказуемом порядке на основе ключа
    random.shuffle(shuffled)

    # Создаем таблицу подстановки
    sub_table = dict(zip(alphabet, shuffled))
    return sub_table


# Основная функция шифрования
def encrypt_with_substitution(text, keyword):
    substituted_text = encrypt(text, keyword)
    return substitution(substituted_text, keyword)

# Основная функция дешифрования
def decrypt_with_substitution(text, keyword):
    decrypted_text = decrypt(text, keyword)
    return reverse_substitution(decrypted_text, keyword)

# Пример использования
keyword = "КОДИК"
text = "незабываемо"
encrypted_text = encrypt_with_substitution(text, keyword)
print("Зашифрованное сообщение:", encrypted_text)

decrypted_text = decrypt_with_substitution(encrypted_text, keyword)
print("Расшифрованное сообщение:", decrypted_text)
