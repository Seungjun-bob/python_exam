import random
grade = random.randint(1, 6)

if 1 <= grade and grade <= 3:
    print(str(grade) + "학년은 저학년입니다.")
if 4 <= grade and grade <= 6:
    print(str(grade) + "학년은 고학년입니다.")