class Book:
    def __init__(self, title, author, price):
        self.title = str(title)
        self.author = str(author)
        self.price = int(price)

    def getBookInfo(self):
        return [self.title, self.author, self.price]

    def __str__(self):
        return "\n{}\n{}\n{}".format(\
            self.title,\
            self.author,\
            self.price)

book1 = Book("파이썬 정복", "한빛 미디어", "20000")
book2 = Book("이것이 MariaDB다 정복", "한빛 미디어", "20000")
book3 = Book("맛있는 MongoDB", "비제이 퍼블릭", "20000")
book4 = Book("Do it! 점프 투 장고", "이지스 퍼블리싱", "20000")
book5 = Book("생활코딩 HTML+CSS+JavaScript", "위키북스", "20000")

print("[객체1:book1]", book1)
print("[객체2:book2]", book2)
print("[객체3:book3]", book3)
print("[객체4:book4]", book4)
print("[객체5:book5]", book5)