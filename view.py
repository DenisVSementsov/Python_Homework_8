from typing import Tuple

def choice_main_menu() -> int:
    while True:
        try:
            choice = int(input('Выберите команду меню: '))
            if choice in range(0, 8):
                print()
                return choice
            else: print('Нет такого пункта. Повторите попытку')
        except: print('Ошибка ввода. Некорректные данные')

def main_menu():
    print('\n1. Показать телефонную книгу')
    print('2. Открыть файлы телефонной книги')
    print('3. Сохранить файл телефонной книги')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Найти контакт')
    print('0. Выход\n')
    return choice_main_menu()

def print_phone_book(phone_book: list):
    if (len(phone_book) == 0):
        print('Телефонная книга пуста или не загружена')
        return

    for id, contact in enumerate(phone_book, 1):
        print(id, *contact)

def print_log_off(): print('До свидания')

def print_load_success(): print('Телефонная книга загружена')

def print_save_success(): print('Телефонная книга сохранена')

def print_remove_success(): print('Контакт удален')

def print_find_contact(): print('Поиск контакта')

def print_contact_is_not_found(): print('Контакт не найден')

def input_new_contact(): 
    name = input('Введите имя контакта:')
    phone = input('Введите телефон контакта:')
    comment = input('Введите коментарий к контакту:')
    return (name, phone, comment)

def input_contact_search_string(): 
    search_string = input('Введите строку для поиска контакта. Это может быть часть имени, номера или коментария:')
    return search_string

def update_contact_property(propName: str) -> Tuple[str, bool]:
    confirm = input(f'Хотите изменить {propName}? y/n')
    if (confirm.lower() == 'y'):
        new_value = input(f'Введите новое значение для {propName}:')
        return (new_value, True)
    return ('', False)

def update_contact(contact: Tuple[str, str, str]): 
    updatedName = update_contact_property('Имя')
    contact[0] = updatedName[0] if updatedName[1] == True else contact[0]

    updatedPhone = update_contact_property('Телефон')
    contact[1] = updatedPhone[0] if updatedPhone[1] == True else contact[1]

    updatedComment = update_contact_property('Коментарий')
    contact[2] = updatedComment[0] if updatedComment[1] == True else contact[2]

    return (contact[0], contact[1], contact[2])

def input_contact_id(message: str): 
    return int(input(message))
