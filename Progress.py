# coding:utf-8
import sys, time

class Indicator:

    _instance = None
    INDIGICATOR = 1
    STRINGPROGRESS = 2
    BEERPROGRESS = 3
    LOADINGINGICATOR = 4

    def __init__(self,indis,dur):
        self.isStop = False
        self.indis = indis
        self.dur = dur

    @staticmethod
    def Ind(indiType):
        if indiType == Indicator.INDIGICATOR:
            indis = ('|','/','ー','\\','|','/','ー','\\')
            speed = 0.03
            pro = Indicator(indis,speed)
            pro.start()
        elif indiType == Indicator.STRINGPROGRESS:
            indis = ('Waiting','Waiting.','Waiting..','Waiting...')
            speed = 0.3
            pro = Indicator(indis,speed)
            pro.start()
        elif indiType == Indicator.BEERPROGRESS:
            indis = ('🍺 '*1,'🍺 '*2,'🍺 '*3,'🍺 '*4,'🍺 '*5,'🍺 '*6)
            speed = 0.1
            pro = Indicator(indis,speed)
            pro.start()
        elif indiType == Indicator.LOADINGINGICATOR:
            indis = ('Loading','Loading.','Loading..','Loading...','Loading....')
            speed = 0.3
            pro = Indicator(indis,speed)
            pro.start()

    def Indicator(self):
        for num in range(0,len(self.indis)):
            self.bufferOut(self.indis[num],self.dur)

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

    def _TEST(self):
        while self.isStop == False:
            self.Indicator()

    def stop(self):
        self.isStop = True

# class PBar:
#
#     def __init__(self, bar):
#         self.bar = bar
#
#     def ProgressBar(self,progress):
#         body = 0
#         while progress != 100:
#             space = ' '
#             if progress % 5 == 0:
#                  body+=1
#             self.bufferProOut('🍺 ',0.02, progress,body)
#             progress += 1
#
#     def startBar(self,pro):
#         while pro != 100:
#             self.PBar(pro)
#             pro+=2
#
#     def PBar(self,progress):
#         if progress % 5 == 0:
#              body+=1
#         self.bufferProt('🍺 ', progress,body)
#
#     def bufferProt(self, buf,pro,co):
#         sys.stdout.write( str(pro) + '%' + '[' + buf*co +']\r')
#         sys.stdout.flush()
#         print '\b' + '  ' + '\r',
#
#     def start(self):
#         while self.isStop == False:
#             self.ProgresBar()
#
#     def startIndi(self):
#         while self.isStop == False:
#             self.Indicator()
#
#     def stop(self):
#         self.isStop = True
#
#     def calcProposion(self,pas):
#         parcent = ((pas) / self.count) * 100
#         print ' {}%'.format(parcent)
#         return ' {}%'.format(parcent)
