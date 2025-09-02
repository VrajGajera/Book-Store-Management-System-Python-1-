class BookStore:
    def __init__(self):
        self.defaultId1 = 1220
        self.defaultId2 = 1229
        self.defaultPassword1 = 3445
        self.defaultPassword2 = 3449
        self.bookName = ""
        self.bookGenre = ""
        self.bookAuthor = ""
        self.bookId = 0
        self.bookQuantity = 0
        self.shipping = 50
        self.bookPrice = 0
        self.books = []

        print("\n*******Welcome To Book Store********")
        self.storedStock()  # Initialize books when creating the store

    def storedStock(self):
        # All the books in the store are stored here...
        self.books = [
            {'bookId': 1, 'bookName': 'Sherlock Holmes', 'bookGenre': 'Mystery', 'bookAuthor': 'Arthur Conan Doyle', 'bookQuantity': 87, 'bookPrice': 370},
            {'bookId': 2, 'bookName': 'The Underground Railroad', 'bookGenre': 'Fiction', 'bookAuthor': 'Colson Whitehead', 'bookQuantity': 66, 'bookPrice': 190},
            {'bookId': 3, 'bookName': 'City of Spells', 'bookGenre': 'Fantasy', 'bookAuthor': 'Alexandra Christo', 'bookQuantity': 39, 'bookPrice': 210},
            {'bookId': 4, 'bookName': 'Harlem Shuffle', 'bookGenre': 'Mystery', 'bookAuthor': 'Colson Whitehead', 'bookQuantity': 30, 'bookPrice': 299},
            {'bookId': 5, 'bookName': 'The Queen of Nothing', 'bookGenre': 'Fantasy', 'bookAuthor': 'Holly Black', 'bookQuantity': 32, 'bookPrice': 150},
            {'bookId': 6, 'bookName': 'Shivaji: The Great Maratha', 'bookGenre': 'History', 'bookAuthor': 'Ranjit Desai', 'bookQuantity': 40, 'bookPrice': 300},
            {'bookId': 7, 'bookName': 'Into the Crooked Place', 'bookGenre': 'Mystery', 'bookAuthor': 'Alexandra Christo', 'bookQuantity': 100, 'bookPrice': 289}
        ]

    def adminPage(self):
        # Admin login logic
        try:
            adminId = int(input("Enter your Id: "))
            if adminId == self.defaultId1 or adminId == self.defaultId2:
                self.password()
            else:
                print("User Not Found")
                self.adminPage()
        except ValueError:
            print("Please enter a valid numeric ID")
            self.adminPage()

    def password(self):
        # Admin password verification
        try:
            adminPassword = int(input("Please enter your Password: "))
            if adminPassword == self.defaultPassword1 or adminPassword == self.defaultPassword2:
                self.adminUse()
            else:
                print("Incorrect Password")
                self.password()
        except ValueError:
            print("Please enter a valid numeric password")
            self.password()

    def adminUse(self):
        # Admin menu for stock checking and updating
        print("Enter Value to Select")
        print("1.) Check Stock \n2.) Update Stock \n3.) Return to Main Menu")
        try:
            adminselect = int(input())
            if adminselect == 1:
                self.checkStock()
            elif adminselect == 2:
                self.updateStock()
            elif adminselect == 3:
                print("Returning to main menu...")
                return  # Return to main menu instead of exiting
            else:
                print("Enter Valid Input")
                self.adminUse()
        except ValueError:
            print("Please enter a valid option")
            self.adminUse()

    def checkStock(self):
        # Admin check stock menu
        print("Enter Value to Select")
        print("1.) Display Whole Stock \n2.) Display Searched Book ID Stock \n3.) Back \n4.) Return to Main Menu")
        try:
            select = int(input())
            if select == 1:
                self.displayFull()
            elif select == 2:
                self.displaySearched()
            elif select == 3:
                self.adminUse()
            elif select == 4:
                print("Returning to main menu...")
                return  # Return to main menu instead of exiting
            else:
                print("Enter Valid Input")
                self.checkStock()
        except ValueError:
            print("Please enter a valid option")
            self.checkStock()

    def displayFull(self):
        # Display all books in stock
        for book in self.books:
            print(f"Book Id: {book['bookId']}")
            print(f"Book Name: {book['bookName']}")
            print(f"Book Author: {book['bookAuthor']}")
            print(f"Book Genre: {book['bookGenre']}")
            print(f"Book Quantity: {book['bookQuantity']}")
            print(f"Book Price: {book['bookPrice']}")
            print()

        self.checkStock()

    def displaySearched(self):
        # Search and display book by ID
        try:
            search = int(input("Enter Book Id You Want to Search: "))
            found = False
            for book in self.books:
                if search == book['bookId']:
                    self.displayBook(book)
                    found = True
                    break
            if not found:
                print("Book Not Found")
            self.checkStock()
        except ValueError:
            print("Please enter a valid Book ID")
            self.displaySearched()

    def displayBook(self, book):
        # Display book details
        print(f"Book ID: {book['bookId']}")
        print(f"Book Name: {book['bookName']}")
        print(f"Book Author: {book['bookAuthor']}")
        print(f"Book Genre: {book['bookGenre']}")
        print(f"Book Quantity: {book['bookQuantity']}")
        print(f"Price: {book['bookPrice']}")
        print()

    def updateStock(self):
        # Admin update stock menu
        print("Enter value to select")
        print("1.) Add new stock")
        print("2.) Add Quantity")
        print("3.) Back")
        try:
            uselect = int(input())
            if uselect == 1:
                self.newAdd()
            elif uselect == 2:
                self.addQuantity()
            elif uselect == 3:
                self.adminUse()
            else:
                print("Enter Valid Input")
                self.updateStock()
        except ValueError:
            print("Please enter a valid option")
            self.updateStock()

    def newAdd(self):
        # Add a new book
        try:
            book_id = int(input("Enter Book ID: "))
            # Check if book ID already exists
            for book in self.books:
                if book['bookId'] == book_id:
                    print("Book ID already exists. Please use a different ID.")
                    return self.newAdd()
            
            book = {
                'bookId': book_id,
                'bookName': input("Enter Book Name: "),
                'bookAuthor': input("Enter Author's Name: "),
                'bookGenre': input("Enter Book Genre: "),
                'bookQuantity': int(input("Enter Book Quantity: ")),
                'bookPrice': float(input("Enter Book Price: "))
            }
            self.books.append(book)
            print("Book Added Successfully")
            self.adminUse()
        except ValueError:
            print("Please enter valid numeric values for ID, Quantity and Price")
            self.newAdd()

    def addQuantity(self):
        # Add quantity to an existing book
        try:
            add = int(input("Enter id of book you want to add: "))
            found = False
            for book in self.books:
                if add == book['bookId']:
                    additional_quantity = int(input("Enter quantity you want to add: "))
                    if additional_quantity <= 0:
                        print("Please enter a positive quantity")
                        return self.addQuantity()
                    book['bookQuantity'] += additional_quantity
                    print(f"Updated Quantity: {book['bookQuantity']}")
                    self.displayBook(book)
                    found = True
                    break
            if not found:
                print("Book Not Found")
            self.updateStock()
        except ValueError:
            print("Please enter valid numeric values")
            self.addQuantity()


class Customer(BookStore):
    def __init__(self):
        super().__init__()
        self.mailId1 = "vrajgajera430@gmail.com"
        self.mailId2 = "ABC@gmail.com"
        self.password1 = 1200
        self.password2 = 3410
        self.discountPrice = 0
        self.coupon = "READ10"

    def customerwelcome(self):
        # Customer login/signup
        print("\n*******Welcome To Customer Page********")
        print("1.) Already a User (Log In) \n2.) New User (Sign Up) \n3.) Return to Main Menu")
        try:
            select = int(input())
            if select == 1:
                self.logIn()
            elif select == 2:
                self.signUp()
            elif select == 3:
                print("Returning to main menu...")
                return  # Return to main menu
            else:
                print("Invalid option. Please try again.")
                self.customerwelcome()
        except ValueError:
            print("Please enter a valid option")
            self.customerwelcome()

    def logIn(self):
        # Customer login
        mail = input("Enter your Mail Id (or type 'back' to return): ")
        if mail.lower() == 'back':
            self.customerwelcome()
            return
        if mail == self.mailId1 or mail == self.mailId2:
            try:
                password = int(input("Enter your password: "))
                if password == self.password1 or password == self.password2:
                    print("Log In successful")
                    self.customerPage()
                else:
                    print("Incorrect Password...Try Again")
                    self.logIn()
            except ValueError:
                print("Please enter a valid numeric password")
                self.logIn()
        else:
            print("Mail Id not Found")
            self.logIn()

    def signUp(self):
        # Customer sign up
        mail = input("Enter your Mail Id (or type 'back' to return): ")
        if mail.lower() == 'back':
            self.customerwelcome()
            return
        if '@' in mail and '.' in mail:  # Better email validation
            try:
                password = int(input("Set Password (Only 4 digit number accepted): "))
                if 1000 <= password <= 9999:
                    confirmPassword = int(input("Confirm Password: "))
                    if confirmPassword == password:
                        # Store the new credentials
                        self.mailId2 = mail
                        self.password2 = password
                        print("Sign Up Successful")
                        self.customerPage()
                    else:
                        print("Passwords do not match!")
                        self.signUp()
                else:
                    print("Password must be a 4 digit number.")
                    self.signUp()
            except ValueError:
                print("Please enter a valid numeric password")
                self.signUp()
        else:
            print("Invalid Email ID. Must contain @ and a domain.")
            self.signUp()

    def customerPage(self):
        # Customer page
        print("Enter value to select")
        print("1.) Display All Available Books \n2.) Search for Books \n3.) Return to Main Menu")
        try:
            select = int(input())
            if select == 1:
                for book in self.books:
                    self.displayBook(book)
                self.buy()
            elif select == 2:
                self.searchBook()
            elif select == 3:
                print("Returning to main menu...")
                return  # Return to main menu
            else:
                print("Invalid option. Please try again.")
                self.customerPage()
        except ValueError:
            print("Please enter a valid option")
            self.customerPage()

    def searchBook(self):
        # Search books by Author or Genre
        print("Search By...")
        print("1.) Author \n2.) Genre \n3.) Back")
        try:
            select = int(input())
            if select == 1:
                self.availableAuthors()
            elif select == 2:
                self.availableGenre()
            elif select == 3:
                self.customerPage()
            else:
                print("Invalid option. Please try again.")
                self.searchBook()
        except ValueError:
            print("Please enter a valid option")
            self.searchBook()

    def availableAuthors(self):
        # Display books by available authors
        print("Available Authors")
        print("1.) Arthur Conan Doyle \n2.) Colson Whitehead\n3.) Alexandra Christo \n4.) Holly Black \n5.) Ranjit Desai \n6.) Back")
        try:
            select = int(input())
            if select == 1:
                self.getAcd()
            elif select == 2:
                self.getCw()
            elif select == 3:
                self.getAc()
            elif select == 4:
                self.getHb()
            elif select == 5:
                self.getRd()
            elif select == 6:
                self.searchBook()
            else:
                print("Invalid option. Please try again.")
                self.availableAuthors()
        except ValueError:
            print("Please enter a valid option")
            self.availableAuthors()

    def getAcd(self):
        # Display books by Arthur Conan Doyle
        self.displayBooksByAuthor("Arthur Conan Doyle")
        self.buy()

    def getCw(self):
        # Display books by Colson Whitehead
        self.displayBooksByAuthor("Colson Whitehead")
        self.buy()

    def getAc(self):
        # Display books by Alexandra Christo
        self.displayBooksByAuthor("Alexandra Christo")
        self.buy()

    def getHb(self):
        # Display books by Holly Black
        self.displayBooksByAuthor("Holly Black")
        self.buy()

    def getRd(self):
        # Display books by Ranjit Desai
        self.displayBooksByAuthor("Ranjit Desai")
        self.buy()

    def displayBooksByAuthor(self, author_name):
        # Display books by a given author
        print(f"Books by {author_name}")
        found = False
        for book in self.books:
            if book['bookAuthor'] == author_name:
                self.displayBook(book)
                found = True
        if not found:
            print(f"No books found by {author_name}")

    def availableGenre(self):
        # Display available genres
        print("Available Genres")
        print("1.) Mystery \n2.) Fiction \n3.) Fantasy \n4.) History \n5.) Back")
        try:
            select = int(input())
            if select == 1:
                self.getMystery()
            elif select == 2:
                self.getFiction()
            elif select == 3:
                self.getFantasy()
            elif select == 4:
                self.getHistory()
            elif select == 5:
                self.searchBook()
            else:
                print("Invalid option. Please try again.")
                self.availableGenre()
        except ValueError:
            print("Please enter a valid option")
            self.availableGenre()

    def getMystery(self):
        # Display Mystery genre books
        self.displayBooksByGenre("Mystery")
        self.buy()

    def getFiction(self):
        # Display Fiction genre books
        self.displayBooksByGenre("Fiction")
        self.buy()

    def getFantasy(self):
        # Display Fantasy genre books
        self.displayBooksByGenre("Fantasy")
        self.buy()

    def getHistory(self):
        # Display History genre books
        self.displayBooksByGenre("History")
        self.buy()

    def displayBooksByGenre(self, genre_name):
        # Display books by genre
        print(f"Books of {genre_name} genre")
        found = False
        for book in self.books:
            if book['bookGenre'] == genre_name:
                self.displayBook(book)
                found = True
        if not found:
            print(f"No books found in {genre_name} genre")

    def buy(self):
        # Purchase books
        print("Enter value to select")
        print("1.) Proceed to Buy \n2.) Browse More \n3.) Return to Main Menu")
        try:
            select = int(input())
            if select == 1:
                self.quantity()
            elif select == 2:
                self.customerPage()
            elif select == 3:
                print("Returning to main menu...")
                return  # Return to main menu
            else:
                print("Invalid option. Please try again.")
                self.buy()
        except ValueError:
            print("Please enter a valid option")
            self.buy()

    def quantity(self):
        try:
            book_id = int(input("Enter Id of the book you want to purchase (or 0 to go back): "))
            if book_id == 0:
                return self.buy()
                
            book = next((b for b in self.books if b['bookId'] == book_id), None)
            
            if book is None:
                print("Book ID not Found")
                return self.quantity()

            qty = int(input("Enter Quantity: "))
            if qty <= 0:
                print("Invalid quantity. Please enter a positive number.")
                return self.quantity()
            
            if qty > book['bookQuantity']:
                print(f"Insufficient Stock. Only {book['bookQuantity']} available.")
                return self.quantity()

            print("Do you have any Coupon Code?")
            print("1.) Yes \n2.) No")
            cc = int(input())
            discount = 0
            if cc == 1:
                code = input("Enter your Coupon Code: ")
                if code == self.coupon:
                    discount = book['bookPrice'] * 0.1
                    print(f"Coupon applied! 10% discount: {discount} per book")
                else:
                    print("Invalid coupon code")
            
            # Update book quantity after purchase
            book['bookQuantity'] -= qty
            
            total_price = (book['bookPrice'] - discount) * qty + self.shipping
            print("\n********YOUR BILL********")
            print(f"Book Name: {book['bookName']}")
            print(f"Quantity: {qty}")
            print(f"Price per book: {book['bookPrice']}")
            print(f"Discount per book: {discount}")
            print(f"Shipping Fee: {self.shipping}")
            print(f"Total Price: {total_price}")
            print("\n******THANK YOU FOR SHOPPING*****")
            
            print("\nWhat would you like to do next?")
            print("1.) Continue Shopping \n2.) Back Home Page")
            next_action = int(input())
            if next_action == 1:
                self.customerPage()
            else:
                print("Thank you for Visit the Book Store. Goodbye!")
                exit()
        except ValueError:
            print("Invalid input. Please enter numeric values only.")
            return self.quantity()


def main():
    # First create a bookstore
    store = BookStore()
    
    # Create a customer with inheritance from BookStore
    customer = Customer()
    
    while True:
        print("\n=== Book Store Main Menu ===")
        print("1.) Admin Login")
        print("2.) Customer Login")
        print("3.) Exit Program")
        
        try:
            select = int(input())
            if select == 1:
                store.adminPage()
            elif select == 2:
                customer.customerwelcome()
            elif select == 3:
                print("Thank you for Visit the Book Store. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Please enter a valid option")

if __name__ == "__main__":
    main()
    