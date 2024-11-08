from bot_v2.modules.address_book import AddressBook
from bot_v2.modules.basic_functions import lincFile
from bot_v2.modules.basic_functions import load_data
from bot_v2.modules.basic_functions import save_data
from bot_v2.modules.basic_functions import all_book
from bot_v2.modules.basic_functions import add_user_book
from bot_v2.modules.basic_functions import add_phone_to_user
from bot_v2.modules.basic_functions import add_birthday_to_user
from bot_v2.modules.basic_functions import add_email_to_user
from bot_v2.modules.basic_functions import add_address_to_user
from bot_v2.modules.basic_functions import add_tag_to_user
from bot_v2.modules.basic_functions import searth_teg_user
from bot_v2.modules.basic_functions import add_notes
from bot_v2.modules.basic_functions import view_note_user
from bot_v2.modules.basic_functions import remove_note_user
from bot_v2.modules.basic_functions import remove_user_notes_all
from colorama import Fore

# from modules.address_book import AddressBook
# from modules.basic_functions import lincFile
# from modules.basic_functions import load_data
# from modules.basic_functions import save_data
# from modules.basic_functions import all_book
# from modules.basic_functions import add_user_book
# from modules.basic_functions import add_phone_to_user
# from modules.basic_functions import add_birthday_to_user
# from modules.basic_functions import add_email_to_user
# from modules.basic_functions import add_address_to_user
# from modules.basic_functions import add_tag_to_user
# from modules.basic_functions import searth_teg_user
# from modules.basic_functions import add_notes
# from modules.basic_functions import view_note_user
# from modules.basic_functions import remove_note_user
# from bot_v2.modules.basic_functions import remove_user_notes_all
# from colorama import Fore



all_commands = \
    '''
Команди для контактів:
 1 - "hello" -> Привітання з користувачем
 2 - "add [ім'я]" -> Створити користувача
 3 - "all" -> Виводить всі контакти з словниками
 4 - "user [name]" -> Виводить дані користувача
 5 - "add-phone [ім'я] [номер телефону]" -> Зберігає список номерів телефону.
 6 - "show-phone [ім'я]" -> Виводить номер телефону контакту
 7 - "add-birthday [ім'я] [дата народження]" -> Додаю до контакту день народження
 8 - "show-birthday [ім'я]" -> Показую день народження контакту
 9 - "birthdays" -> Повертає список користувачів, яких потрібно привітати на задану кількість днів
 10 - "add-email [ім'я] [Email]" -> Команда додавання електронної пошти до користувача
 11 - "show-email [name]" -> Виводить Email
 12 - "add-addres [name] [sity]" -> Додає адресу до користувача
 13 - "show-addres [name]" -> Виводить адресу до користувача
 14 - "remove-user [ім'я]" -> Команда видалення користувача
 
 15 - "open-book [link to file]" -> Команда для відкриття файлу в ручну (якщо не вказати назву то поверне пустий словник)
 16 - "exit" -> Закриває програму із збереженням даних
 17 - "close" -> Закриває програму без збереження даних
 18 - "help" -> Виводить всі доступні команди
 19 - "save" -> Команда зберігання словника в файл .pkl

 20 - "text-color [color]" -> Вибирає коляр тексту
>>>>>>> c979a9cffbc5c3ef0bab7b043498c55c1382f8c5

Команди для нотатків:
 1 - "note [name] [coment] [notes]" -> Додавання нотаток до користувача або редагую існуючі
 2 - "view-notes [name]" -> Виводить нотатки користувача
 3 - "view-all-notes" -> Виводить всі нотатки всіх користувачів
 4 - "remove-notes-all [name]" -> Видаляє всі нотати в користувача
 5 - "remove-note [name] [comment]" -> Видаляє конкретну нотатку користувача
 
Команди для тегів:
 1 - "add-tag [name] [tag]" -> Додає тег до користувача
 2 - "tag-user [tag]" -> Шукає користувача за тегом
'''


""" Основний файл з циклом та парсингом команд"""


def parse_input(user_input):  # Функція для парсингу команд
    cmd, *args = user_input.split()  # Розбиваю команду
    cmd = cmd.strip().lower()  # Записую команду в окрему змінну
    return cmd, *args  # Повертаю команду і аргументи


def main():  # Основна функція з циклом
    default_color = Fore.RESET
    color = default_color
    book = AddressBook()  # Екземпляр класу AddressBook

    # Записую до книги декодовані дані з файлу
    book.add_record(load_data(lincFile))

    print("Welcome to the assistant bot!")
    while True:  # Основний цикл для постійного запиту команд
        user_input = input("Enter a command: ")  # Запитую команду

        try:  # Якщо є команда то виконую перевірки
            # Зберігаю результат парсингу в змінні
            command, *args = parse_input(user_input)

            match command:  # Команди

                case "hello":  # Привітання
                    print("Hello! \nHow can I help you?")

                case "help": print(all_commands)  # Команда з списком команд

                # Команда виведення всх контактів з AddressBook з усіма даними
                case "all": all_book(book)

                # Команда додавання користувача до AddressBook
                case "add": add_user_book(args, book)

                case "user":  # Виводить дані заданого користувача
                    u = "".join(args)  # Додаю ім'я зі списку до рядка
                    print(book.find(u))

                case "remove-user":  # Команда видалення користувача з AddressBook
                    du = "".join(args)
                    book.delete(du)

                case "add-phone":  # Додаю телефон до користувача
                    add_phone_to_user(args, book)
                case "show-phone":  # Виводжу телефон користувача
                    un = "".join(args)  # Додаю ім'я зі списку до рядка
                    # Шукаю телефон користувача в книзі
                    book.find_contacts_user(un, "phone")

                case "add-birthday":  # Додаю день народження до користувача
                    add_birthday_to_user(args, book)
                case "show-birthday":  # Виводжу день народження користувача
                    ub = "".join(args)  # Додаю ім'я зі списку до рядка
                    # Шукаю день народження користувача в книзі
                    book.find_contacts_user(ub, "birthday")

                case "birthdays":  # Виводжу список користувачів, яких потрібно привітати на задану кількість днів
                    in_period = int(input('Input period to search: '))
                    print("Dictionary with greetings: ", [
                          book.find_birthday_users(in_period)])

                case "add-email":  # Додаю пошту до користувача
                    add_email_to_user(args, book)
                case "show-email":  # Виводжу почту користувача
                    uem = "".join(args)
                    book.find_contacts_user(uem, "email")

                # Додаю адресу
                case "add-addres": add_address_to_user(args, book)
                case "show-addres":  # Виводжу адресу користувача
                    nad = "".join(args)
                    book.find_contacts_user(nad, "address")

                case "text-color":  # Вибір коляру
                    if len(args) == 0:
                        color = default_color
                    else:
                        color = Fore.__dict__.get(args[0].upper())
                        if color is None:
                            color = default_color
                    print(color)

                # Додаю адресу
                case "add-addres": add_address_to_user(args, book)
                case "show-addres":
                    nad = "".join(args)
                    book.find_contacts_user(nad, "address")

                # Теги користувача
                case "add-tag": add_tag_to_user(args, book)
                case "tag-user": searth_teg_user(args, book)

                # Нотатки
                case "note":  # Додаю нотатки до користувача
                    add_notes(args, book)

                case "view-notes":  # Перегляд всіх нотаток користувача
                    vnU = "".join(args)  # Додаю ім'я зі списку до рядка
                    view_note_user(vnU, book)
                case "view-all-notes":
                    # Виведення всіх нотаток користувача
                    book.find_data_user("notes")

                case "remove-note":  # Видаляє нотатку в користувача
                    remove_note_user(args, book)
                case "remove-notes-all":
                    remove_user_notes_all(args, book)

                case "open-book":  # Команда для відкриття книги в ручну
                    # Додаю посилання на файл зі списку до рядка
                    lb = "".join(args)
                    # Записую до книги AddressBook декодовані дані з файлу
                    book.add_record(load_data(lb))

                # Зберігаю в файл .pkl книгу з користувачами
                case "save": save_data(book, lincFile)

                case "close": break  # Команда для закриття книги НЕ зберігає словник

                case "exit":  # Команда для закриття книги зберігає словник
                    # Зберігаю в файл .pkl книгу з користувачами
                    save_data(book, lincFile)
                    print("Good bye!")
                    break

                case _:  # Якщо команда не роспізнана
                    print("Invalid command!!!")

        except:
            # Якщо команда відсутня виводжу підказку
            print("Incorrect command... \nEnter 'help'")


if __name__ == "__main__":
    main()
