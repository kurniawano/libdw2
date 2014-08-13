import soar.outputs.pioneer as p
from soar.io import io

class Amigobot(p.Pioneer):
    def __init__(self):
        p.Pioneer.__init__(self)
        self.start()

    def start(self):
        p.Pioneer.startmoving(self)

    def stop(self):
        p.Pioneer.stopmoving(self)
        
    def halt(self):
        self.stop()
        self.start()

    def close(self):
        self.stop()
        p.Pioneer.destroy(self)

    def getSensorInput(self):
        inp = io.SensorInput(self)
        return inp

    def getSonars(self):
        inp=self.getSensorInput()
        return inp.sonars

    def getOdometry(self):
        inp=self.getSensorInput()
        return inp.odometry
