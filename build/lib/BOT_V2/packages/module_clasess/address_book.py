from datetime import datetime
from collections import UserDict
import re


class AddressBook(UserDict):  # Клас для словника

    def add_record(self, data):  # Метод для додавання словника до self.data
        """ 
        Метод запису даних до UserDict
        """
        super().update(data)  # Додаю словник через super

    def find(self, fName: str):  # Шукаю в словнику по імені
        """ 
        Метод для пошуку користувача в словнику,
        повертає словник
        """
        result = {}
        try:
            result.update({fName: self.data[fName]})
            return result  # Повертаю результат
        except:
            # Повертаю попередження про відсутність користувача
            return f"User -{fName}- is missing"

    def delete(self, dName):  # Метод для видалення запису з словника
        """ 
        Метод для видалення користувача
        """
        try:  # Перевіряю на наявність користувача
            self.data.pop(dName)  # Видаляю користувача
            print(f"Delet - '{dName}' ")
        except:
            # Виводжу попередження що користувач відсутній
            print("User is missing")

    def find_contacts_user(self, contName, contValue):
        """ 
        Метод пошуку контактних даних користувачів
        """
        if self.data.get(str(contName)):  # Роблю перевірку на співпадіння в поточному словнику користувачів UserDict
            try:
                # Зберігаю словник користувача з UserDict і витягую з словника значення по ключу
                userData = dict(self.data[contName])["contacts"]
                # Повертаю результат пошуку через прінт
                return print(userData[contValue])
            except:
                print(f"There is no contact-> {contValue}")

        else:
            # Повертаю попередження про відсутність користувача
            print(f"User -{contName}- is missing")


# Метод пошуку даних користувача в UserDict


    def find_data_user(self, findValue, findName=None):
        if findName == None:  # Якщо немає імені то виводжу всі вкладені значення з даних користувача

            for vl in self.data:
                # Виводжу всі значення з даних кожного користувача
                print(vl, self.data[vl][findValue])

        else:  # Якщо є вхідне ім'я користувача то шукаю дані користувача
            # Роблю перевірку на співпадіння в поточному словнику користувачів UserDict
            if self.data.get(str(findName)):
                # Зберігаю словник користувача з UserDict і витягую з словника значення по ключу
                userData = dict(self.data[findName])[findValue]
                return userData  # Повертаю словник з даними користувача

            else:
                # Повертаю попередження про відсутність користувача
                print(f"User -{findName}- is missing")


# Метод пошуку тегів


    def find_tags_users(self, tagVal, tagNam):
        for tg in self.data:  # Пробігаюсь циклом по словнику
            if self.data[tg].get(tagVal):  # Шукаю 'теги' в словниках користувачів
                # Зберігаю знайдений тег з словника
                dtu = str(dict(self.data[tg])[tagVal])
                if tagNam == dtu:  # Роблю перевірку за тегом
                    return print(dtu, tg)  # Виводжу результат пошуку за тегом


# Метод додавання нових даних до користувача


    def add_data_to_users(self, dUser, newData, addNewData):
        # Роблю перевірку на співпадіння в поточному словнику користувачів UserDict
        if self.data.get(dUser):
            # Зберігаю словник користувача з UserDict
            userData = dict(self.data[dUser])
            # Оновлюю словник користувача <- вхідним словником
            userData.update({newData: addNewData})
            # Оновлюю словник користувача в UserDict
            super().update({dUser: userData})
            print("Data has been updated")


# Метод для оновлення/додавання даних до користувача

    # Оновлюю контактні дані користувача


    def update_user_contacts(self, uUser, uDat=None):
        # Зберігаю ключ з вхідного словника який добавлю в контакти до користувача
        uDatKeys = "".join(dict(uDat).keys())
        uDatValues = uDat[uDatKeys]  # Зберігаю значення з вхідного словника
        phone_list = []
        # Роблю перевірку на співпадіння в поточному словнику користувачів UserDict
        if self.data.get(uUser):
            # Зберігаю словник користувача з UserDict якщо є співпадіння
            userD = dict(self.data[uUser])

            if userD.get("contacts"):  # Якщо є співпадіння "contacts" то додаю дані
                # Зберігаю словник "contacts" з користувача з UserDict
                contD = dict(userD["contacts"])

                # Якщо немає спіпадінь в словнику користувача то додаю новий словник до користувача
                if contD.get(uDatKeys) == None:
                    # Додаю значення до вкладеного словника в "contacts"
                    contD.update(uDat)
                    # Добавляю до словника "contacts" користувача <- вхідний словник
                    userD.update({"contacts": contD})
                    # Оновлюю користувача в UserDict
                    super().update({uUser: userD})
                    return print(f"'{uUser}' -> data has been added")

                if contD.get(uDatKeys):  # Якщо є ключ в користувача то оновлюю значення словника

                    if uDatKeys == "phone":

                        for ph in contD[uDatKeys]:
                            if ph != None:
                                phone_list.append(ph)
                        phone_list.append(uDatValues)
                        contD.update({"phone": phone_list})
                    else:
                        # Додаю значення до вкладеного словника в "contacts"
                        contD.update(uDat)

                    # Добавляю до словника "contacts" користувача <- вхідний словник
                    userD.update({"contacts": contD})
                    # Оновлюю користувача в UserDict
                    super().update({uUser: userD})
                    return print(f"'{uUser}' -> data has been updated")

            else:
                # Можна реалізувати нові параметри до контакту
                print("Парамерт відсутній в контакті")

        else:
            # Якщо користувача не знайдено
            return print(f"User '{uUser}' -> is missing")


# Метод для оновлення/додавання нотаток користувача

    # Приймає список [comentars , notate]


    def add_notes_to_users(self, nUser, notes):
        comentars, notate = notes  # Розбиваю вхідний список на змінні

        # Роблю перевірку на співпадіння в поточному словнику користувачів UserDict
        if self.data.get(nUser):
            # Зберігаю словник користувача з UserDict якщо є співпадіння
            contD = dict(self.data[nUser])

            if contD.get("notes") != None:  # Якщо є співпадіння "notes" то додаю нотатки
                # Зберігаю словник "notes" з користувача з UserDict
                noteD = dict(contD["notes"])
                # Оновлюю словник з нотатками
                noteD.update({comentars: notate})
                contD.update({"notes": noteD})  # Додаю нотатки до користувача
                # Оновлюю користувача в UserDict
                super().update({nUser: contD})
                print("Нотатку додано")

            if contD.get("notes") == None:  # Якщо в користувача немає нотаток
                # Створюю новий словник для нотаток
                inComent = {comentars: notate}
                # Додаю нотатки до користувача
                contD.update({"notes": inComent})
                # Оновлюю користувача в UserDict
                super().update({nUser: contD})
                print("Нотатку додано")

        else:
            # Якщо користувача не знайдено
            return print(f"User '{nUser}' -> is missing")


# Метод видалення даних користувача

    # Приймає ім'я, ключ для даних, дані(що видаляються)

    def delete_data_users(self, ddName, keyData, ddData=None):
        # Роблю перевірку на співпадіння в поточному словнику користувачів UserDict
        if self.data.get(ddName):
            # Зберігаю словник з даними користувача
            dataUser = dict(self.data[ddName])
            if ddData == "all":  # Команда для видалення всіх нотаток
                print(dataUser.pop(keyData))  # Видаляю словник з нотатками
                # Оновлюю користувача в UserDict
                super().update({ddName: dataUser})
            else:
                try:
                    # Видаляю дані користувача
                    print("delet->", ddData, "-",
                          dataUser[keyData].pop(ddData))
                except:
                    # Попередження про відсутність нотатки в користувача
                    return print(f"User {ddName} note is missing")

        else:
            # Якщо користувача не знайдено
            return print(f"User '{ddName}' -> is missing")


# Метод для виведення днів народження на наступний тиждень (на задану кількість днів)


    def find_birthday_users_for_week(self):  # birthdays
        try:
            today_time = datetime.today().date()  # Зберігаю поточну дату
            dict_res = {}  # Словник для результату пошуку

            for ur in self.data:  # Проходжусь по словнику UserDict
                # Зберігаю словник користувача
                users_dicts = dict(self.data[ur])["contacts"]
                # print(users_dicts)

                # Роблю перевірку наявність дати народження
                if users_dicts.get("birthday"):
                    # Перетворюю ДН з словника в об'єкт datetime
                    birtDT = datetime.strptime(
                        users_dicts["birthday"], '%Y-%m-%d').date()
                    # Замінюю рік з ДН на поточний
                    repYear = birtDT.replace(year=today_time.year)

                    # Віднімаю ДН від поточної дати і зберігаю як int
                    res_bird = int((repYear - today_time).days)
                    if res_bird <= 7 and res_bird >= 0:  # Перевіряю чи на цьому тижні ДН
                        # Додаю до словника результатат перевірки
                        dict_res.update({ur: birtDT.isoformat()})

            return dict_res  # Повертаю словник з результатом пошуку

        except:
            # Виводжу повідомлення якщо є помилкова дата народження в словнику
            print("Wrong date in the dictionary")


class Field():  # Базовий клас поля для контакту
    def __init__(self, fd_Name, fd_Phone=None) -> None:
        self.fd_Name = fd_Name
        self.fd_Phone = fd_Phone


class Name(Field):  # Клас для імені
    def __init__(self, valName) -> None:
        self.valName = valName

    def __str__(self) -> str:
        return self.valName


class Phone(Field):  # Клас для телефону
    def __init__(self, valPhone) -> None:
        self.valPhone = valPhone

    def phone_validation(self):  # Валідація номеру телефону
        # Перевірка номера телефону
        if isinstance(self.valPhone, str) and len(self.valPhone) == 13 and self.valPhone.startswith("+380"):
            return self.valPhone  # Повертаю перевірений телефон
        else:
            return print("Wrong phone format")


class Birthday(Field):  # Клас для дати народження
    def __init__(self, valBirthday):
        self.valBirthday = valBirthday

    def birthday_validation(self):  # Валідація дати народження
        try:
            # Додаю до рядка результат пошуку елементів врядку
            validBirt = "".join(re.findall(
                "\\d{2}\\.\\d{2}\\.\\d{4}", self.valBirthday))
            # Пробую перетворити ДН з словника в об'єкт datetime
            self.lBirthday = datetime.strptime(validBirt, '%d.%m.%Y').date()
            # Повертаю об'єкт datetime з методом isoformat()
            return self.lBirthday.isoformat()

        except ValueError:
            # Виводжу помилку
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Email(Field):  # Валідація пошти-----------------------------
    def __init__(self, valEmail):
        self.valEmail = valEmail
        print(self.valEmail)

    def email_validation(self):
        # --------------------------------
        email_regex = r'^[a-zA-Z0-9]{1}[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(email_regex, self.valEmail):
            return self.valEmail  # Вертаю почту
        else:
            raise ValueError("Invalid Email")  # Вертаю помилку


class Record:  # Шаблон користувача

    """Клас `Record` для зберігання інформації про контакт.
    Типу форма для словника.
    Можна вказати додаткові
        обов'язкові параметри до контакту
        які будуть записуватись в AddressBook
    """

    def __init__(self, name):
        self.name = name  # Зберігаю обєкт імені
        self.phones = None  # Список для телефонів
        self.birthday = None  # День народження
        self.dictREC = {}  # Вихідний словник

    def dict_record(self):  # Метод для створення словника
        self.dictREC = {self.name: {  # Записую в словник
            "contacts": {
                "phone": [self.phones],
                "birthday": self.birthday
            },
            "notes": {
                'Note1': 'Text1',
                'Note2': 'Text2',
            }
        }}
        return self.dictREC  # Вертаю словник
