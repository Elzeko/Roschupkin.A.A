# -- coding: utf-8 --
def F():
  x1 = int(input())
  y1 = int(input())
  x2 = int(input())
  y2 = int(input())
  if((1 <= x1 <= 8) and (1 <= y1 <= 8) and (1 <= x2 <= 8) and (1 <= y2 <= 8)):
        if(((x1 % 2 != 0) and (y1 % 2 != 0)) or ((x1 % 2 == 0) and (y1 % 2 == 0))):
            xy1 = "black"
        else:
            xy1 = "White"
        if(((x2 % 2 != 0) and (y2 % 2 != 0)) or ((x2 % 2 == 0) and (x2 % 2 == 0))):
            xy2 = "black"
        else:
            xy2 = "white"
        if(xy1 == xy2):
            return "Да"
        else:
            return "Нет"
print(F()) 