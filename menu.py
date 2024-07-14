import sys
import book_dao

menu_options = { # The menu prompt
    1: 'Add a Publisher',
    2: 'Add a Book',
    3: 'Edit a Book',
    # More options to be added
    4: 'Delete a Book',
    5: 'Search Books',
    6: 'Exit',
}
search_menu_options = {# Search option prompt
    
    # To be added
    1:'All books, and search based on Title',
    2: 'Search by publisher ',
    3: 'Search by price range from min to max',
    4:'Search by title and publisher',
    5:'Search by title',
    6:'Go back'
}
def search_all_books(): # queries all the book
    results=list(book_dao.findAll())
    print("Search by Publisher:")
         # Display results
    s_format = "%-10s %-1s %-50s %-1s %-5s %-1s %-25s %-1s %-18s  %-1s %-8s " # format specifiers that indicate left-aligned fields of specific widths (10, 1, and 50 respectively)
    print(s_format % ("ISBN:", "|", "Title:","|","Year","|","Published_By","|","Previous_Edition","|","Price"))
    if len(results) == 0:
        print("N/A")
    else:
        for item in results:
            isbn = item.get('ISBN', 'N/A')  # Using 'N/A' as default if 'ISBN' is not present
            title = item.get('title', 'N/A')
            year = item.get('year', 'N/A')
            published_by = item.get('published_by', 'N/A')
            previous_edition = item.get('previous_edition', 'N/A')
            price = item.get('price', 'N/A')
            print(s_format % (isbn, "|", title, "|", year, "|", published_by, "|", previous_edition, "|", price))
           # print(s_format % (item['ISBN'], "|", item['title'],"|",item['year'],"|",item['published_by'],"|", item['previous_edition'],"|",item['price']))
    print("---End of Search Results---")
def search_by_title(): #query the title
    title = input("What is the exact book title that you are looking for?\n")
    results = list(book_dao.findByTitle(title))
        # Display results
    s_format = "%-10s %-1s %-50s %-1s %-5s %-1s %-25s %-1s %-18s  %-1s %-8s " # format specifiers that indicate left-aligned fields of specific widths (10, 1, and 50 respectively)
    print(s_format % ("ISBN:", "|", "Title:","|","Year","|","Published_By","|","Previous_Edition","|","Price"))
    if len(results) == 0:
        print("N/A")
    else:
        for item in results:
            isbn = item.get('ISBN', 'N/A')  # Using 'N/A' as default if 'ISBN' is not present
            title = item.get('title', 'N/A')
            year = item.get('year', 'N/A')
            published_by = item.get('published_by', 'N/A')
            previous_edition = item.get('previous_edition', 'N/A')
            price = item.get('price', 'N/A')
            print(s_format % (isbn, "|", title, "|", year, "|", published_by, "|", previous_edition, "|", price))
           # print(s_format % (item['ISBN'], "|", item['title'],"|",item['year'],"|",item['published_by'],"|", item['previous_edition'],"|",item['price'])
    print("The end.")
def search_by_publisher(publisher):# find book by publisher
    results=list(book_dao.findbyPublisher(publisher))
    print("Search by Publisher:")
         # Display results
    s_format = "%-10s %-1s %-50s %-1s %-5s %-1s %-25s %-1s %-18s  %-1s %-8s " # format specifiers that indicate left-aligned fields of specific widths (10, 1, and 50 respectively)
    print(s_format % ("ISBN:", "|", "Title:","|","Year","|","Published_By","|","Previous_Edition","|","Price"))
    if len(results) == 0:
        print("N/A")
    else:
        for item in results:
            print(s_format % (item['ISBN'], "|", item['title'],"|",item['year'],"|",item['published_by'],"|", item['previous_edition'],"|",item['price']))
    print("---End of Search Results---")
def search_by_price(min,max):
    results=list(book_dao.findByPrice(min,max))
    print("Search by price:")
         # Display results
    s_format = "%-10s %-1s %-50s %-1s %-5s %-1s %-25s %-1s %-18s  %-1s %-8s " # format specifiers that indicate left-aligned fields of specific widths (10, 1, and 50 respectively)
    print(s_format % ("ISBN:", "|", "Title:","|","Year","|","Published_By","|","Previous_Edition","|","Price"))
    if len(results) == 0:
        print("N/A")
    else:
        for item in results:
            print(s_format % (item['ISBN'], "|", item['title'],"|",item['year'],"|",item['published_by'],"|", item['previous_edition'],"|",item['price']))
    print("---End of Search Results---")

def print_menu(): # print the queries menu option
    print()
    print("Please make a selection")
    for key in menu_options.keys():
        print (str(key)+'.', menu_options[key], end = "  ")
    print()
    print("The end of top-level options")
    print()
def search_by_tile_publisher(title,publisher): # search by title and publisher
    results=list(book_dao.findByTitlePublisher(title,publisher))
    print("Search by price:")
         # Display results
    s_format = "%-10s %-1s %-50s %-1s %-5s %-1s %-25s %-1s %-18s  %-1s %-8s " # format specifiers that indicate left-aligned fields of specific widths (10, 1, and 50 respectively)
    print(s_format % ("ISBN:", "|", "Title:","|","Year","|","Published_By","|","Previous_Edition","|","Price"))
    if len(results) == 0:
        print("N/A")
    else:
        for item in results:
            print(s_format % (item['ISBN'], "|", item['title'],"|",item['year'],"|",item['published_by'],"|", item['previous_edition'],"|",item['price']))
    print("---End of Search Results---")

def print_query():
    print()
    print("Please make a selection")
    for key in search_menu_options.keys():
        print (str(key)+'.', search_menu_options[key], end = "  ")
    print()


def option1(): # add publisher
    print('Handle option \'Option 1\'')
    print()
    print("-------Add Publisher-------")
    print("Type NULL for no entry.")
    name=""
    while len(name)==0:
        name = input("Enter Name: ")
        if len(name)>25:
            name=""
            print("Error: name length must be smaller than 25")
    phone = ""
    while phone == "":
        phone = input("Enter Phone Number: ")
        if len(phone) != 10:
            phone = ""
            print("Error: Phone number length must be 10!")
        try:
            int(phone)
        except ValueError:
            phone = ""
            print("Error: Phone number must consist of integers!")
    city = ""
    while len(city) == 0:
        city = input("Enter City: ")
        if len(city) > 20:
            city = ""
            print("Error: City name too long (max 20 characters)!")
    result = book_dao.addPublisher(name, phone, city)
    print(result)

def option2():#ADD book
    print()
    print("-------Add Book-------")
    print("Type NULL for no entry.")
    ISBN = ""
    while len(ISBN) == 0:
        ISBN = input("Enter ISBN Number: ")
        if len(ISBN) > 10:
            ISBN = ""
            print("Error: ISBN length must be smaller than 10!")
    title=""
    while len(title)==0:
        title = input("Enter Title: ")
        if len(title) > 50:
            title = ""
            print("Error: title length must be smaller than 50!")
    year=""
    while len(year)==0:
        year=input("Enter published year: ")
        if len(year)!=4:
            year=""
            print("Error: year must have at 4 digits")
        try:
            int(year)
        except ValueError:
            year = ""
            print("Error: year number must consist of integers!")
    published_by=""
    while(len(published_by)==0):
        published_by=input("Enter publisher: ")
        if len(published_by)>25:
            published_by=""
            print("Error: publisher name must be smaller than 25")
       
    previousEdition=""
    while(len(previousEdition)==0):
        previousEdition=input("Enter previous Edition: ")
        if len(previousEdition)>10:
            previousEdition=""
            print("Error: previous edition must be smaller than 10")
       
    price=""
    while price=="":
        price=input("Enter price: ")
        try:
            float(price)
        except ValueError:
            price = ""
            print("Error: price  must consist of number only !")
    result = book_dao.addBook( ISBN, title, year, published_by, previousEdition, price)
    print(result)

def option3():# edit a book
        ISBN=""
        while len(ISBN)==0:
            ISBN = input("Enter ISBN Number of the book you want to edit: ")
            if len(ISBN) > 10:
                ISBN = ""
                print("Error: ISBN length must be smaller than 10!")
        new_title=""
        while(len(new_title)==0):
                new_title = input("Enter new title: ")
                if len(new_title) > 50:
                    new_title = ""
                    print("Error: title length must be smaller than 50!")
        new_year=""
        while(len(new_year)==0):
                new_year = input("Enter the new year: ")
                if len(new_year)!=4:
                    new_year=""
                    print("Error: year must have at 4 digits")
                try:
                    int(new_year)
                except ValueError:
                    new_year = ""
                    print("Error: year number must consist of integers!")
        new_published_by=""
        while(len(new_published_by)==0):
                new_published_by = input("Enter the new publisher: ")
                if len(new_published_by)>25:
                    new_published_by=""
                    print("Error: publisher name must be smaller than 25")
        new_previous_edition=""
        while(len(new_previous_edition)==0):
                new_previous_edition = input("Enter the new previous edition: ")
                if len(new_previous_edition)>10:
                    new_previous_edition=""
                    print("Error: previous edition must be smaller than 10")
        new_price=""
        while new_price=="":
                new_price=input("Enter price: ")
        try:
                float(new_price)
        except ValueError:
                new_price = ""
                print("Error: price  must consist of number only !")
                new_price = input("Enter the new price: ")  
        book_dao.editBook(ISBN,new_title,new_year,new_published_by,new_previous_edition,new_price)
      
def option4(): # delete book
    ISBN=""
    while len(ISBN)==0:
            ISBN = input("Enter ISBN Number of the book you want to delete: ")
            if len(ISBN) > 10:
                ISBN = ""
                print("Error: ISBN length must be smaller than 10!")
    book_dao.deleteBook(ISBN)
def option5():
    # A sub-menu shall be printed
    # and prompt user selection

    # print_search_menu

    # user selection of options and actions

    # Assume the option: search all books was chosen
    print_query()
   
    
    option = ''
    try:
        option = int(input('Enter your choice: '))
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
    except:
        print('Wrong input. Please enter a number ...') 
    if option == 1:
        print("Search Option 1: all books were chosen.")
        search_all_books()
        search_by_title()
    elif option ==2:
        print("Search option 2, please specified publisher")
        try: 
            publisher= input('Enter book publisher:')
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        search_by_publisher(publisher)    
    elif option == 3:
        print("Search option 3, please specified price range")
        try: 
            min= input('Enter book price min:')
            max=input('Enter book price max: ')
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        try:
            min=float(min)
        except ValueError:
            min = ""
            print("Error: minimum price  must consist of number only !")

        try:
            max=float(max)
        except ValueError:
            max = ""
            print("Error: maximum price  must consist of number only !")
            search_by_price(min,max)
    elif option == 4:
        print("Search option 4, please specified title and publisher")
        try: 
            title= input('Enter book title :')
            publisher=input('Enter book publisher: ')
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        search_by_tile_publisher(title,publisher)
    elif option ==5 :
        search_by_title()
   
    else:
        print("Invalid option. Please enter a number from 1 to 6")

if __name__=='__main__':
    print_menu
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        except:
            print('Wrong input. Please enter a number ...')

        # Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        # More options to be added
        elif option ==3:
            option3()
        elif option ==4:
             option4()
        elif option == 5:
            option5()
        elif option == 6:
            print('Thanks your for using our database services! Bye')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 6.')











