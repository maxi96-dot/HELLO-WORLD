def fattorialeIterativo(num):
    risultato = num
    while (num > 1):
        risultato = risultato * (num - 1)
        num = num - 1
    return risultato

def fattorialeRicorsivo(num):
  if(num == 1):
    return 1
  return num * fattorialeRicorsivo(num - 1)

def fattorialeSemplice(num):
  if(num == 1):
    return 1
  if(num == 2):
    return 2
  if(num == 3):
    return 6
  if(num == 4):
    return 24
  return 0