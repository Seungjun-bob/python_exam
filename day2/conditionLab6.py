import random

score = random.randint(0, 100)
if 0 <= score < 60:
    grade = "F"
if 60 <= score < 70:
    grade = "D"
if 70 <= score < 80:
    grade = "C"
if 80 <= score < 90:
    grade = "B"
if 90 <= score <= 100:
    grade = "A"

print(str(score) + "점은 %s등급입니다."%(grade))