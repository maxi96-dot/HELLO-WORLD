class Automa:
  def __init__(self):
    self.STATO = 0

  def evento(self, inp):
    if(self.STATO == 0):
      if(inp == 0):
        self.STATO = 0
      else:
        self.STATO = 1
    else:
      self.STATO = 1

  def printStato(self):
    print('Lo stato corrente è {}'.format(self.STATO))