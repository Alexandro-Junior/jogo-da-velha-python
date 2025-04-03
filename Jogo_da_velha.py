
# ciência da computação  Programação de Computadores 
# 1º A

a1 = '_'
a2 = '_'
a3 = '_'
b1 = '_'
b2 = '_'
b3 = '_'
c1 = '_'
c2 = '_'
c3 = '_'

def win_X():
  if a1 == 'X' and a2 == 'X' and a3 == 'X':
    print(' ')
    tabela()
    print(' ')
    exit("PARABÉNS VOCÊ VENCEU")
  elif b1 == 'X' and b2 == 'X' and b3 == 'X':
    print(' ')
    tabela()
    print(' ')
    exit("PARABÉNS VOCÊ VENCEU")
  if c1 == 'X' and c2 == 'X' and c3 == 'X':
    print(' ')
    tabela()
    print(' ')
    exit("PARABÉNS VOCÊ VENCEU")
  elif a1 == 'X' and b1 == 'X' and c1 == 'X': 
    print(' ')
    tabela()
    print(' ')
    exit("PARABÉNS VOCÊ VENCEU")
  if a2 == 'X' and b2 == 'X' and c2 == 'X':
    print(' ')
    tabela()
    print(' ')
    exit("PARABÉNS VOCÊ VENCEU")
  elif a3 == 'X' and b3 == 'X' and c3 == 'X': 
    print(' ')
    tabela()
    print(' ')
    exit("PARABÉNS VOCÊ VENCEU")
  if a1 == 'X' and b2 == 'X' and c3 == 'X':
    print(' ')
    tabela()
    print(' ')
    exit("PARABÉNS VOCÊ VENCEU")
  elif a3 == 'X' and b2 == 'X' and c1 == 'X':
    print(' ')
    tabela()
    exit("win")

def win_O():
  if a1 == 'O' and a2 == 'O' and a3 == 'O':
    print(' ')
    tabela()
    print(' ')
    exit("QUE PENA VOCÊ PERDEU")
  elif b1 == 'O' and b2 == 'O' and b3 == 'O':
    print(' ')
    tabela()
    print(' ')
    exit("QUE PENA VOCÊ PERDEU")
  if c1 == 'O' and c2 == 'O' and c3 == 'O':
    print(' ')
    tabela()
    print(' ')
    exit("QUE PENA VOCÊ PERDEU")
  elif a1 == 'O' and b1 == 'O' and c1 == 'O': 
    print(' ')
    tabela()
    print(' ')
    exit("QUE PENA VOCÊ PERDEU")
  if a2 == 'O' and b2 == 'O' and c2 == 'O': 
    print(' ')
    tabela()
    print(' ')
    exit("QUE PENA VOCÊ PERDEU")
  elif a3 == 'O' and b3 == 'O' and c3 == 'O': 
    print(' ')
    tabela()
    print(' ')
    exit("QUE PENA VOCÊ PERDEU")
  if a1 == 'O' and b2 == 'O' and c3 == 'O':
    print(' ')
    tabela()
    print(' ')
    exit("QUE PENA VOCÊ PERDEU")
  elif a3 == 'O' and b2 == 'O' and c1 == 'O':
    print(' ')
    tabela()
    print(' ')
    exit("QUE PENA VOCÊ PERDEU")
    
def tabela():
  global a1 
  global a2 
  global a3
  global b1 
  global b2 
  global b3
  global c1 
  global c2 
  global c3 
  print('  1   2   3')
  print('a {} | {} | {}'.format(a1,a2,a3))
  print('----+---+---')
  print('b {} | {} | {}'.format(b1,b2,b3))
  print('----+---+---')
  print('c {} | {} | {}'.format(c1,c2,c3))

def jogador_começa():
  tabela()
  print()
  global a1 
  global a2 
  global a3
  global b1 
  global b2 
  global b3
  global c1 
  global c2 
  global c3 
  
  casas = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
  while True:
    print(' ')
    j1 = input('Qual a sua primeira jogada?: ')
    if j1.lower() == 'a1':
      break
    if j1.lower() == 'a2':
      break
    elif j1.lower() == 'a3':
      break
    if j1.lower() == 'b1':
      break
    elif j1.lower() == 'b2':
      break
    elif j1.lower() == 'b3':
      break
    if j1.lower() == 'c1':
      break
    elif j1.lower() == 'c2':
      break
    elif j1.lower() == 'c3':
      break
    if j1 != casas:
      print('Digite uma casa corretamente!')
      continue
  if j1 == 'a1':
    a1 = 'X'
  elif j1 == 'a2':
    a2 = 'X'
  if j1 == 'a3':
    a3 = 'X'
  elif j1 == 'b1':
    b1 = 'X'
  if j1 == 'b2':
    b2 = 'X'
  elif j1 == 'b3':
    b3 = 'X'
  if j1 == 'c1':
    c1 = 'X'
  elif j1 == 'c2':
    c2 = 'X'
  if j1 == 'c3':
    c3 = 'X'
  
  if a1 == 'X' or a2 == 'X' or a3 == 'X' or b1 == 'X' or b3 == 'X' or c1 == 'X' or c2 ==  'X' or c3 ==  'X':
    b2  = 'O'
  if b2 == 'X':
    a1 = 'O' 
  
  print(' ')
  tabela()
  print(' ')
  while True:
    print(' ')
    j2 = input('Qual a sua jogada?: ')
    if j2 == j1:
      continue
    if j2 == 'a1' and a1 == 'O':
      print(' ')
      print('Casa já selecionada')
      print(' ')
      continue
    elif j2 == 'a2' and a2 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if j2 == 'a3' and a3 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    elif j2 == 'b1' and b1 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if j2 == 'b2' and b2 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    elif j2 == 'b3' and b3 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if j2 == 'c1' and c1 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    elif j2 == 'c2' and c2 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if j2 == 'c3' and c3 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if j2 == 'a1' and a1 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    elif j2 == 'a2' and a2 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if j2 == 'a3' and a3 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    elif j2 == 'b1' and b1 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if j2 == 'b2' and b2 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    elif j2 == 'b3' and b3 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if j2 == 'c1' and c1 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    elif j2 == 'c2' and c2 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if j2 == 'c3' and c3 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if j2.lower() == 'a1':
      break
    if j2.lower() == 'a2':
      break
    elif j2.lower() == 'a3':
      break
    if j2.lower() == 'b1':
      break
    elif j2.lower() == 'b2':
      break
    elif j2.lower() == 'b3':
      break
    if j2.lower() == 'c1':
      break
    elif j2.lower() == 'c2':
      break
    elif j2.lower() == 'c3':
      break
    if j2 != casas:
      print('Digite uma casa corretamente!')
      continue
      print(' ')
      print('Essas são as casas disponivéis: {}'. format(casas))
  if j2 == 'a1':
    a1 = 'X'
  elif j2 == 'a2':
    a2 = 'X'
  if j2 == 'a3':
    a3 = 'X'
  elif j2 == 'b1':
    b1 = 'X'
  if j2 == 'b2':
    b2 = 'X'
  elif j2 == 'b3':
    b3 = 'X'
  if j2 == 'c1':
    c1 = 'X'
  elif j2 == 'c2':
    c2 = 'X'
  if j2 == 'c3':
    c3 = 'X'
  win_X()
  
  if a1 == 'X' and a2 == 'X':
    a3 = 'O'
  elif a2 == 'X' and a3 == 'X':
    a1 = 'O'
  if a1 == 'X' and a3 ==  'X':
    a2 = 'O'
  if a1 == 'X' and b1 == 'X':
    c1 = 'O'
  elif a1 == 'X' and b2 == 'X':
    c3 = 'O'
  if a1 == 'X' and c1 == 'X': 
    b1 = 'O'
  elif a1 == 'X' and c3 == 'X': 
    c1  = 'O'
  if b1 == 'X' and c1 == 'X':
    a3 = 'O'
  elif b2 == 'X' and c3 == 'X':
    b1 = 'O'
  if a2 == 'X' and b2 == 'X':
    c2 = 'O'
  elif b2 == 'X' and c2 == 'X':
    a2 = 'O'
  if a3 == 'X' and c1 == 'X':
    c3 = 'O'
  elif a3 == 'X' and b3 == 'X':
    c3 == 'O'
  if a3 == 'X' and c3 == 'X':
    b3 = 'O'
  elif b3 == 'X' and c3 == 'X':
    a3 = 'O'
  if b1 == 'X' and b3 == 'X':
    c3 = 'O'
  elif b2 == 'X' and b3 == 'X':
    b1 = 'O'
  if b1 == 'X' and b2 == 'X': 
    b3 = 'O'
  elif c1 == 'X' and c2 == 'X':
    c3 = 'O'
  if c1 == 'X' and c3 == 'X':
    c2 = 'O'
  elif c2 == 'X' and c3 == 'X':
    c1 = 'O'
  if a3 == 'X' and b2 == 'X':
    c1 = 'O'
  if a1 == 'X' and b2 == 'O' and b3 == 'X':
    c2 = 'O'
  elif a1 == 'X' and b2 == 'O' and c2 == 'X':
    b3 = 'O'
  if a2 == 'X' and b2 == 'O' and b1 == 'X':
    a3 = 'O'
  elif a2 == 'X' and b2 == 'O' and b3 == 'X':
    a3 = 'O'
  if a2 == 'X' and b2 == 'O' and c1 == 'X':
    a1 = 'O'
  elif a2 == 'X' and b2 == 'O' and c2 == 'X':
    a3 = 'O'
  if a2 == 'X' and b2 == 'O' and c3 == 'X':
    a3 = 'O'
  if a3 == 'X' and b2 == 'O' and b1 == 'X':
    c2 = 'O'
  elif a3 == 'X' and b2 == 'O' and c2 == 'X':
    b1 = 'O'
  elif b1 == 'X' and b2 == 'O' and c2 == 'X':
    c1 = 'O'
  if b1 == 'X' and b2 == 'O' and c3 == 'X':
    c1 = 'O'
  elif b3 == 'X' and b2 == 'O' and c1 == 'X':
    c3 = 'O'
  if b3 == 'X' and b2 == 'O' and c2 == 'X':
    c1 = 'O'
  # elif b3 == 'X' and b2 == 'O' and c3 == 'X':
  #   c1 = 'O'

    
  print(' ')
  tabela()
  win_O()
  print(' ')
  while True:
    print(' ')
    j3 = input('Qual a sua jogada?: ')
    if j3 == j1 or j3 == j2:
      continue
    if j3 == 'a1' and a1 == 'O':
      print(' ')
      print('Casa já selecionada')
      print(' ')
      continue
    elif j3 == 'a2' and a2 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if j3 == 'a3' and a3 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    elif j3 == 'b1' and b1 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if j3 == 'b2' and b2 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    elif j3 == 'b3' and b3 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if j3 == 'c1' and c1 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    elif j3 == 'c2' and c2 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if j3 == 'c3' and c3 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if j3 == 'a1' and a1 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    elif j3 == 'a2' and a2 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if j3 == 'a3' and a3 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    elif j3 == 'b1' and b1 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if j3 == 'b2' and b2 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    elif j3 == 'b3' and b3 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if j3 == 'c1' and c1 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    elif j3 == 'c2' and c2 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if j3 == 'c3' and c3 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if j3.lower() == 'a1':
      break
    if j3.lower() == 'a2':
      break
    elif j3.lower() == 'a3':
      break
    if j3.lower() == 'b1':
      break
    elif j3.lower() == 'b2':
      break
    elif j3.lower() == 'b3':
      break
    if j3.lower() == 'c1':
      break
    elif j3.lower() == 'c2':
      break
    elif j3.lower() == 'c3':
      break
    if j3 != casas:
      print('Digite uma casa corretamente!')
      continue
      print(' ')
      print('Essas são as casas disponivéis: {}'. format(casas))
  print(' ')
  if j3 == 'a1':
    a1 = 'X'
  elif j3 == 'a2':
    a2 = 'X'
  if j3 == 'a3':
    a3 = 'X'
  elif j3 == 'b1':
    b1 = 'X'
  if j3 == 'b2':
    b2 = 'X'
  elif j3 == 'b3':
    b3 = 'X'
  if j3 == 'c1':
    c1 = 'X'
  elif j3 == 'c2':
    c2 = 'X'
  if j3 == 'c3':
    c3 = 'X'
  win_X()
  
  if a1 == 'X' and a2 == 'X':
    a3 = 'O'
  elif a2 == 'X' and a3 == 'X':
    a1 = 'O'
  if a1 == 'X' and a3 == 'X' and a3 == 'X' and c3 == 'X':  
    a2 = 'O'
  elif a1 == 'X' and a3 == 'X' and a1 == 'X' and c1 == 'X':
    a2 == 'O'
  if a1 == 'X' and b1 == 'X':
    c1 = 'O'
  elif a1 == 'X' and b2 == 'X':
    c3 = 'O'
  elif a1 == 'X' and c3 == 'X': 
    c1  = 'O'
  if b1 == 'X' and c1 == 'X':
    a1 = 'O'
  elif b2 == 'X' and c3 == 'X':
    b1 = 'O'
  if a2 == 'X' and b2 == 'X':
    c2 = 'O'
  elif b2 == 'X' and c2 == 'X':
    a2 = 'O'
  if a3 == 'X' and c1 == 'X':
    c3 = 'O'
  elif a3 == 'X' and b3 == 'X':
    c3 ='O'
  elif b3 == 'X' and c3 == 'X':
    a3 = 'O'
  if b1 == 'X' and b3 == 'X': 
    c3 = 'O'
  elif b2 == 'X' and b3 == 'X':
    b1 = 'O'
  if b1 == 'X' and b2 == 'X': 
    b3 = 'O'
  elif c1 == 'X' and c2 == 'X':
    c3 = 'O'
  if c1 == 'X' and c3 == 'X':
    c2 = 'O'
  elif c2 == 'X' and c3 == 'X':
    c1 = 'O'
  if a3 == 'X' and b2 == 'X':
    c1 = 'O'
  elif a1 == 'X' and c1 == 'X':
    b1 = 'O'
  if a3 == 'X' and c3 == 'X':
    b3 = 'O'
  elif a1 == '_' and b1 == '_' and c2 == '_' and c3 == '_':
    b1 = 'O'
  
  print(' ')
  tabela()
  win_O()
  print(' ')

  while True:
    print(' ')
    j4 = input('Qual a sua jogada?: ')
    if j4 == j1 or j4 == j2 and j4 == j3:
      continue
    if j4 == 'a1' and a1 == 'O':
      print(' ')
      print('Casa já selecionada')
      print(' ')
      continue
    elif j4 == 'a2' and a2 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if j4 == 'a3' and a3 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    elif j4 == 'b1' and b1 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if j4 == 'b2' and b2 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    elif j4 == 'b3' and b3 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if j4 == 'c1' and c1 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    elif j4 == 'c2' and c2 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if j4 == 'c3' and c3 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if j4 == 'a1' and a1 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    elif j4 == 'a2' and a2 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if j4 == 'a3' and a3 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    elif j4 == 'b1' and b1 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if j4 == 'b2' and b2 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    elif j4 == 'b3' and b3 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if j4 == 'c1' and c1 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    elif j4 == 'c2' and c2 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if j4 == 'c3' and c3 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if j4.lower() == 'a1':
      break
    if j4.lower() == 'a2':
      break
    elif j4.lower() == 'a3':
      break
    if j4.lower() == 'b1':
      break
    elif j4.lower() == 'b2':
      break
    elif j4.lower() == 'b3':
      break
    if j4.lower() == 'c1':
      break
    elif j4.lower() == 'c2':
      break
    elif j4.lower() == 'c3':
      break
    if j4 != casas:
      print('Digite uma casa corretamente!')
      continue
      print(' ')
      print('Essas são as casas disponivéis: {}'. format(casas))
  print(' ')
  if j4 == 'a1':
    a1 = 'X'
  elif j4 == 'a2':
    a2 = 'X'
  if j4 == 'a3':
    a3 = 'X'
  elif j4 == 'b1':
    b1 = 'X'
  if j4 == 'b2':
    b2 = 'X'
  elif j4 == 'b3':
    b3 = 'X'
  if j4 == 'c1':
    c1 = 'X'
  elif j4 == 'c2':
    c2 = 'X'
  if j4 == 'c3':
    c3 = 'X'
  win_X()
  
  if a1 == 'X' and a2 == 'X':
    a3 = 'O'
  elif a2 == 'X' and a3 == 'X':
    a1 = 'O'
  if a1 == 'X' and a3 ==  'X':
    a2 = 'O'
  if a1 == 'X' and b1 == 'X':
    c1 = 'O'
  elif a1 == 'X' and b2 == 'X':
    c3 = 'O'
  if a1 == 'X' and c1 == 'X': 
    b1 = 'O'
  elif a1 == 'X' and c3 == 'X': 
    c1  = 'O'
  if b1 == 'X' and c1 == 'X':
    a1 = 'O'
  elif b2 == 'X' and c3 == 'X':
    b1 = 'O'
  if a2 == 'X' and b2 == 'X':
    c2 = 'O'
  elif b2 == 'X' and c2 == 'X':
    a2 = 'O'
  elif a3 == 'X' and b3 == 'X':
    c3 ='O'
  if a3 == 'X' and c3 == 'X':
    b3 = 'O'
  elif b3 == 'X' and c3 == 'X':
    a3 = 'O'
  if b1 == 'X' and b3 == 'X': 
    c3 = 'O'
  elif b2 == 'X' and b3 == 'X':
    b1 = 'O'
  if b1 == 'X' and b2 == 'X': 
    b3 = 'O'
  elif c1 == 'X' and c2 == 'X':
    c3 = 'O'
  if c1 == 'X' and c3 == 'X':
    c2 = 'O'
  elif c2 == 'X' and c3 == 'X':
    c1 = 'O'
  if a3 == 'X' and b2 == 'X':
    c1 = 'O'
  elif c1 == 'O' and c2 == 'X' and c3 == '_':
    c3 = 'O'
  if c1 == 'X' and c2 == '_' and c3 == '_':
    c2 = 'O'
  elif c3 == 'X' and c2 == '_' and c1 == '_':
    c2 = 'O'
  if c2 == 'X' and c3 == '_' and c1 == '_':
    c1 = 'O'
  elif a1 == 'X' and a2 == '_' and a3 == '_':
    a3 = 'O'
  elif a2 == 'X' and a1 == '_' and a3 == '_':
    a3 = 'O'
  elif a3 == 'X' and a2 == '_' and a1 == '_':
    a1 = 'O'
    
  tabela()
  win_O()
  print(' ')
  print(' ')
  while True:
    print(' ')
    j5 = input('Qual a sua jogada?: ')
    if j5 == j1 or j5 == j2 and j5 == j3 and j5 == j4:
      continue
    if j5 == 'a1' and a1 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    elif j5 == 'a2' and a2 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if j5 == 'a3' and a3 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    elif j5 == 'b1' and b1 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if j5 == 'b2' and b2 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    elif j5 == 'b3' and b3 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if j5 == 'c1' and c1 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    elif j5 == 'c2' and c2 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if j5 == 'c3' and c3 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if j5 == 'a1' and a1 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    elif j5 == 'a2' and a2 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if j5 == 'a3' and a3 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    elif j5 == 'b1' and b1 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if j5 == 'b2' and b2 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    elif j5 == 'b3' and b3 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if j5 == 'c1' and c1 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    elif j5 == 'c2' and c2 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if j5 == 'c3' and c3 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if j5.lower() == 'a1':
      break
    if j5.lower() == 'a2':
      break
    elif j5.lower() == 'a3':
      break
    if j5.lower() == 'b1':
      break
    elif j5.lower() == 'b2':
      break
    elif j5.lower() == 'b3':
      break
    if j5.lower() == 'c1':
      break
    elif j5.lower() == 'c2':
      break
    elif j5.lower() == 'c3':
      break
    if j5 != casas:
      print('Digite uma casa corretamente!')
      continue
      print(' ')
      print('Essas são as casas disponivéis: {}'. format(casas))
  print(' ')
  if j5 == 'a1':
    a1 = 'X'
  elif j5 == 'a2':
    a2 = 'X'
  if j5 == 'a3':
    a3 = 'X'
  elif j5 == 'b1':
    b1 = 'X'
  if j5 == 'b2':
    b2 = 'X'
  elif j5 == 'b3':
    b3 = 'X'
  if j5 == 'c1':
    c1 = 'X'
  elif j5 == 'c2':
    c2 = 'X'
  if j5 == 'c3':
    c3 = 'X'
  
  tabela()
  print(' ')
  exit('DEU VELHA!')

def maquina_começa():
  global a1 
  global a2 
  global a3
  global b1 
  global b2 
  global b3
  global c1 
  global c2 
  global c3
  a1 = 'O'
  print(' ')
  tabela()
  casas = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
  
  while True:
    print(' ')
    jo1 = input('Qual a sua jogada?: ')
    if jo1 == 'a1' and a1 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if jo1.lower() == 'a2':
      break
    elif jo1.lower() == 'a3':
      break
    if jo1.lower() == 'b1':
      break
    elif jo1.lower() == 'b2':
      break
    elif jo1.lower() == 'b3':
      break
    if jo1.lower() == 'c1':
      break
    elif jo1.lower() == 'c2':
      break
    elif jo1.lower() == 'c3':
      break
    if jo1 != casas:
      print('Digite uma casa corretamente!')
      continue 
      print(' ')
      print('Essas são as casas disponivéis: {}'. format(casas))
  if jo1 == 'a1':
    a1 = 'X'
  elif jo1 == 'a2':
    a2 = 'X'
  if jo1 == 'a3':
    a3 = 'X'
  elif jo1 == 'b1':
    b1 = 'X'
  if jo1 == 'b2':
    b2 = 'X'
  elif jo1 == 'b3':
    b3 = 'X'
  if jo1 == 'c1':
    c1 = 'X'
  elif jo1 == 'c2':
    c2 = 'X'
  if jo1 == 'c3':
    c3 = 'X'
  
  if b2 == 'X':
    c3 = 'O'
  elif a2 == 'X' or b1 == 'X' or b3 == 'X' or c2 == 'X' or a3 == 'X' or c1 == 'X' or a3 == 'X':
    b2 = 'O'
  
  tabela()
  print(' ')
  while True:
    print(' ')
    jo2 = input('Qual a sua jogada?: ')
    if jo2 == jo1:
      continue
    if jo2 == 'a1' and a1 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    elif jo2 == 'a2' and a2 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if jo2 == 'a3' and a3 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    elif jo2 == 'b1' and b1 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if jo2 == 'b2' and b2 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    elif jo2 == 'b3' and b3 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if jo2 == 'c1' and c1 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    elif jo2 == 'c2' and c2 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if jo2 == 'c3' and c3 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if jo2 == 'a1' and a1 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    elif jo2 == 'a2' and a2 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if jo2 == 'a3' and a3 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    elif jo2 == 'b1' and b1 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if jo2 == 'b2' and b2 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    elif jo2 == 'b3' and b3 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if jo2 == 'c1' and c1 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    elif jo2 == 'c2' and c2 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if jo2 == 'c3' and c3 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if jo2.lower() == 'a1':
      break
    if jo2.lower() == 'a2':
      break
    elif jo2.lower() == 'a3':
      break
    if jo2.lower() == 'b1':
      break
    elif jo2.lower() == 'b2':
      break
    elif jo2.lower() == 'b3':
      break
    if jo2.lower() == 'c1':
      break
    elif jo2.lower() == 'c2':
      break
    elif jo2.lower() == 'c3':
      break
    if jo2 != casas:
      print('Digite uma casa corretamente!')
      continue
      print(' ')
      print('Essas são as casas disponivéis: {}'. format(casas))
  if jo2 == 'a1':
    a1 = 'X'
  elif jo2 == 'a2':
    a2 = 'X'
  if jo2 == 'a3':
    a3 = 'X'
  elif jo2 == 'b1':
    b1 = 'X'
  if jo2 == 'b2':
    b2 = 'X'
  elif jo2 == 'b3':
    b3 = 'X'
  if jo2 == 'c1':
    c1 = 'X'
  elif jo2 == 'c2':
    c2 = 'X'
  if jo2 == 'c3':
    c3 = 'X'
  win_X()
  
  if a1 == 'X' and a2 == 'X':
      a3 = 'O'
  elif a2 == 'X' and a3 == 'X':
      a1 = 'O'
  if a1 == 'X' and a3 ==  'X':
    a2 = 'O'
  if a1 == 'X' and b1 == 'X':
    c1 = 'O'
  elif a1 == 'X' and b2 == 'X':
    c3 = 'O'
  if a1 == 'X' and c1 == 'X': 
    b1 = 'O'
  elif a1 == 'X' and c3 == 'X': #força o jogador a jogar
      c1  = 'O'
  if b1 == 'X' and c1 == 'X':
      a3 = 'O'
  elif b2 == 'X' and c3 == 'X':
    b1 = 'O'
  if a2 == 'X' and b2 == 'X':
    c2 = 'O'
  elif b2 == 'X' and c2 == 'X':
    a2 = 'O'
  if a3 == 'X' and c1 == 'X':
    c3 = 'O'
  elif a3 == 'X' and b3 == 'X':
    c3 == 'O'
  if a3 == 'X' and c3 == 'X':
    b3 = 'O'
  elif b3 == 'X' and c3 == 'X':
    a3 = 'O'
  if b1 == 'X' and b3 == 'X': #pode gera ataque 
    c3 = 'O'
  elif b2 == 'X' and b3 == 'X':
    b1 = 'O'
  if b1 == 'X' and b2 == 'X': #cria uma jogada 
    b3 = 'O'
  elif c1 == 'X' and c2 == 'X':
    c3 = 'O'
  if c1 == 'X' and c3 == 'X':
    c2 = 'O'
  elif c2 == 'X' and c3 == 'X':
    c1 = 'O'
  if a3 == 'X' and b2 == 'X':
    c1 = 'O'
  if c1 == 'X' and b2 == 'X':
    a3 = 'O'
  if a1 == 'X' and b2 == 'O' and b3 == 'X':
    c2 = 'O'
  elif a1 == 'X' and b2 == 'O' and c2 == 'X':
    b3 = 'O'
  if a2 == 'X' and b2 == 'O' and b1 == 'X':
    a3 = 'O'
  elif a2 == 'X' and b2 == 'O' and b3 == 'X':
    a3 = 'O'
  if a2 == 'X' and b2 == 'O' and c1 == 'X':
    a1 = 'O'
  elif a2 == 'X' and b2 == 'O' and c2 == 'X':
    a3 = 'O'
  if a2 == 'X' and b2 == 'O' and c3 == 'X':
    a3 = 'O'
  if a3 == 'X' and b2 == 'O' and b1 == 'X':
    c2 = 'O'
  elif a3 == 'X' and b2 == 'O' and c2 == 'X':
    b1 = 'O'
  elif b1 == 'X' and b2 == 'O' and c2 == 'X':
    c1 = 'O'
  if b1 == 'X' and b2 == 'O' and c3 == 'X':
    c1 = 'O'
  elif b3 == 'X' and b2 == 'O' and c1 == 'X':
    c3 = 'O'
  if b3 == 'X' and b2 == 'O' and c2 == 'X':
    c1 = 'O'
  win_O()
  print(' ')
  tabela()
  print(' ')
  
  while True:
    print(' ')
    jo3 = input('Qual a sua jogada?: ')
    if jo3 == jo1 or jo3 == jo2:
      continue
    if jo3 == 'a1' and a1 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    elif jo3 == 'a2' and a2 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if jo3 == 'a3' and a3 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    elif jo3 == 'b1' and b1 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if jo3 == 'b2' and b2 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    elif jo3 == 'b3' and b3 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if jo3 == 'c1' and c1 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    elif jo3 == 'c2' and c2 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if jo3 == 'c3' and c3 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if jo3 == 'a1' and a1 == 'X':
      print('Casa já selecionada anteriormente')
      continue
    elif jo3 == 'a2' and a2 == 'X':
      print('Casa já selecionada anteriormente')
      continue
    if jo3 == 'a3' and a3 == 'X':
      print('Casa já selecionada anteriormente')
      continue
    elif jo3 == 'b1' and b1 == 'X':
      print('Casa já selecionada anteriormente')
      print(' ')
      continue
    if jo3 == 'b2' and b2 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    elif jo3 == 'b3' and b3 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if jo3 == 'c1' and c1 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    elif jo3 == 'c2' and c2 == 'X':
      print(' ')
      print('Casa já selecionada')
      continue
    if jo3 == 'c3' and c3 == 'X':
      print(' ')
      print('Casa já selecionada')
      continue
    if jo3.lower() == 'a1':
      break
    if jo3.lower() == 'a2':
      break
    elif jo3.lower() == 'a3':
      break
    if jo3.lower() == 'b1':
      break
    elif jo3.lower() == 'b2':
      break
    elif jo3.lower() == 'b3':
      break
    if jo3.lower() == 'c1':
      break
    elif jo3.lower() == 'c2':
      break
    elif jo3.lower() == 'c3':
      break
    if jo3 != casas:
      print('Digite uma casa corretamente!')
      continue
      print(' ')
      print('Essas são as casas disponivéis: {}'. format(casas))
  if jo3 == 'a1':
    a1 = 'X'
  elif jo3 == 'a2':
    a2 = 'X'
  if jo3 == 'a3':
    a3 = 'X'
  elif jo3 == 'b1':
    b1 = 'X'
  if jo3 == 'b2':
    b2 = 'X'
  elif jo3 == 'b3':
    b3 = 'X'
  if jo3 == 'c1':
    c1 = 'X'
  elif jo3 == 'c2':
    c2 = 'X'
  if jo3 == 'c3':
    c3 = 'X'
  win_X()
  
  
  if a1 == 'X' and a2 == 'X':
    a3 = 'O'
  elif a2 == 'X' and a3 == 'X':
    a1 = 'O'
  if a1 == 'X' and a3 == 'X' and a3 == 'X' and c3 == 'X': 
    a2 = 'O'
  elif a1 == 'X' and a3 == 'X' and a1 == 'X' and c1 == 'X':
    a2 == 'O'
  if a1 == 'X' and b1 == 'X':
    c1 = 'O'
  elif a1 == 'X' and b2 == 'X':
    c3 = 'O'
  elif a1 == 'X' and c3 == 'X': #força o jogador a jogar
    c1  = 'O'
  if b1 == 'X' and c1 == 'X':
    a1 = 'O'
  elif b2 == 'X' and c3 == 'X':
    b1 = 'O'
  if a2 == 'X' and b2 == 'X':
    c2 = 'O'
  elif b2 == 'X' and c2 == 'X':
    a2 = 'O'
  if a3 == 'X' and c1 == 'X':
    c3 = 'O'
  elif a3 == 'X' and b3 == 'X':
    c3 ='O'
  elif b3 == 'X' and c3 == 'X':
    a3 = 'O'
  if b1 == 'X' and b3 == 'X':  
    c3 = 'O'
  elif b2 == 'X' and b3 == 'X':
    b1 = 'O'
  if b1 == 'X' and b2 == 'X': 
    b3 = 'O'
  elif c1 == 'X' and c2 == 'X':
    c3 = 'O'
  if c1 == 'X' and c3 == 'X':
    c2 = 'O'
  elif c2 == 'X' and c3 == 'X':
    c1 = 'O'
  if a3 == 'X' and b2 == 'X':
    c1 = 'O'
  if c1 == 'X' and b2 == 'X':
    a3 = 'O'
  elif a1 == 'X' and c1 == 'X':
    b1 = 'O'
  if a3 == 'X' and c3 == 'X':
    b3 = 'O'
  elif a1 == '_' and b1 == '_' and c2 == '_' and c3 == '_':
    b1 = 'O'
  win_O()
  print(' ')
  tabela()
  print(' ')
  
  while True:
    print(' ')
    jo4 = input('Qual a sua jogada?: ')
    if jo4 == jo1 or jo4 == jo2 and jo4 == jo3:
      continue
    elif jo3 == 'a1' and a1 == 'O':
      print(' ')
      print('Casa já selecionada')
    elif jo3 == 'a2' and a2 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if jo3 == 'a3' and a3 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    elif jo4 == 'b1' and b1 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if jo4 == 'b2' and b2 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    elif jo4 == 'b3' and b3 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if jo4 == 'c1' and c1 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    elif jo4 == 'c2' and c2 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if jo4 == 'c3' and c3 == 'O':
      print(' ')
      print('Casa já selecionada')
      continue
    if jo4 == 'a1' and a1 == 'X':
      print('Casa já selecionada anteriormente')
      continue
    elif jo4 == 'a2' and a2 == 'X':
      print('Casa já selecionada anteriormente')
      continue
    if jo4 == 'a3' and a3 == 'X':
      print('Casa já selecionada anteriormente')
      continue
    elif jo4 == 'b1' and b1 == 'X':
      print('Casa já selecionada anteriormente')
      print(' ')
      continue
    if jo4 == 'b2' and b2 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    elif jo4 == 'b3' and b3 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    if jo4 == 'c1' and c1 == 'X':
      print(' ')
      print('Casa já selecionada anteriormente')
      continue
    elif jo4 == 'c2' and c2 == 'X':
      print(' ')
      print('Casa já selecionada')
      continue
    if jo4 == 'c3' and c3 == 'X':
      print(' ')
      print('Casa já selecionada')
      continue
    if jo4.lower() == 'a1':
      break
    if jo4.lower() == 'a2':
      break
    elif jo4.lower() == 'a3':
      break
    if jo4.lower() == 'b1':
      break
    elif jo4.lower() == 'b2':
      break
    elif jo4.lower() == 'b3':
      break
    if jo4.lower() == 'c1':
      break
    elif jo4.lower() == 'c2':
      break
    elif jo4.lower() == 'c3':
      break
    if jo4 != casas:
      print('Digite uma casa corretamente!')
      continue
      print(' ')
      print('Essas são as casas disponivéis: {}'. format(casas))
  if jo4 == 'a1':
    a1 = 'X'
  elif jo4 == 'a2':
    a2 = 'X'
  if jo4 == 'a3':
    a3 = 'X'
  elif jo4 == 'b1':
    b1 = 'X'
  if jo4 == 'b2':
    b2 = 'X'
  elif jo4 == 'b3':
    b3 = 'X'
  if jo4 == 'c1':
    c1 = 'X'
  elif jo4 == 'c2':
    c2 = 'X'
  if jo4 == 'c3':
    c3 = 'X'
  
  if a2 == '_':
    a2 = 'O'
  if b2 == '_':
    b2 = 'O'
  if c2 == '_':
    c2 = 'O'
  if b1 == '_':
    b1 = 'O'
  if c1 == '_':
    c1 = 'O'
  if a3 == '_':
    a3 = 'O'
  if b3 == '_':
    b3 = 'O'
  if b3 == '_':
    b3 = 'O'
  
  tabela()
  print(' ')
  exit('DEU VELHA!')

import random 
print('*-JOGO DA VELHA-*')
print(' ')
print('OI, VOCÊ ESTÁ INICIANDO O JOGO DA VELHA!')
print(' ')
jogador = str(input(' Antes de começar, qual seu nome? '))
sorteio = [jogador, 'a Máquina']
escolhido = random.choice(sorteio)
print('Quem começará jogando será {}!'.format(escolhido))
print(' ')
if escolhido == jogador:
  jogador_começa()
elif escolhido == 'a Máquina':
  maquina_começa()
