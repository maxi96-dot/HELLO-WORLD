from scheduler import Scheduler
from vect import Vect
from oracle import Oracle
from robot import Robot

class Wall:
  def __init__(self, xo, yo, xe, ye):
    self.xo = xo
    self.yo = yo
    self.xe = xe
    self.ye = ye

class Environment:
  def __init__(self):
    self.walls = list()

  def addWall(self, wall):
    self.walls.append(wall)

  def checkCollision(self, pos):
    for wall in self.walls:
      if wall.xo < pos.x and pos.x < wall.xe and wall.yo < pos.y and pos.y < wall.ye:
        return wall
    return None


e = Environment()
s = Scheduler()
o = Oracle(1, e)

w = Wall(100, 0, 120, 100)
e.addWall(w)
w = Wall(-120, 0, -100, 100)
e.addWall(w)

pos0 = Vect(0,50)
vel0 = Vect(2, 0.1)
r1 = Robot('robot 1', pos0, vel0)

o.addActor(r1)

event = o.start(0)
s.addEvent(event)
for _ in range(100):
  event = s.nextEvent()
  new_event = o.update(event)
  s.addEvent(new_event)

r1.printData()