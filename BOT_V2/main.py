# Імпортую свій файл з користувачами
from BOT_V2 import AddressBook, lincFile, load_data, save_data, all_book, add_user_book, add_phone_to_user, add_birthday_to_user, add_email_to_user, add_address_to_user, add_tag_to_user, searth_teg_user, add_notes, view_note_user, remove_note_user, remove_user_notes_all

all_commands = \
    '''
Команди для контактів:
 1 - "hello" -> Привітання з користувачем
 2 - "add [ім'я]" -> Створюю користувача
 3 - "add-phone [ім'я] [номер телефону]" -> Зберігає список номерів телефону, ???при додаванні робить перевірку чи номер існує.
 4 - "phone [ім'я]" -> Виводить номер телефону контакту
 5 - "all" -> Виводить всі контакти з словниками
 6 - "close" -> Закриває програму без збереження даних
 7 - "add-birthday [ім'я] [дата народження]" -> Додаю до контакту день народження
 8 - "show-birthday [ім'я]" -> Показую день народження контакту
 9??? - "birthdays" -> Повертає список користувачів, яких потрібно привітати на задану кількість днів від введеної дати
 10 - "open-book [link to file]" -> Команда для відкриття файлу в ручну (якщо не вказати назву то поверне пустий словник)
 11 - "remove-user [ім'я]" -> Команда видалення користувача
 12 - "add-email [ім'я] [Email]" -> Команда додавання електронної пошти до користувача
 13 - "save" -> Команда зберігання словника в файл .pkl
 14 - "help" -> Виводить всі доступні команди 
 15 - "exit" -> Закриває програму із збереженням даних

 16 - "user [name]" -> Виводить дані користувача
 17 - "add-addres [name] [sity]" -> Додає адресу до користувача
 18 - "show-addres [name]" -> Виводить адресу до користувача

Команди для нотатків:
 1 - "n [name] [coment] [notes]" -> Додавання нотаток до користувача або редагую існуючі
 2 - "view-notes [name]" -> Виводить нотатки користувача
 3 - "view-all-notes" -> Виводить всі нотатки всіх користувачів
 4 - "remove-notes-all [name]" -> Видаляє всі нотати в користувача
 5 - "remove-note [name] [comment]" -> Видаляє конкретну нотатку користувача
 
Команди тегів:
 1 - "add-tag [name] [tag]" -> Додає тег до користувача
 2 - "tag-user [tag]" -> Шукає користувача за тегом
'''


""" Основний цикл з парсингом команд"""


def parse_input(user_input):  # Функція для парсингу команд
    cmd, *args = user_input.split()  # Розбиваю команду
    cmd = cmd.strip().lower()  # Записую команду в окрему змінну
    return cmd, *args  # Повертаю команду і аргументи


def main():  # Основна функція з циклом
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

                case "help": print(all_commands)  # Команда з привітанням

                # Команда виведення всх контактів з AddressBook з усіма даними
                case "all": all_book(book)

                # Команда додавання користувача до AddressBook
                case "add": add_user_book(args, book)

                case "user":  # -----------------------------------
                    u = "".join(args)  # Додаю ім'я зі списку до рядка
                    print(book.find(u))

                case "remove-user":  # Команда видалення користувача з AddressBook
                    du = "".join(args)
                    book.delete(du)

                case "add-phone":  # Додаю телефон до користувача
                    add_phone_to_user(args, book)
                case "phone":  # Виводжу телефон користувача
                    un = "".join(args)  # Додаю ім'я зі списку до рядка
                    # Шукаю телефон користувача в книзі
                    book.find_contacts_user(un, "phone")

                case "add-birthday":  # Додаю день народження до користувача
                    add_birthday_to_user(args, book)
                case "show-birthday":  # Виводжу день народження користувача
                    ub = "".join(args)  # Додаю ім'я зі списку до рядка
                    # Шукаю день народження користувача в книзі
                    book.find_contacts_user(ub, "birthday")

                case "birthdays":  # Виводжу дні народження користувачів на найближчий тиждень
                    print("Dictionary with greetings for the week: ",
                          book.find_birthday_users_for_week())

                case "add-email":  # Додаю пошту до користувача
                    add_email_to_user(args, book)
                case "show-email":  # Виводжу почту користувача
                    uem = "".join(args)
                    book.find_contacts_user(uem, "email")

                # -----------------------------------------
                case "add-addres": add_address_to_user(args, book)
                case "show-addres":
                    nad = "".join(args)
                    book.find_contacts_user(nad, "address")

                # Теги користувача
                case "add-tag": add_tag_to_user(args, book)
                case "tag-user": searth_teg_user(args, book)

                # Нотатки
                case "n":  # Додаю нотатки до користувача
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

            # #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
                case "open-book":  # Команда для відкриття книги в ручну
                    # Додаю посилання на файл зі списку до рядка
                    lb = "".join(args)
                    # Записую до книги AddressBook декодовані дані з файлу
                    book.add_record(load_data(lb))

                # Зберігаю в файл .pkl книгу з користувачами
                case "save": save_data(book, lincFile)

                # case "close": break #Команда для закриття книги НЕ зберігає словник

                case "exit":  # Команда для закриття книги зберігає словник
                    # Зберігаю в файл .pkl книгу з користувачами
                    save_data(book, lincFile)
                    print("Good bye!")
                    break

                case _:  # Якщо команда не роспізнана
                    print("Invalid command!!!")

        except:
            print("Incorrect command...")  # Якщо команда відсутня


if __name__ == "__main__":
    main()
