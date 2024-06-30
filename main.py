def work_with_phonebook():
	

    choice = show_menu()

    phone_book = read_txt('phon.txt')

    while (choice != 10):

        if choice == 1:
            print(phone_book)
        elif choice == 2:
            last_name = input('Какую фамилию найти? ')
            print(find_by_lastname(phone_book,last_name))
        elif choice == 3:
            number=input('Какой номер найти? ')
            print(find_by_number(phone_book,number))
        elif choice == 4:
            lastname = input('Введите фамилию: ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice == 5:
            print(add_number(phone_book))
        elif choice == 6:
            save_phonebook_to_txt(phone_book, 'phon.txt')
        elif choice == 7:
            write_txt('phonebook.txt',phone_book)
        elif choice == 8:
            line_number = int(input("Введите номер строки для копирования: "))
            filename_destination = input("Введите имя файла назначения: ")
            copy_line_to_file(phone_book, line_number, filename_destination)
            print("Данные успешно скопированы.")
            input("Press Enter to continue...")
        elif choice == 9:
            exit()

        choice = show_menu()


def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Удалить абонента из справочника\n"
		  "5. Добавить абонента в справочник\n"
          "6. Сохранить справочник в текстовом формате\n"
          "7. Закончить работу и сохранить\n"
          "8. Скопировать данные в другой файл\n"
          "9. Выход без сохранения")
    choice1 = int(input())
    return choice1
    

#Иванов,	Иван,	111,	Занял сотку
#Петров,	Петр,	222,	Взводный в танках
#Васичкина,	Василиса,	333,	Не брать
#Питонов,	Антон,	777,	Кореш
#Рафтова,	Ириска,	555,	Соседка


#1
def read_txt(filename): 

    phone_book = []

    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

#line.split(',') = [Питонов,	Антон,	777,	Кореш]

    with open(filename,'r',encoding='utf-8') as phb:

        for line in phb:
            
            record = dict(zip(fields, line.split(',')))
        
			#dict(( (Фамилия, Иванов),(Имя, Иван),(Номер, 111),(Описание, Занял сотку)))
            phone_book.append(record)
    
    return phone_book


#2
def find_by_lastname(phone_book, last_name):
    for i in range(len(phone_book)):
        if phone_book[i]["Фамилия"] == last_name:
            return phone_book[i]
    return "Абонент не найден:("


#3
def find_by_number(phone_book, number):
    for i in range(len(phone_book)):
        if phone_book[i]["Телефон"] == number:
            return phone_book[i]
    return "Номер телефона не найден:("


#4
def delete_by_lastname(phone_book,lastname):
    for i in range(len(phone_book)):
        if phone_book[i]["Фамилия"] == lastname:
            del phone_book[i]
            return f"Абонент {lastname} удален"
    return "Абонент не найден:("
  

#5
def add_number(phone_book):
    lastname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    number = input("Введите номер: ")
    description = input("Введите описание: ")
    new_entry = {'Фамилия': lastname, 'Имя': name, 'Телефон': number, 'Описание': description}
    phone_book.append(new_entry)
    return f"Абонент {lastname} {name} добавлен"


#6
def save_phonebook_to_txt(phone_book, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for entry in phone_book:
            file.write('{},{},{},{}\n'.format(entry['Фамилия'], entry['Имя'], entry['Телефон'], entry['Описание']))


#7
def write_txt(filename , phone_book):

    with open(filename,'w',encoding='utf-8') as phout:

        for i in range(len(phone_book)):

            s=''
            for v in phone_book[i].values():

                s = s + v + ','

            phout.write(f'{s[:-1]}\n')

#W  A

#x = 10

#x = x + 5


#8
def copy_line_to_file(phone_book, line_number, filename_destination):
    if 1 <= line_number <= len(phone_book):
        entry = phone_book[line_number - 1]
        with open(filename_destination, "a", encoding="utf-8") as file:
            file.write(
            f"{entry['Фамилия']},{entry['Имя']},{entry['Телефон']},{entry['Описание']}\n"
            )
    else:
        print("Неверный номер строки")


work_with_phonebook()