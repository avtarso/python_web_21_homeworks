try:
    from classes.field import Field
    from classes.abstractoutput import AbstractOutput
    from classes.name import Name
    from classes.birthday import Birthday
    from classes.phone import Phone
    from classes.email import Email 
    from classes.address import Address
    from classes.record import Record
    from classes.addressbook import AddressBook
    from settings.settings import addressbook_filename, PAG
    from classes.note import Note
    from classes.notes import Notes
    from functions.functions import make_menu
    from functions.make_header import make_header
except ModuleNotFoundError:
    from personal_assistant_bot.classes.field import Field
    from personal_assistant_bot.classes.abstractoutput import AbstractOutput
    from personal_assistant_bot.classes.name import Name
    from personal_assistant_bot.classes.birthday import Birthday
    from personal_assistant_bot.classes.phone import Phone
    from personal_assistant_bot.classes.email import Email
    from personal_assistant_bot.classes.address import Address
    from personal_assistant_bot.classes.record import Record
    from personal_assistant_bot.classes.addressbook import AddressBook
    from personal_assistant_bot.functions.functions import make_menu
    from personal_assistant_bot.functions.make_header import make_header    
    from personal_assistant_bot.classes.note import Note
    from personal_assistant_bot.classes.notes import Notes
    from personal_assistant_bot.settings.settings import addressbook_filename, PAG


from colorama import init, Fore

init(autoreset=True)

def press_any_key():
    input("\nPress Enter to continue...")


class Menu(AbstractOutput):
    @classmethod
    def message(cls):
        make_header("MAIN MENU")
        return input('''
1. About Bot Helper
2. Hello, User!
3. Use Records
4. Use Notes
5. Sort Files in Folder

0. Exit

Please, input your choice: ''')
    

class MenuAbout(AbstractOutput):
    @classmethod
    def message(cls):
        make_header("ABOUT BOT HELPER")
        print("\nI'm a great bot and I will facilitate your work, now I will describe what I can do\n"
              "I can work with contact: add, edit, remove contact's phone, email, birthday, address.\nAlso "
              "I can work with your notes: add, edit, remove, show note or all notes, find and sort notes.\n"
              "And finally, I have very useful function - sort, it helps you to sort all your files in "
              "some directory. \nWhere do you want to start?")
        press_any_key()


class MenuHello(AbstractOutput):
    @classmethod
    def message(cls):
        make_header("HELLO, USER!")
        print('\nHello! How are you today? Are you ready to work?')

        press_any_key()


class AddressBookOutput(AddressBook, AbstractOutput):

    def init_book(self):
        if not self:
            self.read_contacts_from_file(addressbook_filename)
            print("breack")#
            print(self)#
            print(len(self))#
            quit()#


    @staticmethod
    def message():
        make_header("ADDESSBOOK MENU")
        return input('''
1. Show all Records
2. Find Records
3. Show Records with birthday in N days
4. Add Record
5. Edit Record
6. Delete Record
7. Save AddressBook

0. Exit to previous menu

Please, input your choice: ''')


    def show_all_records(self):
        make_header("SHOW ALL RECORDS")
        self.iterator()
        press_any_key()


    def find_records(self):
        make_header("FIND RECORDS")
        find_string = input("\nPlease input Name of record, which you want find: ")
        find_result = AddressBook()
        find_result = self.find_record(find_string)

        if find_result:
            print("")
            self.find_record(find_string).iterator_simple()
        else:
            print(Fore.RED + f"\nI can`t find any matches with '{find_string}'")

        press_any_key()


    def days_from_birthday(self):
        make_header("N DAYS FROM BIRTHDAY")
        days_to_search = input("\nPlease input number of days to search: ")
        print("")
        self.find_birthdays(days_to_search).iterator()
        press_any_key()


    def add_record_output(self):
        make_header("ADD RECORD")
        name = input("\nPlease enter the name: ")
        new_record = Record(name)

        while True:
            phone = input("Please enter the phone: ")
            try:
                new_record.add_phone(phone)
            except ValueError:
                print(Fore.RED + 'Incorrect number format. Please enter a 10-digit number.')
            else:
                break

        while True:
            email = input("Please enter the email: ")
            try:
                new_record.add_email(email)
            except ValueError:
                print(Fore.RED + 'Incorrect email format. Please enter email like user@example.com.')
            else:
                break

        address = input("Please enter the address: ")
        new_record.add_address(address)

        while True:
            birthday = input("Please enter the date of birth in format DD/MM/YYYY: ")
            try:
                new_record.add_birthday(birthday)
            except ValueError:
                print(Fore.RED + 'Waiting format of date - DD/MM/YYYY. Reinput, please.')
            else:
                break

        self.add_record(new_record)
        print(Fore.GREEN + "\nRecord added successful!\n")

        self.appruve_record(new_record)

    press_any_key()


    def record_edit(self):
        make_header("EDIT RECORD")
        self.edit_record()
        press_any_key()


    def record_delete(self):
        make_header("DELETE RECORD")
        contact_name = input("\nPlease enter contact name you need to delete: ")
        print("")
        self.delete(contact_name)
        press_any_key()


    def save(self):
        make_header("SAVE ADDRESSBOOK")
        self.write_contacts_to_file(addressbook_filename)
        print(Fore.GREEN + "\nAddressBook saved successful!")
        press_any_key()


class MenuSort(AbstractOutput):
    @classmethod
    def message(cls):
        make_header("SORT FILES IN FOLDER")
        print(Fore.RED + "\nCarefully! Files will be sorted! You won't be able to find them in your usual place!")

        folder = input("\nPlease input folder name or press Enter to exit: ")

        if not folder:
            pass
        else:
            sort(folder)

            print(Fore.GREEN + f"\nFiles and folders in {folder} sorted successful!")

            press_any_key()