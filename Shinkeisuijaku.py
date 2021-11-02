import tkinter
from PIL import Image

img = [None] * 14

def draw_card():
  for i in range(14):
    x = (i % 7) * 120+ 60
    y = int(i / 7) * 168 + 84
    


root = tkinter.Tk()
root.title("神経衰弱")
root.resizable(False, False)
cvs = tkinter.Canvas(width=960, height=670)
cvs.pack()
for i in range(14):
  img[i] = Image.open(file="img/"+str(i)+".png")
draw_card()
root.mainloop()