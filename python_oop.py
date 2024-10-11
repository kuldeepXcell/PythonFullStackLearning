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

# class Book:
#     def __init__(self, isbn, title, author, publisher, pages, price, copies):
#         self.isbn = isbn
#         self.title = title
#         self.author = author
#         self.publisher = publisher
#         self.pages = pages
#         self._price = price
#         self.copies = copies
#
#     def in_stock(self):
#         return True if self.copies > 0 else False
#
#     def sell(self):
#         if self.in_stock():
#             self.copies -= 1
#         else:
#             print("Book out of Stock !")
#
#     def display(self):
#         print(f"ISBN: {self.isbn}\n"
#               f"Title: {self.title}\n"
#               f"Author: {self.author}\n"
#               f"Publisher: {self.publisher}\n"
#               f"Pages: {self.pages}\n"
#               f"Price: {self._price}\n"
#               f"Copies: {self.copies}\n")
#
#     @property
#     def price(self):
#         if not (50<=self._price<=1000):
#             print("Invalid Price Range")
#         else:
#             return self._price
#
# book1 = Book('957-4-36-547417-1', 'Learn Physics', 'Stephen', 'CBC', 350, 200, 10)
# book2 = Book('652-6-86-748413-3', 'Learn Chemistry', 'Jack', 'CBC', 400, 220, 20)
# book3 = Book('957-7-39-347216-2', 'Learn Maths', 'John', 'XYZ', 500, 300, 5)
# book4 = Book('957-7-39-347216-2', 'Learn Biology', 'Jack', 'XYZ', 400, 200, 6)
#
# books = [book1,book2,book3,book4]
# for book in books:
#     book.display()
#
#######################################################################################################################
#
# class Product():
#     def __init__(self, id, marked_price, discount):
#         self.id = id
#         self.marked_price = marked_price
#         self._discount = discount
#
#     def display(self):
#         print(self.id, self.marked_price, self.discount)
#
#     @property
#     def selling_price(self):
#         return (self.marked_price
#                 - (self._discount/100)*self.marked_price)
#
#     @property
#     def discount(self):
#         if self.marked_price > 500:
#             self._discount += 2
#         else:
#             pass
#
# p1 = Product('X879', 400, 6)
# p2 = Product('A234', 100, 5)
# p3 = Product('B987', 990, 4)
# p4 = Product('H456', 800, 6)
#
# p1.discount
# print(p1.selling_price)
# p3.discount
# print(p3.selling_price)
#
#######################################################################################################################
#
# class Circle:
#     def __init__(self,radius):
#         if radius < 0:
#             print("Cannot Create Circle with Negative Radius !")
#         else:
#             self.radius = radius
#
#     @property
#     def diameter(self):
#         return self.radius * 2
#
#     @property
#     def circumference(self):
#         return 2*3.14*self.radius
#
#     def area(self):
#         return 3.14*(self.radius**2)
#
# c1 = Circle(4)
# print(c1.radius)
# print(c1.diameter)
# print(c1.circumference)
#
#######################################################################################################################
#
# class SalesPerson:
#     total_revenue = []
#     names = []
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.sales_amount = 0
#         SalesPerson.names.append(self.name)
#         SalesPerson.total_revenue.append(self.sales_amount)
#
#     def make_sale(self, money):
#         self.sales_amount += money
#         SalesPerson.total_revenue[SalesPerson.names.index(self.name)] = self.sales_amount
#
#     def show(self):
#         print(self.name, self.age, self.sales_amount)
#
#
# s1 = SalesPerson('Bob', 25)
# s2 = SalesPerson('Ted', 22)
# s3 = SalesPerson('Jack', 27)
#
# s1.make_sale(1000)
# s1.make_sale(1200)
# s2.make_sale(5000)
# s3.make_sale(3000)
# s3.make_sale(8000)
#
# s1.show()
# s2.show()
# s3.show()
#
# print(SalesPerson.names)
# print(SalesPerson.total_revenue)
#
# #######################################################################################################################
#
# class Employee:
#     allowed_domains = {'gmail.com', 'yahoo.com', 'outlook.com'}
#     domains = set()
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         if self.email.split("@")[1] in Employee.allowed_domains:
#             Employee.domains.add(self.email.split("@")[1])
#         else:
#             raise Exception(f"{self.email.split("@")[1]} Not Allowed !")
#
#
# def display(self):
#     print(self.name, self.email)
#
#
# e1 = Employee('John', 'john@gmail.com')
# e2 = Employee('Jack', 'jack@yahoo.com')
# e3 = Employee('Jill', 'jill@outlook.com')
# e4 = Employee('Ted', 'ted@yahoo.com')
# e5 = Employee('Tim', 'tim@gmail.com')
# e6 = Employee('Mike', 'mike@yahoo.com')
# e7 = Employee('Jack', 'jack@yaho.com')
#
# print(Employee.domains)

#######################################################################################################################

# class Stack:
#     MAX_SIZE = 10
#
#     def __init__(self):
#         self.items = []
#
#     def is_empty(self):
#         return self.items == []
#
#     def size(self):
#         return len(self.items)
#
#     def push(self, item):
#         if self.size() >= Stack.MAX_SIZE:
#             raise Exception("!!! STACK SIZE EXCEEDED !!!")
#         else:
#             self.items.append(item)
#
#     def pop(self):
#         if self.is_empty():
#             raise RuntimeError("Stack is empty")
#         return self.items.pop()
#
#     def display(self):
#         print(self.items)
#
#
# if __name__ == "__main__":
#     st = Stack()
#
#     while True:
#         print("1.Push")
#         print("2.Pop")
#         print("3.Peek")
#         print("4.Size")
#         print("5.Display")
#         print("6.Quit")
#
#         choice = int(input("Enter your choice : "))
#
#         if choice == 1:
#             x = int(input("Enter the element to be pushed : "))
#             st.push(x)
#         elif choice == 2:
#             x = st.pop()
#             print("Popped element is : ", x)
#         elif choice == 3:
#             print("Element at the top is : ", st.peek())
#         elif choice == 4:
#             print("Size of stack ", st.size())
#         elif choice == 5:
#             st.display()
#         elif choice == 6:
#             break;
#         else:
#             print("Wrong choice")
#         print()

#######################################################################################################################

# class BankAccount:
#     bank_name = "Kotak Bank"
#
#     def __init__(self, name, balance=0, bank=bank_name):
#         self.name = name
#         self.balance = balance
#         self.bank = bank
#
#     def display(self):
#         print(self.name, self.balance, self.bank_name)
#
#     def withdraw(self, amount):
#         self.balance -= amount
#
#     def deposit(self, amount):
#         self.balance += amount
#
#
# a1 = BankAccount('Mike', 200)
# a2 = BankAccount('Tom')
#
# a1.display()
# a2.display()
#
#
#######################################################################################################################
#
# class Time:
#     def __init__(self, h, m, s):
#         self._h = h
#         self._m = m
#         self._s = s
#
#     def __eq__(self, other):
#         if self._h == other._h and self._m == other._m and self._s == other._s:
#             return True
#         else:
#             return False
#
#     def __lt__(self, other):
#         if self._h < other._h:
#             return True
#         if self._h == other._h:
#             if self._m < other._m:
#                 return True
#             elif self._m == other._m:
#                 if self._s < other._s:
#                     return True
#                 else:
#                     return False
#             else:
#                 return False
#         else:
#             return False
#
#     def __gt__(self, other):
#         if self._h > other._h:
#             return True
#         if self._h == other._h:
#             if self._m > other._m:
#                 return True
#             elif self._m == other._m:
#                 if self._s > other._s:
#                     return True
#                 else:
#                     return False
#             else:
#                 return False
#         else:
#             return False
#
#     # Read-only field accessors
#     @property
#     def hours(self):
#         return self._h
#
#     @property
#     def minutes(self):
#         return self._m
#
#     @property
#     def seconds(self):
#         return self._s
#
# def _cmp(time1, time2):
#     if time1._h < time2._h:
#         return True
#     if time1._h > time2._h:
#         return False
#     if time1._m < time2._m:
#         return True
#     if time1._m > time2._m:
#         return False
#     if time1._s < time2._s:
#         return True
#     if time1._s > time2._s:
#         return False
#     return 0
#
#
# t1 = Time(13, 10, 5)
# t2 = Time(13, 11, 30)
# t3 = Time(5, 15, 30)
# t4 = Time(5, 16, 30)
# t5 = Time(5, 15, 35)
# print(t1 < t2)
# print(t1 > t2)
# print(t1 == t2)
# print(t2 == t3)

#######################################################################################################################

class Length:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        return f'{self.feet} {self.inches}'

    def __add__(self, other):
        if type(other) is int:
            return f"{self.feet+other}' {self.inches}''"
        else:
            updated_feet = self.feet + other.feet
            updated_inches = self.inches + other.inches
            extra_feet = updated_inches//12
            if extra_feet > 0:
                updated_feet  += extra_feet
                updated_inches -= 12*extra_feet
            return f"{updated_feet}' {updated_inches}''"

    def __radd__(self, other):
        return self.__add__(other)

    def add_length(self, L):
        f = self.feet + L.feet
        i = self.inches + L.inches
        if i >= 12:
            i = i - 12
        f += 1
        return Length(f, i)

    def add_inches(self, inches):
        f = self.feet + inches // 12
        i = self.inches + inches % 12
        if i >= 12:
            i = i - 12
        f += 1
        return Length(f, i)


length1 = Length(2, 10)
length2 = Length(3, 5)

print(length1 + length2)
print(length1 + 2)
print(length1 + 20)
print(20 + length1)

#######################################################################################################################

