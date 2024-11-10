import pickle
from bot_v2.modules.address_book import AddressBook
from bot_v2.modules.address_book import Record
from bot_v2.modules.address_book import Phone
from bot_v2.modules.address_book import Birthday
from bot_v2.modules.address_book import Email


def all_book(User_book: AddressBook) -> str:
    """
    Функція виведення контактів, читає всю книгу контактів. \n
    `User_book` - книга контактів
    """
    for b in User_book.data:
        print(b, User_book[b])


def add_user_book(addUser: str, User_book: AddressBook) -> str:
    """
    Функція додавання користувача до Address_Book:
    (name, dict) \n
    `addUser` - ім'я користувача \n
    `User_book` - книга контактів
    """
    aub = "".join(addUser)  # Додаю ім'я зі списку до рядка
    if aub:  # Роблю перевірку на пусте значення
        rec = Record(aub)  # Створюю об'єкт класу Record
        User_book.add_record(rec.dict_record())  # І записую в UserDict
        print(f"Сontact '{aub}' added")
    else:
        print("!Add a username!")  # Виводжу попередження що ім'я не введене


def add_phone_to_user(args: list, User_book: AddressBook):
    """ 
    Функція додавання до користувача телефону:
    ([name, phone], dict) \n
    `User_book` - книга контактів \n
    `args` - список параметрів(ім'я, телефон)
    """
    n, phone = args  # Розбиваю список
    # Зберігаю завалідований номер телефону
    phone = Phone(phone).phone_validation()
    if phone != None:  # Роблю перевірку на відсутність валідації
        # Оновлюю телефон користувача
        User_book.update_user_contacts(n, {"phone": phone})


def add_birthday_to_user(args: list, User_book: AddressBook):
    """ 
    Функція додавання до користувача дня народження:
    (['name', 'birthday'], dict) \n
    `User_book` - книга контактів \n
    `args` - список параметрів(ім'я, день-народження)
    """
    try:
        n, birthday = args  # Пробую розбити список
        # Перезаписую ДН з валідацією
        birthday = Birthday(birthday).birthday_validation()
        # Оновлюю ДН користувача в словнику
        User_book.update_user_contacts(n, {"birthday": birthday})

    except:
        # Повертаю помилку
        print(
            "Enter the command correctly \n-> add-birthday [name] [DD.MM.YYYY]")


def add_email_to_user(args: list, User_book: AddressBook):
    """ 
    Функція додавання Email до користувача:
    (['name', 'email'], dict) \n
    `User_book` - книга контактів \n
    `args` - список параметрів(ім'я, ел-почта)
    """
    try:
        n, email = args  # Пробую розбити список
        # --------------------------------------------------
        email = Email(email).email_validation()
        # Оновлюю почту користувача в словнику
        User_book.update_user_contacts(n, {"email": email})

    except:
        # Повертаю помилку
        print("Enter the command correctly \n-> add-email [name] [Email]")


def add_address_to_user(args: list, User_book: AddressBook):
    """ 
    Функція додавання міста або країни до користувача:
    (['name', 'address'], dict) \n
    `User_book` - книга контактів \n
    `args` - список параметрів(ім'я, адреса)
    """
    na, adres = args
    User_book.update_user_contacts(na, {"address": adres})


def add_tag_to_user(args: list, User_book: AddressBook):
    """ 
    Функція додавання тегів до користувача:
    (['name', 'tag'], dict) \n
    `User_book` - книга контактів \n
    `args` - список параметрів(ім'я, тег)
    """
    nu, tag = args  # Розбиваю список на змінні
    User_book.add_data_to_users(nu, "tag", tag)  # Додаю тег до користувача


def searth_teg_user(args: list, User_book: AddressBook):
    """ 
    Функція пошуку користувача за тегом:
    ("tag", dict) \n
    `User_book` - книга контактів \n
    `args` - тег за яким шукати користувача
    """
    stu = "".join(args)  # Додаю ім'я зі списку до рядка
    User_book.find_tags_users("tag", stu)  # Шукаю тег


def add_notes(args: list, User_book: AddressBook):
    """ 
    Функція додавання нотаток до користувача:
    (['name', 'comment', 'note'], dict) \n
    `User_book` - книга контактів \n
    `args` - список параметрів(ім'я, коментар, нотатка)
    """
    try:
        u, com, nt = args  # Пробую розбити список
        # [com, nt] #Оновлюю нотатки користувача в словнику
        User_book.add_notes_to_users(u, [com, nt])

    except:
        # Повертаю помилку
        print("Enter the command correctly \n-> note [name] [coment] [notes]")


def view_note_user(namUser: str, User_book: AddressBook) -> str:
    """ 
    Функція для перегляду нотаток користувача:
    (['name'], dict) \n
    `User_book` - книга контактів \n
    `namUser` - ім'я користувача для пошуку нотаток
    """
    try:
        # Шукаю в книзі нотатки користувача
        dtUser = User_book.find_data_user("notes", namUser)
        for du in dtUser:  # Пробінаюсь циклом по словнику з нотатками
            print(du, "-", dtUser[du])  # Виводжу нотатки
    except:
        print(f"User {namUser} note is missing")


def remove_note_user(args: list, User_book: AddressBook):
    """ 
    Функція видалення однієї нотатки в користувача:
    (['name', 'coment'], dict) \n
    `User_book` - книга контактів \n
    `args` - список параметрів(ім'я, коментар)
    """
    try:
        n, rnu = args
        User_book.delete_data_users(n, "notes", rnu)
    except:
        print("Enter the command correctly \n-> remove-note [name] [coment]")


def remove_user_notes_all(args: list, User_book: AddressBook):
    """ 
    Функція видалення всіх нотаток в користувача:
    (['name'], dict) \n
    `User_book` - книга контактів \n
    `args` - приймає ім'я контакту який потрібно видалити
    """
    run = "".join(args)  # Додаю ім'я зі списку до рядка
    # Видаляю нотатки користувача
    User_book.delete_data_users(run, "notes", "all")




def save_data(book: AddressBook, filename: str):  # Функція збереження словника до файлу .pkl
    """ 
    Функція збереження словника до файлу .pkl : 
    (book, filename) \n
    `book` - приймає словник який потрібно зберегти \n
    `filename`  - назва файлу
    """
    with open(filename, "wb") as f:  # Відкриваю файл
        pickle.dump(book, f)  # Створюю новий файл або переписую існуючий
        print("Book is saved")


def load_data(filename: str) -> dict:  # Функція зчитування файлу .pkl
    """ 
    Функція відкриття файлу .pkl :
    (filename).  \n
    Повертає зчитаний файл, або екземпляр класу Address_Book \n
    `filename`  - назва файлу
    """
    try:
        with open(filename, "rb") as f:  # Пробую відкрити файл
            try:
                print("Book has been updated")
                return pickle.load(f)  # Декодую файл і повертаю
            except:
                return AddressBook()
    except FileNotFoundError:  # Якщо файл відсутній то створюю новий словник
        # Повернення нової адресної книги, якщо файл не знайдено
        return AddressBook()
