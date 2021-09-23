import time
import random

#Mole function
def mogura(r):
  m = ""
  n = ""

  #loop turn
  for i in range(8):
    ana = "."
    if i == r:
      ana = "0"
    m = m + " _" + ana + "_ "
    n = n + " [" + str(i) + "] "
  print(m)
  print(n)


print("=============Game Start================")
hit = 0
ts = time.time()

for i in range(10):
  r = random.randint(0, 7)
  mogura(r)
  p = input("Where is Mole？ ")
  
  #Hit or Miss turn
  if p == str(r):
    print("HIT!")
    hit += 1
  else:
    print("MISS")


  t = int(time.time() - ts)
  bonus = 0

  if t < 60:
    bonus = 60 - t

print("============Game End==============")
print("TIME, ", t, "sec")
print("HIT ", hit, "✖︎ BONUS", bonus)
print("SCORE", hit * bonus)