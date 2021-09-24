import tkinter
import random
import time
from tkinter import font

masu = [
  [1, 0, 0],
  [0, 0, 2],
  [0, 0, 0]
]

target = 0
win = 0
FNT = ("Times New Roman", 60)

def masume():
  cvs.delete("all")
  for i in range(1, 3):
    cvs.create_line(200*i, 0, 200*i, 600, fill="gray", width=8)
    cvs.create_line(0, 200*i, 600, 200*i, fill="gray", width=8)
  
  for y in range(3):
    for x in range(3):
      X = x * 200
      Y = y * 200
      if masu[y][x] == 1:
        cvs.create_oval(X+20, Y+20, X+180, Y+180, outline="blue", width=12)
      if masu[y][x] == 2:
        cvs.create_line(X+20, Y+20, X+180, Y+180, fill="red", width=12)
        cvs.create_line(X+180, Y+20, X+20, Y+180, fill="red", width=12)

    if target == 0:
      cvs.create_text(300, 300, text="スタート", fill="navy", font=FNT)
    cvs.update()

#Process Click

def click(e):
  global target

  if win == 9:
    replay()
    return
  if target == 1 or target == 3 or target == 5 or target == 7:
    return

  mx = int(e.x/200)
  my = int(e.y/200)
  if mx>2: mx = 2
  if my>2: my = 2

  if masu[my][mx] == 0:
    masu[my][mx] = 1
    target += 1
    masume()
    time.sleep(0.5)
    judgement()
    WinOrLose()
    
    if target < 9:
      computer()
      masume()
      time.sleep(0.5)
      judgement()
      WinOrLose()

#Process Computer

def computer():
  global target

  #line up three masu
  for y in range(3):
    for x in range(3):
      if masu[y][x] == 0:
        masu[y][x] = 2
        judgement()
        if win == 2:
          target += 1
          return
        masu[y][x] = 0

  #stop play that line up three masu
  for y in range(3):
    for x in range(3):
      if masu[y][x] == 0:
        masu[y][x] = 1
        judgement()
        if win == 1:
          masu[y][x] = 2
          target += 1
          return
        masu[y][x] = 0
        
  while True:
    x = random.randint(0, 2)
    y = random.randint(0, 2)

    if masu[y][x] == 0:
      masu[y][x] = 2
      target += 1
      masume()
      time.sleep(0.5)
      judgement()
      WinOrLose()
      break

#judgement win

def judgement():
  global win
  win = 0
  for n in range(1, 3):
    #judge vertical line
    if masu[0][0] == n and masu[1][0] == n and masu[2][0] == n:
      win = n
    if masu[0][1] == n and masu[1][1] == n and masu[2][1] == n:
      win = n
    if masu[0][2] == n and masu[1][2] == n and masu[2][2] == n:
      win = n

    #judge horizontal line
    if masu[0][0] == n and masu[1][0] == n and masu[2][0] == n:
      win = n
    if masu[1][0] == n and masu[1][1] == n and masu[1][2] == n:
      win = n
    if masu[2][0] == n and masu[2][1] == n and masu[2][2] == n:
      win = n
    
    #judge diagonal
    if masu[0][0] == n and masu[1][1] == n and masu[2][2] == n:
      win = n
    if masu[0][2] == n and masu[1][1] == n and masu[2][0] == n:
      win = n
  
  if win == 1:
    root.title("Bingo three circles")
  if win == 2:
    root.title("Bingo three crosses")
 

# win or lose

def WinOrLose():
  global target
  if win == 1:
    cvs.create_text(300, 300, text="You Win!", font=FNT, fill="cyan")
    target = 9
  if win == 2:
    cvs.create_text(300, 300, text="Computer Win!", font=FNT, fill="gold")
    target = 9
  if win == 0 and target == 9:
    cvs.create_text(300, 300, text="Drow", font=FNT, fill="lime")


#Process replay

def replay():
  global target
  target = 0
  for y in range(3):
    for x in range(3):
      masu[y][x] = 0
  masume()

root = tkinter.Tk()
root.title("Line Up three squares")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tkinter.Canvas(width=600, height=600, bg="white")
cvs.pack()
masume()
root.mainloop()