class Library:
  def __init__(self):
    self.noBooks = 0
    self.books = []
    
  def addBook(self, book):
    self.books.append(book)
    self.noBooks = len(self.books)

  def showInfo(self):
    print(f"The library has {self.noBooks} books. The books are")
    for book in self.books:
      print(book)

list1 = Library()
list1.addBook("Rich Dad Poor Dad")
list1.addBook("The Power of Subconsious Mind")
list1.addBook("Wings of Fire")
list1.showInfo()