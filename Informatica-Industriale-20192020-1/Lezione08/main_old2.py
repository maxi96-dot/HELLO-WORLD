from scheduler import Scheduler
from vect import Vect
from oracle import Oracle
from robot import Robot

s = Scheduler()
o = Oracle(.1)

pos0 = Vect(0,0)
vel0 = Vect(+2, 0)
r1 = Robot('robot 1', pos0, vel0)
pos0 = Vect(0,0)
vel0 = Vect(0,+1)
r2 = Robot('robot 2', pos0, vel0)

o.addActor(r1)
o.addActor(r2)

event = o.start(0)
s.addEvent(event)

for _ in range(20):
  event = s.nextEvent()
  new_event = o.update(event)
  s.addEvent(new_event)

r1.printData()
print(f'------------')
r2.printData()