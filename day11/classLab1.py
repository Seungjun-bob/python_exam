class Member:
    def __init__(self, name, account, passwd, birthyear):
        self.name = name
        self.account = account
        self.passwd = passwd
        self.birthyear = birthyear

member1 = Member("둘리", "dolly123", "123456", "960105")
member2 = Member("도우너", "douner456", "abcd", "001111")
member3 = Member("또치", "ddochi789", "qwer", "980505")

print("회원1 : {}({},{},{})".format(member1.name, member1.account, member1.passwd, member1.birthyear))
print("회원2 : {}({},{},{})".format(member2.name, member2.account, member2.passwd, member2.birthyear))
print("회원1 : {}({},{},{})".format(member3.name, member3.account, member3.passwd, member3.birthyear))
