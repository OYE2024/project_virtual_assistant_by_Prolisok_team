
import pickle
from packages import AddressBook, Record, Phone, Birthday, Email


def all_book(User_book: AddressBook) -> str:
    """
    Функція виведення контактів,
    читає всю книгу контактів
    """
    for b in User_book.data:
        print(b, User_book[b])


def add_user_book(addUser, User_book: AddressBook) -> str:
    """
    Функція додавання користувача до Address_Book
    """
    u = "".join(addUser)  # Додаю ім'я зі списку до рядка
    if u:  # Роблю перевірку на пусте значення
        rec = Record(u)  # Створюю об'єкт класу Record
        User_book.add_record(rec.dict_record())  # І записую в UserDict
        print(f"Сontact '{u}' added")
    else:
        print("!Add a username!")  # Виводжу попередження що ім'я не введене


def add_phone_to_user(args, User_book):
    """ 
    Функція додавання до користувача телефону
    ([name, phone], dict)
    """
    n, p = args  # Розбиваю список
    # Зберігаю завалідований номер телефону
    p = Phone(p).phone_validation()
    if p != None:  # Роблю перевірку на відсутність валідації
        # Оновлюю телефон користувача
        User_book.update_user_contacts(n, {"phone": p})


def add_birthday_to_user(args, User_book):
    """ 
    Функція додавання до користувача дня народження
    (['name', 'birthday'], dict)
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


def add_email_to_user(args, User_book: AddressBook):
    """ 
    Функція додавання Email
    (['name', 'email'], dict)
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


# -------------------------------------
def add_address_to_user(args, User_book: AddressBook):
    n, adres = args
    User_book.update_user_contacts(n, {"address": adres})


def add_tag_to_user(args, User_book):
    """ 
    Функція додавання тегів до користувача
    (['name', 'tag'], dict)
    """
    nn, tag = args  # Розбиваю список на змінні
    User_book.add_data_to_users(nn, "tag", tag)  # Додаю тег до користувача


def searth_teg_user(args, User_book):  # Функція пошуку користувача за тегом
    tn = "".join(args)  # Додаю ім'я зі списку до рядка
    User_book.find_tags_users("tag", tn)  # Шукаю тег


def add_notes(args, User_book):  # Функція додавання нотаток до користувача з
    try:
        u, com, nt = args  # Пробую розбити список
        # [com, nt] #Оновлюю нотатки користувача в словнику
        User_book.add_notes_to_users(u, [com, nt])

    except:
        # Повертаю помилку
        print("Enter the command correctly \n-> note [name] [coment] [notes]")


def view_note_user(namUser, User_book):  # Функція для перегляду нотаток користувача
    try:
        # Шукаю в книзі нотатки користувача
        dtUser = User_book.find_data_user("notes", namUser)
        for du in dtUser:  # Пробінаюсь циклом по словнику з нотатками
            print(du, "-", dtUser[du])  # Виводжу нотатки
    except:
        print(f"User {namUser} note is missing")


def remove_note_user(args, User_book):  # Функція видалення однієї нотатки в користувача
    try:
        n, nd = args
        User_book.delete_data_users(n, "notes", nd)
    except:
        print("Enter the command correctly \n-> remove-note [name] [coment]")


# Функція видалення всіх нотаток в користувача
def remove_user_notes_all(args, User_book):
    rnu = "".join(args)  # Додаю ім'я зі списку до рядка
    # Видаляю нотатки користувача
    User_book.delete_data_users(rnu, "notes", "all")


"""  і """
lincFile = "addressbook.pkl"  # Посилання на файл (назва файлу)


def save_data(book, filename):  # Функція збереження словника до файлу .pkl
    """ 
    Функція збереження даних в файл .pkl
    """
    with open(filename, "wb") as f:  # Відкриваю файл
        pickle.dump(book, f)  # Створюю новий файл або переписую існуючий
        print("Book is saved")


def load_data(filename):  # Функція зчитування файлу .pkl
    """ 
    Функція відкриття файлу .pkl -> 
    повертає зчитаний файл, або екземпляр класу Address_Book
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
