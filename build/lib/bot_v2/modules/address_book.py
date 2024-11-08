from datetime import datetime
from collections import UserDict
import re


class AddressBook(UserDict):  # Клас для словника

    def add_record(self, data):  # Метод для додавання словника до self.data
        """ Метод запису даних до UserDict """
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



    def find_data_user(self, findValue, findName=None):
        """ 
        Метод пошуку даних користувача в UserDict,
        (val, name=None)
        """
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


    def find_tags_users(self, tagVal, tagNam):
        """ 
        Метод пошуку користувача за тегом
        """
        for tg in self.data:  # Пробігаюсь циклом по словнику
            if self.data[tg].get(tagVal):  # Шукаю 'теги' в словниках користувачів
                # Зберігаю знайдений тег з словника
                dtu = str(dict(self.data[tg])[tagVal])
                if tagNam == dtu:  # Роблю перевірку за тегом
                    return print(dtu, tg)  # Виводжу результат пошуку за тегом



    def add_data_to_users(self, dUser, newData, addNewData):
        """ 
        Метод додавання нових даних до словника користувача,
        (user, key, val)
        """
        # Роблю перевірку на співпадіння в поточному словнику користувачів UserDict
        if self.data.get(dUser):
            # Зберігаю словник користувача з UserDict
            userData = dict(self.data[dUser])
            # Оновлюю словник користувача <- вхідним словником
            userData.update({newData: addNewData})
            # Оновлюю словник користувача в UserDict
            super().update({dUser: userData})
            print("Data has been updated")



    def update_user_contacts(self, uUser, uDat=None):
        """ 
        Метод для оновлення/додавання даних до користувача
        (user, data: dict)
        """
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




    def add_notes_to_users(self, nUser, notes):
        """ 
        Метод для оновлення/додавання нотаток користувача
        Приймає список(user, [comentars , notate])
        """
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



    def delete_data_users(self, ddName, keyData, ddData=None):
        """ 
        Метод видалення даних користувача.
        Приймає ім'я, ключ для даних, дані(що видаляються)
        """
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




    def find_birthday_users(self, period: int): # birthdays
        """ 
        Метод для виведення днів народження на задану кількість днів.
        """
        try:
            today_time = datetime.today().date() #Зберігаю поточну дату
            dict_res = {} #Словник для результату пошуку
            
            for ur in self.data: #Проходжусь по словнику UserDict
                users_dicts = dict(self.data[ur])["contacts"] #Зберігаю словник користувача
                
                if users_dicts.get("birthday"): #Роблю перевірку наявність дати народження
                    birtDT = datetime.strptime(users_dicts["birthday"], '%Y-%m-%d').date() #Перетворюю ДН з словника в об'єкт datetime
                    repYear = birtDT.replace(year=today_time.year) #Замінюю рік з ДН на поточний
                    
                    ###___________________________________???????????????
                    res_bird = int(( repYear - today_time ).days) #Віднімаю ДН від поточної дати і зберігаю як int
                    
                    if res_bird < period and res_bird > 0: #Роблю перевірку по періоду
                        dict_res.update({ur: birtDT.isoformat()}) #Додаю до словника результатат перевірки 
                        
            return dict_res #Повертаю словник з результатом пошуку
        
        except: print("Wrong date in the dictionary") #Виводжу повідомлення якщо є помилкова дата народження в словнику



class Field():
    """ 
    Базовий клас для валідації даних про користувача
    """
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


class Email(Field):  # Валідація пошти
    def __init__(self, valEmail):
        self.valEmail = valEmail
        print(self.valEmail)

    def email_validation(self): # Валідація Email
        email_regex = r'^[a-zA-Z0-9]{1}[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(email_regex, self.valEmail):
            return self.valEmail  # Вертаю пошту
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
