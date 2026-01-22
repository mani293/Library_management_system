class Library:

  def __init__ (self, listOfBooks):
    self.availableBooks = listOfBooks

  def displayAvailableBooks(self):
    print("\nAvailable books: ")
    for book in self.availableBooks:
      print(book)

  def lendBook(self, requestedBook):
    if requestedBook in self.availableBooks:
      print("\nYou have now borrowed the book\n")
      self.availableBooks.remove(requestedBook)
    else:
      print("\nSorry, the book is not available in our Library\n")

  def addBook(self, returnBook):
    self.availableBooks.append(returnBook)
    print("\nYou have returened the book, Thanks\n")


class Customer:
  def requestBook(self):
    print("\nEnter the name of a book you would like to borrow: ")
    self.book = input()
    return self.book

  def returnBook(self):
    print("\nEnter the name of a book you would like to return: " )
    self.book = input()
    return self.book

library = Library(['Energize your mind','positive thinking','ikigai'])
customer = Customer()
while True:
  print("enter 1 to display the available books")
  print("enter 2 to request a book")
  print("enter 3 to return a book")
  print("enter 4 to exit")

  userChoice =int(input())
  if userChoice == 1:
    library.displayAvailableBooks()
  elif userChoice == 2:
    requestedBook = customer.requestBook()
    library.lendBook(requestedBook)
  elif userChoice == 3:
    returnBook = customer.returnBook()
    library.addBook(returnBook)
  elif userChoice == 4:
    quit()
  else:
    print("Please enter correct choice\n")