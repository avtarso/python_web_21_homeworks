try:
    from classes.record import Record
    from classes.addressbook import AddressBook
    from classes.notes import Notes
    from classes.menu import AddressBookOutput
    from functions.functions import make_menu
    from functions.make_header import make_header
    from functions.sort import sort
    from settings.settings import addressbook_filename, notes_filename
    import classes.menu
except ModuleNotFoundError:
    from personal_assistant_bot.classes.record import Record
    from personal_assistant_bot.classes.addressbook import AddressBook
    from personal_assistant_bot.classes.notes import Notes
    from personal_assistant_bot.classes.menu import AddressBookOutput
    from personal_assistant_bot.functions.functions import make_menu
    from personal_assistant_bot.functions.make_header import make_header
    from personal_assistant_bot.functions.sort import sort
    from personal_assistant_bot.settings.settings import addressbook_filename, notes_filename
    import personal_assistant_bot.classes.menu


from colorama import init, Fore
init(autoreset=True)


def main():
    
    while True:

        choice1 = classes.menu.Menu.message()

        if choice1 == "1":
            classes.menu.MenuAbout.message()

        elif choice1 == "2":
            classes.menu.MenuHello.message()

        elif choice1 == "3":
            book = AddressBookOutput()
            switcher = True                
            while switcher:
                
                choice2 = AddressBookOutput.message()
                book = book.read_contacts_from_file(addressbook_filename)

                if choice2 == "1":
                    book.show_all_records()

                elif choice2 == "2":
                    book.find_records()

                elif choice2 == "3":
                    book.days_from_birthday()
                
                elif choice2 == "4":
                    book.add_record_output()

                elif choice2 == "5":
                    book.record_edit()

                elif choice2 == "6":
                    book.record_delete()

                elif choice2 == "7":
                    book.save()

                elif choice2 == "0":
                    switcher = False

        elif choice1 == "4":
            notes = Notes().load_from_file(notes_filename)
            make_menu(notes)
        
        elif choice1 == "5":
            classes.menu.MenuSort.message()

        elif choice1 == "0":
            break


if __name__ == '__main__':
    main()
