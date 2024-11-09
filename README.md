Example BOT_V2(r) Version 1.0 08/11/2024
author - "Prolisok team"
===================

GENERAL USAGE NOTES
===================
<p>Current BOT_V2 version is installable and runnable on WIN and GNU-Linux platforms. Functionality on Mac-OS
platforms was not tested.</p>

USAGE NOTES
==================

BOT_V2 can be used for saving, editing and deleting contacts in format: Name, Phone, eMail, address. Optionally, it can be used for notes saving and editing. 

<p><b>Команди для контактів (commands for contacts editing):</b></p>
 <ol><li>"hello" -> Привітання (just hello)</li>
 <li>"add [name]" -> Створити контакт (create contact)</li>
 <li>"all" -> Вивести всі контакти з словниками (show all contacts)</li>
 <li>"user [name]" -> Вивести дані користувача (chow contact`s info)</li>
<li>"add-phone [ім'я] [номер телефону]" -> Додати номер телефону контакту (add phone to contact`s info)</li>
<li>"show-phone [ім'я]" -> Вивести номер телефону контакту (show contact`s phone)</li>
<li>"add-birthday [ім'я] [дата народження]" -> Додати до контакту день народження (add birth date to contact`s info)</li>
 <li>"show-birthday [ім'я]" -> Показати день народження контакту (show contact`s birth date)</li>
<li>"birthdays" -> Показати список контактів, які матимуть день народження в наступні n днів (show list of contacts, whos birthday will be next n days)</li>
<li>"add-email [ім'я] [Email]" -> Додати адресу електронної пошти контакту (add eMail tot contact`s info)</li>
 <li>"show-email [name]" -> Вивести адресу електронної пошти контакту (show contact`s eMail)</li>
 <li>"add-addres [name] [sity]" -> Додати адресу контакту (add address to contact`s info)</li>
 <li>"show-addres [name]" -> Вивести адресу контакту (show contact`s address)</li>
 <li>"remove-user [ім'я]" -> Видалити контакт (remove contact)</li>
<li>"open-book [link to file]" -> Відкрити збережену книгу контактів (open existing contacts book)</li>
 <li>"exit" -> Закрити програму із збереженням даних (save datas and close app)</li>
<li>"close" -> Закрити програму без збереження даних (close app without saving)</li>
<li>"help" -> Вивести всі доступні команди (show all commands)</li>
<li>"save" -> Зберегти книгу контактів (save contact book)</li>
<li>"text-color [color]" -> Вибрати колір тексту (choose color of output)</li></ol>
<p><b>Команди для нотаток (commands for notes editing):</b></p>
 <ol><li>"note [name] [coment] [notes]" -> Додати нотатки до запису контакту (редагувати існуючі) (add notes to contact`s info)</li>
<li>"view-notes [name]" -> Вивести нотатки, пов'язані з контактом (show contact-linked notes)</li>
<li>"view-all-notes" -> Вивести всі нотатки (show all notes)</li>
 <li>"remove-notes-all [name]" -> Видаляє всі нотати, пов'язані з контактом (remove notes which linked with particular contact)</li>
<li>"remove-note [name] [comment]" -> Видаляє конкретну нотатку, пов'язану з контактом (remove particular note which linked with particular contact)</li></ol>
 
<p><b>Команди для тегів (commands for tegs editing):</b></p>
 <ol><li>"add-tag [name] [tag]" -> Додає тег до контакту (add tag to contact`s info)</li>
<li>"tag-user [tag]" -> Шукає контакт за тегом (search contact by given tag)</li></ol>


INSTALLATION AND PREREQUISITES
==============================

Colorama library must be installed

BOT_V2 can be used:
  <ul>
  <li>as portable app:</li>
	<ol><li>by CLI: <code>python ./path/to/app/project_virtual_assistant_by_Prolisok_team-Future_SetUp/src/bot_v2/main.py</code></li>
  	<li>by GUI: functionality not implemented yet</li></ol>
  <li>as installed app:
	<ol><li>by CLI (WIN, most Linux distros): <code>pip install ./path/to/app/project_virtual_assistant_by_Prolisok_team-Future_SetUp</code></li>
  	<li>by CLI (Arch-based Linux distros): <code>pipx install ./path/to/app/project_virtual_assistant_by_Prolisok_team-Future_SetUp</code></li>
	<li>by GUI: functionality not implemented yet</li></ol></ul>


CONTACTS AND LICENSE INFO
===================
Example BOT_v2 can be reached at:

email - alex.iesypenko@gmail.com


voice - +38 (000) 000 00 00


BOT_v2 example can be used, shared and changed in compliance with the terms of MIT license agreement.

