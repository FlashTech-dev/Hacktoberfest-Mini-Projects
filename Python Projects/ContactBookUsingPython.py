# ContactBook class 
class ContactBook:
    def __init__(self):
        self.names = []
        self.phone_numbers = []
        
    def contactBook(self): #contactbook main screen
        print("*****Welcome to Contact Book****".center(35))
        if (len(self.names) > 0):
            print("\nName\t\t\tPhone Number\n")

            for i in range(len(self.names)):
                print("{}\t\t\t{}".format(self.names[i], self.phone_numbers[i]))
        else:
            print("")
        print("Which operation would you like to perform: ")
        self.repeat()
        
    def display_contact(self): #to display contacts only
        print("*****Contacts****".center(25))
        if (len(self.names) > 0):
            print("\nName\t\t\tPhone Number\n")

            for i in range(len(self.names)):
                print("{}\t\t\t{}".format(self.names[i], self.phone_numbers[i]))
        else:
            print("\nName\t\t\tPhone Number\n")
            print("---- ------\t\t----------")
            print("\nResult: No contacts avialable")
        choice = str(input("\n-Would you like to continue(y/n): "))
        if choice.lower() == 'y':
            self.repeat()
        else:
            self.terminate()
            
    def insert_contact(self): # to insert contacts
        no_of_contacts = int(input("No of contacts you wants to insert: "))
        for _ in range(no_of_contacts):
            name = input("Name: ")
            phone_number = input("Phone Number: ")
            self.names.append(name)
            self.phone_numbers.append(phone_number)
        choice = str(input("\n-Would you like to continue(y/n): "))
        if choice.lower() == 'y':
            self.repeat()
        else:
            self.terminate()
            
    def search_contact(self): # to search contacts by name or phone number
        if len(self.names) > 0:
            search_term = input("\nEnter search term: ")

            print("Search result: ")
            if search_term in self.names:
                index = self.names.index(search_term)
                phone_number = self.phone_numbers[index]
                print("Name {}, Phone Number: {}".format(search_term, phone_number))
            else:
                print("Name Not found")
        else:
            print("\nName\t\t\tPhone Number\n")
            print("---- ------\t\t----------")
            print("\nResult: No contacts exists to search")
        choice = str(input("\n-Would you like to continue(y/n): "))
        if choice.lower() == 'y':
            self.repeat()
        else:
            self.terminate()
        
    def terminate(self): # terminate the program
        return None
    
    def repeat(self): # for repeating the program
        print("-----------------------------------".center(35))
        print("   Operations")
        print("1. Display Contact Book\n2. Insert contacts\n3. Search contact by name or number\n4. exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            self.display_contact()
        elif choice == 2:
            self.insert_contact()
        elif choice == 3:
            self.search_contact()
        elif choice == 4:
            self.terminate()
        else:
            print("Not valid input!!!")
            self.repeat()
            

# Driver Code
if __name__=="__main__":
    cb = ContactBook()
    cb.contactBook()
