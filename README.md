Example BOT_V2(r) Version 1.0 08/11/2024
author - "Prolisok team"


GENERAL USAGE NOTES
===================
- Current BOT_V2 version is installable and runnable
  on WIN and GNU-Linux platforms. Functionality on Mac-OS
  platforms was not tested.


USAGE NOTES
==================

BOT_V2 can be used for saving, editing and deleting contacts in format: Name, Phone, eMail, address. Optionally, it can be used for notes saving and editing. 

Команди для контактів (commands for contacts editing):
 1 - "hello" -> Привітання (just hello)
 2 - "add [name]" -> Створити контакт (create contact)
 3 - "all" -> Вивести всі контакти з словниками (show all contacts)
 4 - "user [name]" -> Вивести дані користувача (chow contact`s info)
 5 - "add-phone [ім'я] [номер телефону]" -> Додати номер телефону контакту (add phone to contact`s info)
 6 - "show-phone [ім'я]" -> Вивести номер телефону контакту (show contact`s phone)
 7 - "add-birthday [ім'я] [дата народження]" -> Додати до контакту день народження (add birth date to contact`s info)
 8 - "show-birthday [ім'я]" -> Показати день народження контакту (show contact`s birth date)
 9 - "birthdays" -> Показати список контактів, які матимуть день народження в наступні n днів (show list of contacts, whos birthday will be next n days)
 10 - "add-email [ім'я] [Email]" -> Додати адресу електронної пошти контакту (add eMail tot contact`s info)
 11 - "show-email [name]" -> Вивести адресу електронної пошти контакту (show contact`s eMail)
 12 - "add-addres [name] [sity]" -> Додати адресу контакту (add address to contact`s info)
 13 - "show-addres [name]" -> Вивести адресу контакту (show contact`s address)
 14 - "remove-user [ім'я]" -> Видалити контакт (remove contact)
 
 15 - "open-book [link to file]" -> Відкрити збережену книгу контактів (open existing contacts book)
 16 - "exit" -> Закрити програму із збереженням даних (save datas and close app) 
 17 - "close" -> Закрити програму без збереження даних (close app without saving)
 18 - "help" -> Вивести всі доступні команди (show all commands)
 19 - "save" -> Зберегти книгу контактів (save contact book)

 20 - "text-color [color]" -> Вибрати колір тексту (choose color of output)

Команди для нотатків (commands for notes editing):
 1 - "note [name] [coment] [notes]" -> Додати нотатки до запису контакту (редагувати існуючі) (add notes to contact`s info)
 2 - "view-notes [name]" -> Вивести нотатки, пов'язані з контактом (show contact-linked notes)
 3 - "view-all-notes" -> Вивести всі нотатки (show all notes)
 4 - "remove-notes-all [name]" -> Видаляє всі нотати, пов'язані з контактом (remove notes which linked with particular contact)
 5 - "remove-note [name] [comment]" -> Видаляє конкретну нотатку, пов'язану з контактом (remove particular note which linked with particular contact)
 
Команди для тегів (commands for tegs editing): 
 1 - "add-tag [name] [tag]" -> Додає тег до контакту (add tag to contact`s info)
 2 - "tag-user [tag]" -> Шукає контакт за тегом (search contact by given tag)


INSTALLATION AND PREREQUISITES
==============================

Colorama library must be installed

BOT_V2 can be used:
  
  - as portable app:
	by CLI: python ./path/to/app/project_virtual_assistant_by_Prolisok_team-Future_SetUp/src/bot_v2/main.py
  	by GUI: functionality not implemented yet
  - as installed app:
	by CLI (WIN, most Linux distros): pip install ./path/to/app/project_virtual_assistant_by_Prolisok_team-Future_SetUp
  	by CLI (Arch-based Linux distros): pipx install ./path/to/app/project_virtual_assistant_by_Prolisok_team-Future_SetUp
	by GUI: functionality not implemented yet


CONTACTS AND LICENSE INFO
===================
Example BOT_v2 can be reached at:

email - alex.iesypenko@gmail.com
voice - +38 (000) 000 00 00


BOT_v2 example can be used, shared and changed in compliance with the terms of MIT license agreement.

