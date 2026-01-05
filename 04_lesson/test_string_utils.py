import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# Позитивные проверки Функция capitalize
@pytest.mark.positive
@pytest.mark.positive_capitalize
@pytest.mark.parametrize("input_str, expected", [
    ("d", "D"),                                 # 1. 1 буква нижний регистр
    ("daniil golikov", "Daniil golikov"),       # 2. 2 Слова через пробел
    ("Python", "Python"),                       # 3. Текст Верхний регистр
    ("программирование", "Программирование"),   # 4. Текст на Кирилице
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Позитивные проверки Функция trim
@pytest.mark.positive
@pytest.mark.positive_trim
@pytest.mark.parametrize("input_str, expected", [
    (" String", "String"),          # 1. Один пробел в начале текст
    ("Result", "Result"),           # 2. Строка без пробела
    ("     ", ""),                  # 3. Пробелы
    ("", ""),                       # 4. Пустая строка
    (" First ", "First "),          # 5. Пробел в начале и в конце строки
    ("Second day", "Second day"),   # 6. 2 слова через пробел
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


# Позитивные проверки функции contains
@pytest.mark.positive
@pytest.mark.positive_contains
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("String", "S", True),      # 1. Первый символ (заглавная 'S')
    ("String", "g", True),      # 2. Последний символ
    ("String", "r", True),      # 3. Символ в середине
    ("String ", " ", True),     # 4. Пробел в конце строки
    ("String", "s", False),     # 5. Регистрозависимость: 's' ≠ 'S'
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


# Позитивные проверки Функция delete_symbol
@pytest.mark.positive
@pytest.mark.positive_delete_symbol
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "P", "Skyro"),           # 1. Символ в середине
    ("SkyPro", "Pro", "Sky"),           # 2. Подстрока в конце
    ("SkyPro", "Sky", "Pro"),           # 3. Подстрока в начале
    ("banana", "a", "bnn"),             # 4. Повторяющиеся символы
    ("Hello World", "o", "Hell Wrld"),  # 5. Два слова с одинаковым символом
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


# Негативные проверки Функция capitalize
@pytest.mark.negative
@pytest.mark.negative_capitalize
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),   # 1. Цифры и буквы
    ("", ""),               # 2. Пустая строка
    ("   ", "   "),         # 3. Пробелы
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Негативные проверки Функция trim
@pytest.mark.negative
@pytest.mark.negative_trim
@pytest.mark.parametrize("input_str, expected", [
    ("123", "123"),     # 1. Цифры
    ("[]", "[]"),       # 2. []
    ("None", "None"),   # 3. NONE
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# Негативные проверки Функция contains
@pytest.mark.negative
@pytest.mark.negative_contains
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("String", "", True),   # 1. Пустой символ
    ("", "S", False),       # 2. Пустая строка
    ("", "", True),         # 3. Пустой символ и строка
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.negative_delete_symbol
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("String", "", "String"),     # 1. Пустой символ  строка не меняется
    ("", "S", ""),                # 2. Пустая строка  результат пустой
    ("", "", ""),                 # 3. Оба аргумента пустые
    ("SkyPro", "x", "SkyPro"),    # 4. Символ отсутствует  строка без изменений
    ("Hello World", " ", "HelloWorld"),  # 5. Удаление пробела
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
