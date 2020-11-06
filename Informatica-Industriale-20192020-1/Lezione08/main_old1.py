from scheduler import Scheduler
from clock import Clock

s = Scheduler()
c1 = Clock('Clock 1', 10)
c2 = Clock('Clock 2', 3)
c3 = Clock('Clock 3', 2)

event = c1.start(3)
s.addEvent(event)
event = c2.start(2)
s.addEvent(event)
event = c3.start(12)
s.addEvent(event)

for _ in range(20):
  event = s.nextEvent()
  new_event = event.actor.update(event)
  s.addEvent(new_event)