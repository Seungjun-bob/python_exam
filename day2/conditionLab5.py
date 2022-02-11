import random

score = random.randint(0, 100)
if 0 <= score < 60:
    print(str(score) + "점은 F등급입니다.")
if 60 <= score < 70:
    print(str(score) + "점은 D등급입니다.")
if 70 <= score < 80:
    print(str(score) + "점은 C등급입니다.")
if 80 <= score < 90:
    print(str(score) + "점은 B등급입니다.")
if 90 <= score <= 100:
    print(str(score) + "점은 A등급입니다.")