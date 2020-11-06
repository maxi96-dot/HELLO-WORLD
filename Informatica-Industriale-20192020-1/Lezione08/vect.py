class Vect:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def add(self, vect):
    self.x += vect.x
    self.y += vect.y

  def addScaled(self, vect, s):
    self.x += s*vect.x
    self.y += s*vect.y