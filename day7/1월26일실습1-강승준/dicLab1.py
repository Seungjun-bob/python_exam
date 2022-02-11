color = { "red":"#ff0000", "blue":"#0000ff", "green":"#008000", "yellow":"#ffff00",
        "orange":"#ffa500", "black":"#000000", "white": "#ffffff",
        "violet":"#ee82ee", "pink":"#ffc0cb", "lime":"#00ff00"
          }
input_color = input("칼라명을 영문으로 입력하세요 :")

if input_color in color.keys():
    RGB_val = color[input_color]
    print(input_color, "칼라의 RGB 값은", RGB_val, "입니다.")
else:
    print(input_color, "칼라의 RGB 값을 찾을 수 없습니다.")