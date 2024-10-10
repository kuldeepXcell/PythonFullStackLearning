# class bank_account:
#     def __init__(self,name,balance):
#         self.name = name
#         self.balance = balance
#         self.__loan = 0
#
#     @property
#     def loan(self):
#         print(f"Loan Amount : {self.__loan}")
#
#     @loan.setter
#     def loan(self, val):
#         self.__loan = val
#
#     def display(self):
#         print(f"Account Holder's Name: {self.name}")
#         print(f"Account Balance: {self.balance}\n")
#
#     def withdraw(self, amount):
#         self.balance -= amount
#
#     def deposit(self, amount):
#         self.balance += amount
#
#
# person1 = bank_account("Kuldeep", 100_00_000)
# person2 = bank_account("Deepak", 100_00_001)
#
# person1.display()
# person2.display()
#
# person1.withdraw(300000)
# person2.deposit(300000)
# person2.withdraw(5000000)
# person1.deposit(2500000)
#
# person1.display()
# person2.display()
#
# person1.loan = 20

#######################################################################################################################

class Book:
    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self._price = price
        self.copies = copies

    def in_stock(self):
        return True if self.copies > 0 else False

    def sell(self):
        if self.in_stock():
            self.copies -= 1
        else:
            print("Book out of Stock !")

    def display(self):
        print(f"ISBN: {self.isbn}\n"
              f"Title: {self.title}\n"
              f"Author: {self.author}\n"
              f"Publisher: {self.publisher}\n"
              f"Pages: {self.pages}\n"
              f"Price: {self._price}\n"
              f"Copies: {self.copies}\n")

    @property
    def price(self):
        if not (50<=self._price<=1000):
            print("Invalid Price Range")
        else:
            return self._price

book1 = Book('957-4-36-547417-1', 'Learn Physics', 'Stephen', 'CBC', 350, 200, 10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry', 'Jack', 'CBC', 400, 220, 20)
book3 = Book('957-7-39-347216-2', 'Learn Maths', 'John', 'XYZ', 500, 300, 5)
book4 = Book('957-7-39-347216-2', 'Learn Biology', 'Jack', 'XYZ', 400, 200, 6)

books = [book1,book2,book3,book4]
for book in books:
    book.display()

#######################################################################################################################

class Product():
    def __init__(self, id, marked_price, discount):
        self.id = id
        self.marked_price = marked_price
        self._discount = discount

    def display(self):
        print(self.id, self.marked_price, self.discount)

    @property
    def selling_price(self):
        return (self.marked_price
                - (self._discount/100)*self.marked_price)

    @property
    def discount(self):
        if self.marked_price > 500:
            self._discount += 2
        else:
            pass

p1 = Product('X879', 400, 6)
p2 = Product('A234', 100, 5)
p3 = Product('B987', 990, 4)
p4 = Product('H456', 800, 6)

p1.discount
print(p1.selling_price)
p3.discount
print(p3.selling_price)

#######################################################################################################################

class Circle:
    def __init__(self,radius):
        if radius < 0:
            print("Cannot Create Circle with Negative Radius !")
        else:
            self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def circumference(self):
        return 2*3.14*self.radius

    def area(self):
        return 3.14*(self.radius**2)

c1 = Circle(4)
print(c1.radius)
print(c1.diameter)
print(c1.circumference)

#######################################################################################################################

