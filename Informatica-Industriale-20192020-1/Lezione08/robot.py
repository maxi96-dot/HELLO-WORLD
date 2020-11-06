from vect import Vect

class Robot:
  def __init__(self, name, pos0, vel0):
    self.name = name
    self.pos  = Vect(pos0.x, pos0.y)
    self.vel  = Vect(vel0.x, vel0.y)
    self.timeLastUpdate = 0

    self.time = list()
    self.posX = list()
    self.posY = list()

  def update(self, event, env):
    delta = event.time - self.timeLastUpdate
    self.timeLastUpdate = event.time
    self.pos.addScaled(self.vel, delta)

    wall = env.checkCollision(self.pos)
    if wall != None:
      if abs(wall.xe - wall.xo) > abs(wall.ye - wall.yo):
        self.vel.y *= (-1)
      else:
        self.vel.x *= (-1)

    self.time.append(event.time)
    self.posX.append(self.pos.x)
    self.posY.append(self.pos.y)

  def printData(self):
    for k in range(len(self.time)):
      print(f'{self.name} - {self.time[k]} ({self.posX[k]}, {self.posY[k]})')