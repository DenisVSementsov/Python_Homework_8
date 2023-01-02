import phone_book

path = 'phone_book.txt'

def str_to_list(phone_book_records: list) -> list: 
    return [contact.strip().split(';') for contact in phone_book_records]

def list_to_str(phone_book_records: list) -> str: 
    new_phone_book = [';'.join(contact)+ '\n' for contact in phone_book_records]
    new_phone_book[-1] = new_phone_book[-1][:-1]
    return ''.join(new_phone_book)

def load_data_base():
    with open(path, 'r', encoding = 'UTF-8') as file:
        phone_book_records = file.readlines()
    phone_book.set_phone_book(str_to_list(phone_book_records))

def save_data_base():
    phone_book_records = phone_book.get_phone_book()
    string = list_to_str(phone_book_records)
    with open(path, 'w', encoding = 'UTF-8') as file:
        file.write(string)
