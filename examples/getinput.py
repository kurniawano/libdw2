import amigobot.amigobot as am
import time

def moveAndRead():
    inp = robot.getSensorInput()
    print "Sonars : ", inp.sonars
    print "Odometry : ", inp.odometry
    robot.motorOutput(0,0.05)

robot = am.Amigobot()

print "Press Ctrl-C stop."
any = raw_input("Press any key to continue...")

while True:
    try:
        moveAndRead()
        time.sleep(1)
    except KeyboardInterrupt:
        break

robot.halt()
robot.close()


