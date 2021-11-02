def compute(Expression, ExpLen):
  Operator = [100]
  Priority = [100]
  Value = [100]

  chr = ""
  OpCnt = 0
  nest = 0
  for i in range(0, ExpLen):
    chr = Expression[i]
    if chr >= '0' and chr <= '9':
      Value[OpCnt] = 10 * Value[OpCnt] + int(chr)
    
    if chr == '+' or chr == '-' or chr == '*' or chr == '/':
      Operator[OpCnt] = chr
      if chr == '+' or chr == '-':
        Priority[OpCnt] = nest + 1
      else:
        Priority[OpCnt] = nest + 2
      OpCnt+=1
      Value[OpCnt] = 0
    if chr == '(':
      nest += 10
    if chr == ')':
      nest -= 10
  
  #計算処理
  if OpCnt > 0:
    ip = 0
    for i in range(1, OpCnt):
      if Priority[ip] < Priority[i]:
        ip = i
    chr = Operator[ip]
    if chr == '+':
      Value[ip] = Value[ip] + Value[ip + 1]
    if chr == '-':
      Value[ip] = Value[ip] - Value[ip + 1]
    if chr == '*':
      Value[ip] = Value[ip] * Value[ip + 1]
    if chr == '/':
      Value[ip] = Value[ip] / Value[ip + 1]
    for i in range(ip + 1, OpCnt):
      Value[i] = Value[i + 1]
      Operator[i - 1] = Operator[i]
      Priority[i - 1] = Priority[i]
  return Value[0]

print(compute("20+40*(1+2)", 4))