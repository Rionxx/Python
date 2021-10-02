import tkinter


BLACK = 1
WHITE = 2
board = [
  [0,2,2,0,2,2,2,1],
  [2,0,0,0,0,0,0,0],
  [2,0,2,0,0,1,2,0],
  [1,0,0,2,0,2,2,0],
  [0,0,0,0,0,2,2,0],
  [2,0,0,0,0,0,2,1],
  [2,0,0,0,0,2,0,0],
  [1,0,0,0,0,1,0,0],
]

#click event
def click(e):
  mx = int(e.x/80)
  my = int(e.y/80)
  if mx>7: mx = 7
  if my>7: my = 7
  if board[my][mx] == 0:
    stone_put(mx, my, BLACK)
  field()

# Reversi field
def field():
  cvs.delete("all")
  for y in range(8):
    for x in range(8):
      X = x*80
      Y = y*80
      cvs.create_rectangle(X, Y, X+80, Y+80, outline="black")

      if board[y][x] == BLACK:
        cvs.create_oval(X+10, Y+10, X+70, Y+70, fill="black", width=0)
      if board[y][x] == WHITE:
        cvs.create_oval(X+10, Y+10, X+70, Y+70, fill="white", width=0)
      if returnStone(x, y,BLACK)>0:
        cvs.create_oval(X+5, Y+5, X+75, Y+75, outline="cyan", width=2)
    cvs.update()

#Count how many you can return if you hit it there
def stone_put(x, y, color):
  board[y][x] = color
  for dy in range(-1, 2):
    for dx in range(-1, 2):
      k = 0
      sx = x
      sy = y

      while True:
        sx += dx
        sy += dy

        if sx<0 or sx>7 or sy<0 or sy>7:
          break
        if board[sy][sx] == 0:
          break
        if board[sy][sx] == 0:
          k += 1
          if board[sy][sx] == color:
            for i in range(k):
              sx -= dx
              sy -= dy
              board[sy][sx] = color
            break

#Count how many return when stone put in this
def returnStone(x, y, color):
  if board[y][x]>0:
    return -1 # Can not put masu
  total = 0
  for dy in range(-1, 2):
    for dx in range(-1, 2):
      k = 0
      sx = x
      sy = y
      while True:
        sx += x
        sy += y
        if sx<0 or sx>7 or sy<0 or sy>7:
          break
      if board[sy][sx]==0:
        break
      if board[sy][sx]==3-color:
        k += 1
      if board[sy][sx]==color:
        total += k
        break
  return total

root = tkinter.Tk()
root.title("Reversi")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tkinter.Canvas(width=640, height=700, bg="green")
cvs.pack()
field()
root.mainloop()
