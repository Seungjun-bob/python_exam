def myemail_info(s):

    if "@" not in s:
        return None
    return print(tuple(s.split('@')))


myemail_info('abcd@naver.com')
myemail_info('abc')