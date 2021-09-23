import tkinter
import random
import time

masu = [
  [1, 0, 0],
  [0, 0, 2],
  [0, 0, 0]
]

target = 0
win = 0

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
    cvs.update()


def click(e):
  global target
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
    if target < 9:
      computer()


def computer():
  global target
  while True:
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    if masu[y][x] == 0:
      masu[y][x] = 2
      target += 1
      masume()
      time.sleep(0.5)
      break

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
 
root = tkinter.Tk()
root.title("Line Up three squares")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tkinter.Canvas(width=600, height=600, bg="white")
cvs.pack()
masume()
root.mainloop()