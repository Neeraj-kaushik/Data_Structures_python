class Time():
    def __init__(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes
    def addtime(t1,t2):
        t3=Time(0,0)
        if t1.minutes+t2.minutes>60:
            t3.hours=(t1.minutes+t2.minutes)//60
        t3.hours=t1.hours+t2.hours+t3.hours
        t3.minutes=(t1.minutes+t2.minutes)-(((t1.minutes+t2.minutes)/60)*60)
        return t3
    def displaytime(self):
        return "time is",self.hours,"hours",self.minutes,"minutes"
    def displayminutes(self):
        return (self.hours*60)+self.minutes

a=Time(2,45)
b=Time(3,20)
c=Time(a,b)
print(c.addtime())
print(c.displaytime())
print(c.displayminutes())
