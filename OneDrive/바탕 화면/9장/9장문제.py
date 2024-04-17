class car:
    def method(self):
        print('슈퍼 클래스')

class sedan(car):
    def method(self):
        print('서브 클래스')

mycar=car()
mysedan=sedan()
mycar.method()
mysedan.method()
'답=3번'

class car:
    speed=0

    def upspeed(self,value):
        self.speed=self.speed+value
class RVcar(car):
    seatNum=0

    def getSeatNum(self):
        return self.seatNum
