# coding:utf-8
import sys, time

class Indicator:

    spin = 1
    waiting = 2
    beer = 3
    loading = 4

    def __init__(self,indis,dur):
        self.isStop = False
        self.items = indis
        self.dur = dur

    @staticmethod
    def progress(Type):
        if Type == Indicator.spin:
            items = ('|','/','ー','\\','|','/','ー','\\')
            speed = 0.03
            pro = Indicator(items,speed)
            pro.start()
        elif Type == Indicator.waiting:
            items = ('Waiting','Waiting.','Waiting..','Waiting...')
            speed = 0.3
            pro = Indicator(items,speed)
            pro.start()
        elif Type == Indicator.beer:
            items = ('🍺 '*1,'🍺 '*2,'🍺 '*3,'🍺 '*4,'🍺 '*5,'🍺 '*6)
            speed = 0.1
            pro = Indicator(items,speed)
            pro.start()
        elif Type == Indicator.loading:
            items = ('Loading','Loading.','Loading..','Loading...','Loading....')
            speed = 0.3
            pro = Indicator(items,speed)
            pro.start()

    def Indicator(self):
        for num in range(0,len(self.items)):
            self.bufferOut(self.items[num],self.dur)

    def bufferOut(self,buf,t):
        space = ' '
        sys.stdout.write(buf + '\r')
        sys.stdout.flush()
        time.sleep(t)
        print '\b' + space * len(buf) + '\r',
        time.sleep(t)

    def start(self):
        while self.isStop == False:
            self.Indicator()

    def stop(self):
        self.isStop = True