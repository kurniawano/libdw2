import amigobot.amigobot as am
import time

# Open connection with Amigobot
myRobot = am.Amigobot()

# Move straight fvel = 0.05 m/s
myRobot.motorOutput(0.05,0)
time.sleep(5)

# rotate left omega = 0.05 rad/s
myRobot.motorOutput(0,0.05)
time.sleep(5)

# rotate right omega = -0.05 rad/s
myRobot.motorOutput(0,-0.05)
time.sleep(5)

# stop
myRobot.halt()

# close connection
myRobot.close()
