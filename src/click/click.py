import sys
import random
import pyautogui as pa
#pa.PAUSE = 0.1

print("set mouse to starting position")
input()
sp = pa.position()
print("set mouse to end position")
input()
ep = pa.position()

w = ep.x - sp.x
h = ep.y - sp.y

while True:
    try:
        dx = random.randint(0, w)
        dy = random.randint(0, h)
        print("dx: " + str(dx))
        print("dy: " + str(dy))
        pa.click(sp.x + dx, sp.y + dy)
        print("click")
    except KeyboardInterrupt:
        print("bye")
        sys.exit()
