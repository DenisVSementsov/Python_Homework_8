from typing import Tuple

phone_book = []

def get_phone_book()-> list:
    global phone_book
    return phone_book

def set_phone_book(new_phone_book: list):
    global phone_book
    phone_book = new_phone_book

def add_contact(contact: Tuple[str, str, str]):
    global phone_book
    phone_book.append(contact)

def update_contact(id: int, contact: Tuple[str, str, str]):
    global phone_book
    phone_book[id-1] = contact

def remove_contact(id: int):
    global phone_book
    name = phone_book[id-1][0]
    confirm = input(f'Уверены, что хотите удалить контакт {name}? y/n')
    if(confirm.lower() == 'y'):
        phone_book.pop[id-1]
        return True
    return False

def find_contact(id: int) -> Tuple[str, str, str] | None:
    global phone_book
    if (len(phone_book) <= id): return None
    return phone_book[id-1]

def find_contacts(search_string: str) -> list:
    global phone_book
    return [i for i in phone_book if search_string in i[0] or search_string in i[1] or search_string in i[2]]