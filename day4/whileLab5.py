while True:
    word = input("문자열을 입력하시오 : ")
    wordlength = len(word)
    if wordlength == 0:
        break
    elif 5 <= wordlength <= 8:
        continue
    elif wordlength < 5:
        result = "*" + word + "*"
    elif 8 < wordlength:
        result = "$" + word + "$"
    print("유효한 입력 결과 :", result)

