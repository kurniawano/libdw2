import amigobot.amigobot as am
import time

myRobot = am.Amigobot()
myRobot.motorOutput(0.05,0)
time.sleep(5)
myRobot.halt()
myRobot.close()
