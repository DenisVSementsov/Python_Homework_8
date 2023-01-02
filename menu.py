import view
import phone_book
import data_base

def main_menu(choice: int):
    match choice:
        case 1:
            phone_book_records = phone_book.get_phone_book()
            view.print_phone_book(phone_book_records)
        case 2:
            data_base.load_data_base()
            view.print_load_success() 
        case 3:
            data_base.save_data_base()
            view.print_save_success()
        case 4:
            new_contact = view.input_new_contact()
            phone_book.add_contact(new_contact)
        case 5:
            phone_book_records = phone_book.get_phone_book()
            view.print_phone_book(phone_book_records)
            id = view.input_contact_id('Введите ID контакта, который хотите изменить:')
            contact = phone_book.find_contact(id)
            if (contact != None): 
                updated_contact = view.update_contact(contact)
                phone_book.update_contact(id, updated_contact)
            else: view.print_contact_is_not_found()
        case 6:
            phone_book_records = phone_book.get_phone_book()
            view.print_phone_book(phone_book_records)
            id = view.input_contact_id('Введите ID контакта, который хотите удалить:')
            if (phone_book.remove_contact(id)) : view.print_remove_success()
        case 7:
            view.print_find_contact()
            search_string = view.input_contact_search_string()
            contacts = phone_book.find_contacts(search_string)
            view.print_phone_book(contacts)
        case 0:
            return True

def start():
    while True:
        choice = view.main_menu()
        if (main_menu(choice)):
            view.print_log_off()
            break

start()